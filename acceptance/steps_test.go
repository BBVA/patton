package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"os/exec"
	"strings"

	"github.com/cucumber/godog"
	"github.com/cucumber/godog/gherkin"
)

type pattonParams struct {
	searchTerm, version string
	distro              string
	searchType          string
}

type pattonOutput struct {
	exitCode int
	stdout   []string
}
type execution struct {
	binaryPath,
	databasePath string
	params *pattonParams
	output *pattonOutput
}

func (ex *execution) iHaveSearchTerm(searchTerm string) error {
	ex.params.searchTerm = searchTerm

	return nil
}

func (ex *execution) iHaveSearchTermAndVersion(searchTerm, version string) error {
	ex.params.searchTerm = searchTerm
	ex.params.version = version

	return nil
}

func (ex *execution) itIsAWordpressPlugin() error {
	// return godog.ErrPending
	return nil
}

func (ex *execution) iHaveOutputOfPackageManager(distro string, rawPkgOutput *gherkin.DocString) error {
	ex.params.distro = distro
	ex.params.searchTerm = rawPkgOutput.Content

	return nil
}

func (ex *execution) iExecutePattonSearchWithSearchType(searchType string) error {
	ex.params.searchType = searchType

	cmd := exec.Command(ex.binaryPath, "-d", ex.databasePath, "-t", ex.params.searchType, "-v", ex.params.version, ex.params.searchTerm)
	stdout, _ := cmd.StdoutPipe()

	if err := cmd.Start(); err != nil {
		return fmt.Errorf("Error starting command: %v", err)
	}

	scanner := bufio.NewScanner(stdout)
	for scanner.Scan() {
		ex.output.stdout = append(ex.output.stdout, scanner.Text())
	}

	if err := cmd.Wait(); err != nil {
		if exitErr, ok := err.(*exec.ExitError); ok {
			ex.output.exitCode = exitErr.ExitCode()
		} else {
			return fmt.Errorf("Error starting command: %v", err)
		}
	}

	return nil
}

func (ex *execution) iGetAtLeastOneCve(table *gherkin.DataTable) error {
	count := 0
	// Remove titles from table
	for _, row := range table.Rows[1:] {
		for _, outLine := range ex.output.stdout {
			// Check CVE match
			if strings.Contains(outLine, row.Cells[0].Value) {
				count++
				break
			}
		}
	}

	// Don't take into account the title row
	if count < (len(table.Rows) - 1) {
		return fmt.Errorf("Only %d matches", count)
	}

	return nil
}

func (ex *execution) iHaveTheRawOutputOfInstalledPackagesForPackageManager(distro string, rawPkgOutput *gherkin.DocString) error {
	ex.params.distro = distro
	ex.params.searchTerm = rawPkgOutput.Content

	return nil
}

func (ex *execution) iExecutePattonSearchWithType(searchType string) error {
	ex.params.searchType = searchType

	cmd := exec.Command(ex.binaryPath, "-d", ex.databasePath, "-t", ex.params.searchType, "-v", ex.params.version, "-")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		return fmt.Errorf("Error setting stdin pipe for command: %v", err)
	}

	go func() {
		defer stdin.Close()
		_, err := io.WriteString(stdin, ex.params.searchTerm)
		if err != nil {
			log.Fatal(err)
		}
	}()

	stdout, _ := cmd.StdoutPipe()

	scanner := bufio.NewScanner(stdout)
	for scanner.Scan() {
		ex.output.stdout = append(ex.output.stdout, scanner.Text())
	}

	return nil
}

func (ex *execution) iGetAtLeastTheseVulnerabilities(arg1 *gherkin.DataTable) error {
	return godog.ErrPending
}

func (ex *execution) notFoundTheseFalsePositives(arg1 *gherkin.DataTable) error {
	return godog.ErrPending
}

func FeatureContext(s *godog.Suite) {
	exec := &execution{"patton", "patton.db.zst", &pattonParams{}, &pattonOutput{stdout: make([]string, 0)}}

	if binaryPath, ok := os.LookupEnv("PATTON_BINARY"); ok {
		exec.binaryPath = binaryPath
	}

	if dbPath, ok := os.LookupEnv("PATTON_DATABASE"); ok {
		exec.databasePath = dbPath
	}

	s.Step(`^I have search term "([^"]*)" and version "([^"]*)"$`, exec.iHaveSearchTermAndVersion)
	s.Step(`^I have search term "([^"]*)"$`, exec.iHaveSearchTerm)
	s.Step(`^It is a Wordpress plugin$`, exec.itIsAWordpressPlugin)
	s.Step(`^I have the output of "([^"]*)" package manager$`, exec.iHaveOutputOfPackageManager)
	s.Step(`^I execute Patton search with search type "([^"]*)"$`, exec.iExecutePattonSearchWithSearchType)
	s.Step(`^I get at least one cve$`, exec.iGetAtLeastOneCve)
	s.Step(`^I have the raw output of installed packages for "([^"]*)" package manager$`, exec.iHaveTheRawOutputOfInstalledPackagesForPackageManager)
	s.Step(`^I execute Patton search with type "([^"]*)"$`, exec.iExecutePattonSearchWithType)
	s.Step(`^I get at least these vulnerabilities$`, exec.iGetAtLeastTheseVulnerabilities)
	s.Step(`^Not found these false positives$`, exec.notFoundTheseFalsePositives)

	s.BeforeScenario(func(interface{}) {
		exec.params = &pattonParams{}
		exec.output = &pattonOutput{stdout: make([]string, 0)}
	})
}
