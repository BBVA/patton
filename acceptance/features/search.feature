Feature: Search Software Vulnerabilities

  Scenario: Find vulnerabilities in a product name with specific version
    Given I have search term "Apache JSPWiki" and version "2.11"
    When I execute Patton search with search type "product"
    Then I get at least one cve
      | CVE ID         | URL                                             |
      | CVE-2019-10090 | https://nvd.nist.gov/vuln/detail/CVE-2019-10090 |

  Scenario: Find vulnerabilities in a library that affects only when runs in a specific framework.
    Given I have search term "Tinymce Color Picker"
    And It is a Wordpress plugin
    When I execute Patton search with search type "fulltext"
    Then I get at least one cve
      | CVE ID         | URL                                            |
      | CVE-2014-3845  | https://nvd.nist.gov/vuln/detail/CVE-2014-3845 |

  Scenario: Find vulnerabilities in a system running Ubuntu package manager
      Given I have the output of "Ubuntu" package manager
        """
        ii  docker   1.4.1   amd64   Docker: the open-source application container engine
        """
      When I execute Patton search with search type "pkg_ubuntu"
      Then I get at least one cve
          | CVE ID         | URL                                                          |
          | CVE-2019-5736  | https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736 |


  Scenario: Find vulnerabilities in all installed packages in Ubuntu system
    Given I have the raw output of installed packages for "Ubuntu" package manager
      """
      Desired=Unknown/Install/Remove/Purge/Hold
      | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
      |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
      ||/ Name                              Version               Architecture          Description
      +++-=================================-=====================-=====================-========================================================================
      ii  accountsservice                   0.6.40-2ubuntu11.3    amd64                 query and manipulate user account information
      ii  acl                               2.2.52-3              amd64                 Access control list utilities
      ii  acpid                             1:2.0.26-1ubuntu2     amd64                 Advanced Configuration and Power Interface event daemon
      ii  adduser                           3.113+nmu3ubuntu4     all                   add and remove users and groups
      ii  apparmor                          2.10.95-0ubuntu2.7    amd64                 user-space parser utility for AppArmor
      ii  apport                            2.20.1-0ubuntu2.15    all                   automatically generate crash reports for debugging
      ii  apport-symptoms                   0.20                  all                   symptom scripts for apport
      ii  apt                               1.2.24                amd64                 commandline package manager
      ii  apt-transport-https               1.2.24                amd64                 https download transport for APT
      ii  apt-utils                         1.2.24                amd64                 package management related utility programs
      ii  aria2                             1.19.0-1build1        amd64                 High speed download utility
      ii  at                                3.1.18-2ubuntu1       amd64                 Delayed job execution and batch processing
      ii  aufs-tools                        1:3.2+20130722-1.1ubu amd64                 Tools to manage aufs filesystems
      ii  base-files                        9.4ubuntu4.5          amd64                 Debian base system miscellaneous files
      ii  base-passwd                       3.5.39                amd64                 Debian base system master password and group files
      ii  bash                              4.3-14ubuntu1.2       amd64                 GNU Bourne Again SHell
      ii  bash-completion                   1:2.1-4.2ubuntu1.1    all                   programmable completion for the bash shell
      ii  bcache-tools                      1.0.8-2               amd64                 bcache userspace tools
      ii  bind9-host                        1:9.10.3.dfsg.P4-8ubu amd64                 Version of 'host' bundled with BIND 9.X
      ii  bsdmainutils                      9.0.6ubuntu3          amd64                 collection of more utilities from FreeBSD
      ii  bsdutils                          1:2.27.1-6ubuntu3.3   amd64                 basic utilities from 4.4BSD-Lite
      ii  btrfs-tools                       4.4-1ubuntu1          amd64                 Checksumming Copy on Write Filesystem utilities
      ii  busybox-initramfs                 1:1.22.0-15ubuntu1    amd64                 Standalone shell setup for initramfs
      ii  busybox-static                    1:1.22.0-15ubuntu1    amd64                 Standalone rescue shell with tons of builtin utilities
      ii  byobu                             5.106-0ubuntu1        all                   text window manager, shell multiplexer, integrated DevOps environment
      ii  bzip2                             1.0.6-8               amd64                 high-quality block-sorting file compressor - utilities
      ii  ca-certificates                   20170717~16.04.1      all                   Common CA certificates
      ii  cgroupfs-mount                    1.2                   all                   Light-weight package to set up cgroupfs mounts
      ii  cloud-guest-utils                 0.27-0ubuntu24        all                   cloud guest utilities
      ii  cloud-init                        17.1-46-g7acc9e68-0ub all                   Init scripts for cloud instances
      ii  cloud-initramfs-copymods          0.27ubuntu1.4         all                   copy initramfs modules into root filesystem for later use
      ii  cloud-initramfs-dyn-netconf       0.27ubuntu1.4         all                   write a network interface file in /run for BOOTIF
      ii  command-not-found                 0.3ubuntu16.04.2      all                   Suggest installation of packages in interactive bash sessions
      ii  command-not-found-data            0.3ubuntu16.04.2      amd64                 Set of data files for command-not-found.
      ii  console-setup                     1.108ubuntu15.3       all                   console font and keymap setup program
      ii  console-setup-linux               1.108ubuntu15.3       all                   Linux specific part of console-setup
      ii  coreutils                         8.25-2ubuntu3~16.04   amd64                 GNU core utilities
      ii  cpio                              2.11+dfsg-5ubuntu1    amd64                 GNU cpio -- a program to manage archives of files
      ii  crda                              3.13-1                amd64                 wireless Central Regulatory Domain Agent
      ii  cron                              3.0pl1-128ubuntu2     amd64                 process scheduling daemon
      ii  cryptsetup                        2:1.6.6-5ubuntu2.1    amd64                 disk encryption support - startup scripts
      ii  cryptsetup-bin                    2:1.6.6-5ubuntu2.1    amd64                 disk encryption support - command line tools
      ii  curl                              7.47.0-1ubuntu2.5     amd64                 command line tool for transferring data with URL syntax
      ii  dash                              0.5.8-2.1ubuntu2      amd64                 POSIX-compliant shell
      ii  dbus                              1.10.6-1ubuntu3.3     amd64                 simple_parser interprocess messaging system (daemon and utilities)
      ii  debconf                           1.5.58ubuntu1         all                   Debian configuration management system
      ii  debconf-i18n                      1.5.58ubuntu1         all                   full internationalization support for debconf
      ii  debianutils                       4.7                   amd64                 Miscellaneous utilities specific to Debian
      ii  dh-python                         2.20151103ubuntu1.1   all                   Debian helper tools for packaging Python libraries and applications
      ii  diffutils                         1:3.3-3               amd64                 File comparison utilities
      ii  distro-info-data                  0.28ubuntu0.6         all                   information about the distributions' releases (data files)
      ii  dmeventd                          2:1.02.110-1ubuntu10  amd64                 Linux Kernel Device Mapper event daemon
      ii  dmidecode                         3.0-2ubuntu0.1        amd64                 SMBIOS/DMI table decoder
      ii  dmsetup                           2:1.02.110-1ubuntu10  amd64                 Linux Kernel Device Mapper userspace library
      ii  dns-root-data                     2015052300+h+1        all                   DNS root data including root zone and DNSSEC key
      ii  dnsmasq-base                      2.75-1ubuntu0.16.04.4 amd64                 Small caching DNS proxy and DHCP/TFTP server
      ii  dnsutils                          1:9.10.3.dfsg.P4-8ubu amd64                 Clients provided with BIND
      ii  docker-ce                         17.09.1~ce-0~ubuntu   amd64                 Docker: the open-source application container engine
      ii  dosfstools                        3.0.28-2ubuntu0.1     amd64                 utilities for making and checking MS-DOS FAT filesystems
      ii  dpkg                              1.18.4ubuntu1.3       amd64                 Debian package management system
      ii  e2fslibs:amd64                    1.42.13-1ubuntu1      amd64                 ext2/ext3/ext4 file system libraries
      ii  e2fsprogs                         1.42.13-1ubuntu1      amd64                 ext2/ext3/ext4 file system utilities
      ii  eatmydata                         105-3                 all                   Library and utilities designed to disable fsync and friends
      ii  ed                                1.10-2                amd64                 classic UNIX line editor
      ii  efibootmgr                        0.12-4                amd64                 Interact with the EFI Boot Manager
      ii  eject                             2.1.5+deb1+cvs2008110 amd64                 ejects CDs and operates CD-Changers under Linux
      ii  ethtool                           1:4.5-1               amd64                 display or change Ethernet device settings
      ii  file                              1:5.25-2ubuntu1       amd64                 Determines file type using "magic" numbers
      ii  findutils                         4.6.0+git+20160126-2  amd64                 utilities for finding files--find, xargs
      ii  fonts-ubuntu-font-family-console  1:0.83-0ubuntu2       all                   Ubuntu Font Family Linux console fonts, sans-serif monospace
      ii  friendly-recovery                 0.2.31                all                   Make recovery more user-friendly
      ii  ftp                               0.17-33               amd64                 classical file transfer client
      ii  fuse                              2.9.4-1ubuntu3.1      amd64                 Filesystem in Userspace
      ii  gawk                              1:4.1.3+dfsg-0.1      amd64                 GNU awk, a pattern scanning and processing language
      ii  gcc-5-base:amd64                  5.4.0-6ubuntu1~16.04. amd64                 GCC, the GNU Compiler Collection (base package)
      ii  gcc-6-base:amd64                  6.0.1-0ubuntu1        amd64                 GCC, the GNU Compiler Collection (base package)
      ii  gdisk                             1.0.1-1build1         amd64                 GPT fdisk text-mode partitioning tool
      ii  geoip-database                    20160408-1            all                   IP lookup command line tools that use the GeoIP library (country databas
      ii  gettext-base                      0.19.7-2ubuntu3       amd64                 GNU Internationalization utilities for the base system
      ii  gir1.2-glib-2.0:amd64             1.46.0-3ubuntu1       amd64                 Introspection data for GLib, GObject, Gio and GModule
      ii  git                               1:2.7.4-0ubuntu1.3    amd64                 fast, scalable, distributed revision control system
      ii  git-man                           1:2.7.4-0ubuntu1.3    all                   fast, scalable, distributed revision control system (manual pages)
      ii  gnupg                             1.4.20-1ubuntu3.1     amd64                 GNU privacy guard - a free PGP replacement
      ii  gpgv                              1.4.20-1ubuntu3.1     amd64                 GNU privacy guard - signature verification tool
      ii  grep                              2.25-1~16.04.1        amd64                 GNU grep, egrep and fgrep
      ii  groff-base                        1.22.3-7              amd64                 GNU troff text-formatting system (base system components)
      ii  grub-common                       2.02~beta2-36ubuntu3. amd64                 GRand Unified Bootloader (common files)
      ii  grub-efi-amd64                    2.02~beta2-36ubuntu3. amd64                 GRand Unified Bootloader, version 2 (EFI-AMD64 version)
      ii  grub-efi-amd64-bin                2.02~beta2-36ubuntu3. amd64                 GRand Unified Bootloader, version 2 (EFI-AMD64 binaries)
      ii  grub-efi-amd64-signed             1.66.15+2.02~beta2-36 amd64                 GRand Unified Bootloader, version 2 (EFI-AMD64 version, signed)
      ii  grub-legacy-ec2                   17.1-46-g7acc9e68-0ub all                   Handles update-grub for ec2 instances
      rc  grub-pc                           2.02~beta2-36ubuntu3. amd64                 GRand Unified Bootloader, version 2 (PC/BIOS version)
      ii  grub2-common                      2.02~beta2-36ubuntu3. amd64                 GRand Unified Bootloader (common files for version 2)
      ii  gzip                              1.6-4ubuntu1          amd64                 GNU compression utilities
      ii  hdparm                            9.48+ds-1             amd64                 tune hard disk parameters for high performance
      ii  hostname                          3.16ubuntu2           amd64                 utility to set/show the host name or domain name
      ii  ifenslave                         2.7ubuntu1            all                   configure network interfaces for parallel routing (bonding)
      ii  ifupdown                          0.8.10ubuntu1.2       amd64                 high level tools to configure network interfaces
      ii  info                              6.1.0.dfsg.1-5        amd64                 Standalone GNU Info documentation browser
      ii  init                              1.29ubuntu4           amd64                 System-V-like init utilities - metapackage
      ii  init-system-helpers               1.29ubuntu4           all                   helper tools for all init systems
      ii  initramfs-tools                   0.122ubuntu8.10       all                   generic modular initramfs generator (automation)
      ii  initramfs-tools-bin               0.122ubuntu8.10       amd64                 binaries used by initramfs-tools
      ii  initramfs-tools-core              0.122ubuntu8.10       all                   generic modular initramfs generator (core tools)
      ii  initscripts                       2.88dsf-59.3ubuntu2   amd64                 scripts for initializing and shutting down the system
      ii  insserv                           1.14.0-5ubuntu3       amd64                 boot sequence organizer using LSB init.d script dependency information
      ii  install-info                      6.1.0.dfsg.1-5        amd64                 Manage installed documentation in info format
      ii  iproute2                          4.3.0-1ubuntu3.16.04. amd64                 networking and traffic control tools
      ii  iptables                          1.6.0-2ubuntu3        amd64                 administration tools for packet filtering and NAT
      ii  iputils-ping                      3:20121221-5ubuntu2   amd64                 Tools to test the reachability of network hosts
      ii  iputils-tracepath                 3:20121221-5ubuntu2   amd64                 Tools to trace the network path to a remote host
      ii  irqbalance                        1.1.0-2ubuntu1        amd64                 Daemon to balance interrupts for SMP systems
      ii  isc-dhcp-client                   4.3.3-5ubuntu12.7     amd64                 DHCP client for automatically obtaining an IP address
      ii  isc-dhcp-common                   4.3.3-5ubuntu12.7     amd64                 common files used by all of the isc-dhcp packages
      ii  iso-codes                         3.65-1                all                   ISO language, territory, currency, script codes and their translations
      ii  iw                                3.17-1                amd64                 tool for configuring Linux wireless devices
      ii  jq                                1.5+dfsg-1            amd64                 lightweight and flexible command-line JSON processor
      ii  kbd                               1.15.5-1ubuntu5       amd64                 Linux console font and keytable utilities
      ii  keyboard-configuration            1.108ubuntu15.3       all                   system-wide keyboard preferences
      ii  klibc-utils                       2.0.4-8ubuntu1.16.04. amd64                 small utilities built with klibc for early boot
      ii  kmod                              22-1ubuntu5           amd64                 tools for managing Linux kernel modules
      ii  krb5-locales                      1.13.2+dfsg-5ubuntu2  all                   Internationalization support for MIT Kerberos
      ii  language-selector-common          0.165.4               all                   Language selector for Ubuntu
      ii  less                              481-2.1ubuntu0.2      amd64                 pager program similar to more
      ii  libaccountsservice0:amd64         0.6.40-2ubuntu11.3    amd64                 query and manipulate user account information - shared libraries
      ii  libacl1:amd64                     2.2.52-3              amd64                 Access control list shared library
      ii  libapparmor-perl                  2.10.95-0ubuntu2.7    amd64                 AppArmor library Perl bindings
      ii  libapparmor1:amd64                2.10.95-0ubuntu2.7    amd64                 changehat AppArmor library
      ii  libapt-inst2.0:amd64              1.2.24                amd64                 deb package format runtime library
      ii  libapt-pkg5.0:amd64               1.2.24                amd64                 package management runtime library
      ii  libasn1-8-heimdal:amd64           1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - ASN.1 library
      ii  libasprintf0v5:amd64              0.19.7-2ubuntu3       amd64                 GNU library to use fprintf and friends in C++
      ii  libatm1:amd64                     1:2.5.1-1.5           amd64                 shared library for ATM (Asynchronous Transfer Mode)
      ii  libattr1:amd64                    1:2.4.47-2            amd64                 Extended attribute shared library
      ii  libaudit-common                   1:2.4.5-1ubuntu2      all                   Dynamic library for security auditing - common files
      ii  libaudit1:amd64                   1:2.4.5-1ubuntu2      amd64                 Dynamic library for security auditing
      ii  libbind9-140:amd64                1:9.10.3.dfsg.P4-8ubu amd64                 BIND9 Shared Library used by BIND
      ii  libblkid1:amd64                   2.27.1-6ubuntu3.3     amd64                 block device ID library
      ii  libbsd0:amd64                     0.8.2-1               amd64                 utility functions from BSD systems - shared library
      ii  libbz2-1.0:amd64                  1.0.6-8               amd64                 high-quality block-sorting file compressor library - runtime
      ii  libc-ares2:amd64                  1.10.0-3ubuntu0.2     amd64                 asynchronous name resolver
      ii  libc-bin                          2.23-0ubuntu10        amd64                 GNU C Library: Binaries
      ii  libc6:amd64                       2.23-0ubuntu10        amd64                 GNU C Library: Shared libraries
      ii  libcap-ng0:amd64                  0.7.7-1               amd64                 An alternate POSIX capabilities library
      ii  libcap2:amd64                     1:2.24-12             amd64                 POSIX 1003.1e capabilities (library)
      ii  libcap2-bin                       1:2.24-12             amd64                 POSIX 1003.1e capabilities (utilities)
      ii  libcomerr2:amd64                  1.42.13-1ubuntu1      amd64                 common error description library
      ii  libcryptsetup4:amd64              2:1.6.6-5ubuntu2.1    amd64                 disk encryption support - shared library
      ii  libcurl3-gnutls:amd64             7.47.0-1ubuntu2.5     amd64                 easy-to-use client-side URL transfer library (GnuTLS flavour)
      ii  libdb5.3:amd64                    5.3.28-11ubuntu0.1    amd64                 Berkeley v5.3 Database Libraries [runtime]
      ii  libdbus-1-3:amd64                 1.10.6-1ubuntu3.3     amd64                 simple_parser interprocess messaging system (library)
      ii  libdbus-glib-1-2:amd64            0.106-1               amd64                 simple_parser interprocess messaging system (GLib-based shared library)
      ii  libdebconfclient0:amd64           0.198ubuntu1          amd64                 Debian Configuration Management System (C-implementation library)
      ii  libdevmapper-event1.02.1:amd64    2:1.02.110-1ubuntu10  amd64                 Linux Kernel Device Mapper event support library
      ii  libdevmapper1.02.1:amd64          2:1.02.110-1ubuntu10  amd64                 Linux Kernel Device Mapper userspace library
      ii  libdns-export162                  1:9.10.3.dfsg.P4-8ubu amd64                 Exported DNS Shared Library
      ii  libdns162:amd64                   1:9.10.3.dfsg.P4-8ubu amd64                 DNS Shared Library used by BIND
      ii  libdrm-common                     2.4.83-1~16.04.1      all                   Userspace interface to kernel DRM services -- common files
      ii  libdrm2:amd64                     2.4.83-1~16.04.1      amd64                 Userspace interface to kernel DRM services -- runtime
      ii  libdumbnet1:amd64                 1.12-7                amd64                 dumb, portable networking library -- shared library
      ii  libeatmydata1:amd64               105-3                 amd64                 Library and utilities to disable fsync and friends - shared library
      ii  libedit2:amd64                    3.1-20150325-1ubuntu2 amd64                 BSD editline and history libraries
      ii  libefivar0:amd64                  0.23-2                amd64                 Library to manage UEFI variables
      ii  libelf1:amd64                     0.165-3ubuntu1        amd64                 library to read and write ELF files
      ii  liberror-perl                     0.17-1.2              all                   Perl module for error/exception handling in an OO-ish way
      ii  libestr0                          0.1.10-1              amd64                 Helper functions for handling strings (lib)
      ii  libevent-2.0-5:amd64              2.0.21-stable-2ubuntu amd64                 Asynchronous event notification library
      ii  libexpat1:amd64                   2.1.0-7ubuntu0.16.04. amd64                 XML parsing C library - runtime library
      ii  libfdisk1:amd64                   2.27.1-6ubuntu3.3     amd64                 fdisk partitioning library
      ii  libffi6:amd64                     3.2.1-4               amd64                 Foreign Function Interface library runtime
      ii  libfreetype6:amd64                2.6.1-0.1ubuntu2.3    amd64                 FreeType 2 font engine, shared library files
      ii  libfribidi0:amd64                 0.19.7-1              amd64                 Free Implementation of the Unicode BiDi algorithm
      ii  libfuse2:amd64                    2.9.4-1ubuntu3.1      amd64                 Filesystem in Userspace (library)
      ii  libgcc1:amd64                     1:6.0.1-0ubuntu1      amd64                 GCC support library
      ii  libgcrypt20:amd64                 1.6.5-2ubuntu0.3      amd64                 LGPL Crypto library - runtime library
      ii  libgdbm3:amd64                    1.8.3-13.1            amd64                 GNU dbm database routines (runtime version)
      ii  libgeoip1:amd64                   1.6.9-1               amd64                 non-DNS IP-to-country resolver library
      ii  libgirepository-1.0-1:amd64       1.46.0-3ubuntu1       amd64                 Library for handling GObject introspection data (runtime library)
      ii  libglib2.0-0:amd64                2.48.2-0ubuntu1       amd64                 GLib library of C routines
      ii  libglib2.0-data                   2.48.2-0ubuntu1       all                   Common files for GLib library
      ii  libgmp10:amd64                    2:6.1.0+dfsg-2        amd64                 Multiprecision arithmetic library
      ii  libgnutls-openssl27:amd64         3.4.10-4ubuntu1.4     amd64                 GNU TLS library - OpenSSL wrapper
      ii  libgnutls30:amd64                 3.4.10-4ubuntu1.4     amd64                 GNU TLS library - main runtime library
      ii  libgpg-error0:amd64               1.21-2ubuntu1         amd64                 library for common error values and messages in GnuPG components
      ii  libgpm2:amd64                     1.20.4-6.1            amd64                 General Purpose Mouse - shared library
      ii  libgssapi-krb5-2:amd64            1.13.2+dfsg-5ubuntu2  amd64                 MIT Kerberos runtime libraries - krb5 GSS-API Mechanism
      ii  libgssapi3-heimdal:amd64          1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - GSSAPI support library
      ii  libhcrypto4-heimdal:amd64         1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - crypto library
      ii  libheimbase1-heimdal:amd64        1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - Base library
      ii  libheimntlm0-heimdal:amd64        1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - NTLM support library
      ii  libhogweed4:amd64                 3.2-1ubuntu0.16.04.1  amd64                 low level cryptographic library (public-key cryptos)
      ii  libhx509-5-heimdal:amd64          1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - X509 support library
      ii  libicu55:amd64                    55.1-7ubuntu0.3       amd64                 International Components for Unicode
      ii  libidn11:amd64                    1.32-3ubuntu1.2       amd64                 GNU Libidn library, implementation of IETF IDN specifications
      ii  libisc-export160                  1:9.10.3.dfsg.P4-8ubu amd64                 Exported ISC Shared Library
      ii  libisc160:amd64                   1:9.10.3.dfsg.P4-8ubu amd64                 ISC Shared Library used by BIND
      ii  libisccc140:amd64                 1:9.10.3.dfsg.P4-8ubu amd64                 Command Channel Library used by BIND
      ii  libisccfg140:amd64                1:9.10.3.dfsg.P4-8ubu amd64                 Config File Handling Library used by BIND
      ii  libjson-c2:amd64                  0.11-4ubuntu2         amd64                 JSON manipulation library - shared library
      ii  libk5crypto3:amd64                1.13.2+dfsg-5ubuntu2  amd64                 MIT Kerberos runtime libraries - Crypto Library
      ii  libkeyutils1:amd64                1.5.9-8ubuntu1        amd64                 Linux Key Management Utilities (library)
      ii  libklibc                          2.0.4-8ubuntu1.16.04. amd64                 minimal libc subset for use with initramfs
      ii  libkmod2:amd64                    22-1ubuntu5           amd64                 libkmod shared library
      ii  libkrb5-26-heimdal:amd64          1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - libraries
      ii  libkrb5-3:amd64                   1.13.2+dfsg-5ubuntu2  amd64                 MIT Kerberos runtime libraries
      ii  libkrb5support0:amd64             1.13.2+dfsg-5ubuntu2  amd64                 MIT Kerberos runtime libraries - Support library
      ii  libldap-2.4-2:amd64               2.4.42+dfsg-2ubuntu3. amd64                 OpenLDAP libraries
      ii  liblocale-gettext-perl            1.07-1build1          amd64                 module using libc functions for internationalization in Perl
      ii  libltdl7:amd64                    2.4.6-0.1             amd64                 System independent dlopen wrapper for GNU libtool
      ii  liblvm2app2.2:amd64               2.02.133-1ubuntu10    amd64                 LVM2 application library
      ii  liblvm2cmd2.02:amd64              2.02.133-1ubuntu10    amd64                 LVM2 command library
      ii  liblwres141:amd64                 1:9.10.3.dfsg.P4-8ubu amd64                 Lightweight Resolver Library used by BIND
      ii  liblxc1                           2.0.8-0ubuntu1~16.04. amd64                 Linux Containers userspace tools (library)
      ii  liblz4-1:amd64                    0.0~r131-2ubuntu2     amd64                 Fast LZ compression algorithm library - runtime
      ii  liblzma5:amd64                    5.1.1alpha+20120614-2 amd64                 XZ-format compression library
      ii  liblzo2-2:amd64                   2.08-1.2              amd64                 data compression library
      ii  libmagic1:amd64                   1:5.25-2ubuntu1       amd64                 File type determination library using "magic" numbers
      ii  libmnl0:amd64                     1.0.3-5               amd64                 minimalistic Netlink communication library
      ii  libmount1:amd64                   2.27.1-6ubuntu3.3     amd64                 device mounting library
      ii  libmpdec2:amd64                   2.4.2-1               amd64                 library for decimal floating point arithmetic (runtime library)
      ii  libmpfr4:amd64                    3.1.4-1               amd64                 multiple precision floating-point computation
      ii  libmspack0:amd64                  0.5-1ubuntu0.16.04.1  amd64                 library for Microsoft compression formats (shared library)
      ii  libncurses5:amd64                 6.0+20160213-1ubuntu1 amd64                 shared libraries for terminal handling
      ii  libncursesw5:amd64                6.0+20160213-1ubuntu1 amd64                 shared libraries for terminal handling (wide character support)
      ii  libnetfilter-conntrack3:amd64     1.0.5-1               amd64                 Netfilter netlink-conntrack library
      ii  libnettle6:amd64                  3.2-1ubuntu0.16.04.1  amd64                 low level cryptographic library (symmetric and one-way cryptos)
      ii  libnewt0.52:amd64                 0.52.18-1ubuntu2      amd64                 Not Erik's Windowing Toolkit - text mode windowing with slang
      ii  libnfnetlink0:amd64               1.0.1-3               amd64                 Netfilter netlink library
      ii  libnih1:amd64                     1.0.3-4.3ubuntu1      amd64                 NIH Utility Library
      ii  libnl-3-200:amd64                 3.2.27-1ubuntu0.16.04 amd64                 library for dealing with netlink sockets
      ii  libnl-genl-3-200:amd64            3.2.27-1ubuntu0.16.04 amd64                 library for dealing with netlink sockets - generic netlink
      ii  libnuma1:amd64                    2.0.11-1ubuntu1       amd64                 Libraries for controlling NUMA policy
      ii  libonig2:amd64                    5.9.6-1               amd64                 regular expressions library
      ii  libp11-kit0:amd64                 0.23.2-5~ubuntu16.04. amd64                 library for loading and coordinating access to PKCS#11 modules - runtime
      ii  libpam-modules:amd64              1.1.8-3.2ubuntu2      amd64                 Pluggable Authentication Modules for PAM
      ii  libpam-modules-bin                1.1.8-3.2ubuntu2      amd64                 Pluggable Authentication Modules for PAM - helper binaries
      ii  libpam-runtime                    1.1.8-3.2ubuntu2      all                   Runtime support for the PAM library
      ii  libpam-systemd:amd64              229-4ubuntu21         amd64                 system and service manager - PAM module
      ii  libpam0g:amd64                    1.1.8-3.2ubuntu2      amd64                 Pluggable Authentication Modules library
      ii  libparted2:amd64                  3.2-15                amd64                 disk partition manipulator - shared library
      ii  libpcap0.8:amd64                  1.7.4-2               amd64                 system interface for user-level packet capture
      ii  libpci3:amd64                     1:3.3.1-1.1ubuntu1.1  amd64                 Linux PCI Utilities (shared library)
      ii  libpcre3:amd64                    2:8.38-3.1            amd64                 Perl 5 Compatible Regular Expression Library - runtime files
      ii  libperl5.22:amd64                 5.22.1-9ubuntu0.2     amd64                 shared Perl library
      ii  libpipeline1:amd64                1.4.1-2               amd64                 pipeline manipulation library
      ii  libplymouth4:amd64                0.9.2-3ubuntu13.2     amd64                 graphical boot animation and logger - shared libraries
      ii  libpng12-0:amd64                  1.2.54-1ubuntu1       amd64                 PNG library - runtime
      ii  libpolkit-agent-1-0:amd64         0.105-14.1            amd64                 PolicyKit Authentication Agent API
      ii  libpolkit-backend-1-0:amd64       0.105-14.1            amd64                 PolicyKit backend API
      ii  libpolkit-gobject-1-0:amd64       0.105-14.1            amd64                 PolicyKit Authorization API
      ii  libpopt0:amd64                    1.16-10               amd64                 lib for parsing cmdline parameters
      ii  libprocps4:amd64                  2:3.3.10-4ubuntu2.3   amd64                 library for accessing process information from /proc
      ii  libpython3-stdlib:amd64           3.5.1-3               amd64                 interactive high-level object-oriented language (default python3 version
      ii  libpython3.5:amd64                3.5.2-2ubuntu0~16.04. amd64                 Shared Python runtime library (version 3.5)
      ii  libpython3.5-minimal:amd64        3.5.2-2ubuntu0~16.04. amd64                 Minimal subset of the Python language (version 3.5)
      ii  libpython3.5-stdlib:amd64         3.5.2-2ubuntu0~16.04. amd64                 Interactive high-level object-oriented language (standard library, versi
      ii  libreadline5:amd64                5.2+dfsg-3build1      amd64                 GNU readline and history libraries, run-time libraries
      ii  libreadline6:amd64                6.3-8ubuntu2          amd64                 GNU readline and history libraries, run-time libraries
      ii  libroken18-heimdal:amd64          1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - roken support library
      ii  librtmp1:amd64                    2.4+20151223.gitfa864 amd64                 toolkit for RTMP streams (shared library)
      ii  libsasl2-2:amd64                  2.1.26.dfsg1-14build1 amd64                 Cyrus SASL - authentication abstraction library
      ii  libsasl2-modules:amd64            2.1.26.dfsg1-14build1 amd64                 Cyrus SASL - pluggable authentication modules
      ii  libsasl2-modules-db:amd64         2.1.26.dfsg1-14build1 amd64                 Cyrus SASL - pluggable authentication modules (DB)
      ii  libseccomp2:amd64                 2.3.1-2.1ubuntu2~16.0 amd64                 high level interface to Linux seccomp filter
      ii  libselinux1:amd64                 2.4-3build2           amd64                 SELinux runtime shared libraries
      ii  libsemanage-common                2.3-1build3           all                   Common files for SELinux policy management libraries
      ii  libsemanage1:amd64                2.3-1build3           amd64                 SELinux policy management library
      ii  libsepol1:amd64                   2.4-2                 amd64                 SELinux library for manipulating binary security policies
      ii  libsigsegv2:amd64                 2.10-4                amd64                 Library for handling page faults in a portable way
      ii  libslang2:amd64                   2.3.0-2ubuntu1        amd64                 S-Lang programming library - runtime version
      ii  libsmartcols1:amd64               2.27.1-6ubuntu3.3     amd64                 smart column output alignment library
      ii  libsqlite3-0:amd64                3.11.0-1ubuntu1       amd64                 SQLite 3 shared library
      ii  libss2:amd64                      1.42.13-1ubuntu1      amd64                 command-line interface parsing library
      ii  libssh2-1:amd64                   1.5.0-2ubuntu0.1      amd64                 SSH2 client-side library
      ii  libssl1.0.0:amd64                 1.0.2g-1ubuntu4.10    amd64                 Secure Sockets Layer toolkit - shared libraries
      ii  libstdc++6:amd64                  5.4.0-6ubuntu1~16.04. amd64                 GNU Standard C++ Library v3
      ii  libsystemd0:amd64                 229-4ubuntu21         amd64                 systemd utility library
      ii  libtasn1-6:amd64                  4.7-3ubuntu0.16.04.3  amd64                 Manage ASN.1 structures (runtime)
      ii  libtext-charwidth-perl            0.04-7build5          amd64                 get display widths of characters on the terminal
      ii  libtext-iconv-perl                1.7-5build4           amd64                 converts between character sets in Perl
      ii  libtext-wrapi18n-perl             0.06-7.1              all                   internationalized substitute of Text::Wrap
      ii  libtinfo5:amd64                   6.0+20160213-1ubuntu1 amd64                 shared low-level terminfo library for terminal handling
      ii  libudev1:amd64                    229-4ubuntu21         amd64                 libudev shared library
      ii  libusb-0.1-4:amd64                2:0.1.12-28           amd64                 userspace USB programming library
      ii  libusb-1.0-0:amd64                2:1.0.20-1            amd64                 userspace USB programming library
      ii  libustr-1.0-1:amd64               1.0.4-5               amd64                 Micro string library: shared library
      ii  libutempter0:amd64                1.1.6-3               amd64                 privileged helper for utmp/wtmp updates (runtime)
      ii  libuuid1:amd64                    2.27.1-6ubuntu3.3     amd64                 Universally Unique ID library
      ii  libwind0-heimdal:amd64            1.7~git20150920+dfsg- amd64                 Heimdal Kerberos - stringprep implementation
      ii  libwrap0:amd64                    7.6.q-25              amd64                 Wietse Venema's TCP wrappers library
      ii  libx11-6:amd64                    2:1.6.3-1ubuntu2      amd64                 X11 client-side library
      ii  libx11-data                       2:1.6.3-1ubuntu2      all                   X11 client-side library
      ii  libxau6:amd64                     1:1.0.8-1             amd64                 X11 authorisation library
      ii  libxcb1:amd64                     1.11.1-1ubuntu1       amd64                 X C Binding
      ii  libxdmcp6:amd64                   1:1.1.2-1.1           amd64                 X11 Display Manager Control Protocol library
      ii  libxext6:amd64                    2:1.3.3-1             amd64                 X11 miscellaneous extension library
      ii  libxml2:amd64                     2.9.3+dfsg1-1ubuntu0. amd64                 GNOME XML library
      ii  libxmuu1:amd64                    2:1.1.2-2             amd64                 X11 miscellaneous micro-utility library
      ii  libxtables11:amd64                1.6.0-2ubuntu3        amd64                 netfilter xtables library
      ii  libyaml-0-2:amd64                 0.1.6-3               amd64                 Fast YAML 1.1 parser and emitter library
      ii  linux-base                        4.0ubuntu1            all                   Linux image base package
      ii  linux-firmware                    1.157.14              all                   Firmware for Linux kernel drivers
      ii  linux-headers-4.4.0-109           4.4.0-109.132         all                   Header files related to Linux kernel version 4.4.0
      ii  linux-headers-4.4.0-109-generic   4.4.0-109.132         amd64                 Linux kernel headers for version 4.4.0 on 64 bit x86 SMP
      ii  linux-headers-4.4.0-112           4.4.0-112.135         all                   Header files related to Linux kernel version 4.4.0
      ii  linux-headers-4.4.0-112-generic   4.4.0-112.135         amd64                 Linux kernel headers for version 4.4.0 on 64 bit x86 SMP
      ii  linux-headers-generic             4.4.0.112.118         amd64                 Generic Linux kernel headers
      ii  linux-headers-virtual             4.4.0.112.118         amd64                 Transitional package.
      ii  linux-image-4.4.0-109-generic     4.4.0-109.132         amd64                 Linux kernel image for version 4.4.0 on 64 bit x86 SMP
      ii  linux-image-4.4.0-112-generic     4.4.0-112.135         amd64                 Linux kernel image for version 4.4.0 on 64 bit x86 SMP
      ii  linux-image-extra-4.4.0-109-gener 4.4.0-109.132         amd64                 Linux kernel extra modules for version 4.4.0 on 64 bit x86 SMP
      ii  linux-image-extra-4.4.0-112-gener 4.4.0-112.135         amd64                 Linux kernel extra modules for version 4.4.0 on 64 bit x86 SMP
      ii  linux-image-extra-virtual         4.4.0.112.118         amd64                 Transitional package.
      ii  linux-image-generic               4.4.0.112.118         amd64                 Generic Linux kernel image
      ii  linux-image-virtual               4.4.0.112.118         amd64                 This package will always depend on the latest minimal generic kernel ima
      ii  linux-virtual                     4.4.0.112.118         amd64                 Minimal Generic Linux kernel and headers
      ii  locales                           2.23-0ubuntu10        all                   GNU C Library: National Language (locale) data [support]
      ii  login                             1:4.2-3.1ubuntu5.3    amd64                 system login tools
      ii  logrotate                         3.8.7-2ubuntu2.16.04. amd64                 Log rotation utility
      ii  lsb-base                          9.20160110ubuntu0.2   all                   Linux Standard Base init script functionality
      ii  lsb-release                       9.20160110ubuntu0.2   all                   Linux Standard Base version reporting utility
      ii  lshw                              02.17-1.1ubuntu3.4    amd64                 information about hardware configuration
      ii  lsof                              4.89+dfsg-0.1         amd64                 Utility to list open files
      ii  ltrace                            0.7.3-5.1ubuntu4      amd64                 Tracks runtime library calls in dynamically linked programs
      ii  lvm2                              2.02.133-1ubuntu10    amd64                 Linux Logical Volume Manager
      ii  lxc-common                        2.0.8-0ubuntu1~16.04. amd64                 Linux Containers userspace tools (common tools)
      ii  lxcfs                             2.0.8-0ubuntu1~16.04. amd64                 FUSE based filesystem for LXC
      ii  lxd                               2.0.11-0ubuntu1~16.04 amd64                 Container hypervisor based on LXC - daemon
      ii  lxd-client                        2.0.11-0ubuntu1~16.04 amd64                 Container hypervisor based on LXC - client
      ii  makedev                           2.3.1-93ubuntu2~ubunt all                   creates device files in /dev
      ii  man-db                            2.7.5-1               amd64                 on-line manual pager
      ii  manpages                          4.04-2                all                   Manual pages about using a GNU/Linux system
      ii  mawk                              1.3.3-17ubuntu2       amd64                 a pattern scanning and text processing language
      ii  mdadm                             3.3-2ubuntu7.6        amd64                 tool to administer Linux MD arrays (software RAID)
      ii  mime-support                      3.59ubuntu1           all                   MIME files 'mime.types' & 'mailcap', and support programs
      ii  mlocate                           0.26-1ubuntu2         amd64                 quickly find files on the filesystem based on their name
      ii  mokutil                           0.3.0-0ubuntu3        amd64                 tools for manipulating machine owner keys
      ii  mount                             2.27.1-6ubuntu3.3     amd64                 tools for mounting and manipulating filesystems
      ii  mtr-tiny                          0.86-1ubuntu0.1       amd64                 Full screen ncurses traceroute tool
      ii  multiarch-support                 2.23-0ubuntu10        amd64                 Transitional package to ensure multiarch compatibility
      ii  nano                              2.5.3-2ubuntu2        amd64                 small, friendly text editor inspired by Pico
      ii  ncurses-base                      6.0+20160213-1ubuntu1 all                   basic terminal type definitions
      ii  ncurses-bin                       6.0+20160213-1ubuntu1 amd64                 terminal-related programs and man pages
      ii  ncurses-term                      6.0+20160213-1ubuntu1 all                   additional terminal type definitions
      ii  net-tools                         1.60-26ubuntu1        amd64                 NET-3 networking toolkit
      ii  netbase                           5.3                   all                   Basic TCP/IP networking system
      ii  netcat-openbsd                    1.105-7ubuntu1        amd64                 TCP/IP swiss army knife
      ii  ntfs-3g                           1:2015.3.14AR.1-1ubun amd64                 read/write NTFS driver for FUSE
      ii  open-iscsi                        2.0.873+git0.3b4b4500 amd64                 iSCSI initiator tools
      ii  open-vm-tools                     2:10.0.7-3227872-5ubu amd64                 Open VMware Tools for virtual machines hosted on VMware (CLI)
      ii  openssh-client                    1:7.2p2-4ubuntu2.4    amd64                 secure shell (SSH) client, for secure access to remote machines
      ii  openssh-server                    1:7.2p2-4ubuntu2.4    amd64                 secure shell (SSH) server, for secure access from remote machines
      ii  openssh-sftp-server               1:7.2p2-4ubuntu2.4    amd64                 secure shell (SSH) sftp server module, for SFTP access from remote machi
      ii  openssl                           1.0.2g-1ubuntu4.10    amd64                 Secure Sockets Layer toolkit - cryptographic utility
      ii  os-prober                         1.70ubuntu3.3         amd64                 utility to detect other OSes on a set of drives
      ii  overlayroot                       0.27ubuntu1.4         all                   use an overlayfs on top of a read-only root filesystem
      ii  parted                            3.2-15                amd64                 disk partition manipulator
      ii  passwd                            1:4.2-3.1ubuntu5.3    amd64                 change and administer password and group data
      ii  pastebinit                        1.5-1                 all                   command-line pastebin client
      ii  patch                             2.7.5-1               amd64                 Apply a diff file to an original
      ii  pciutils                          1:3.3.1-1.1ubuntu1.1  amd64                 Linux PCI Utilities
      ii  perl                              5.22.1-9ubuntu0.2     amd64                 Larry Wall's Practical Extraction and Report Language
      ii  perl-base                         5.22.1-9ubuntu0.2     amd64                 minimal Perl system
      ii  perl-modules-5.22                 5.22.1-9ubuntu0.2     all                   Core Perl modules
      ii  plymouth                          0.9.2-3ubuntu13.2     amd64                 boot animation, logger and I/O multiplexer
      ii  plymouth-theme-ubuntu-text        0.9.2-3ubuntu13.2     amd64                 boot animation, logger and I/O multiplexer - ubuntu text theme
      ii  policykit-1                       0.105-14.1            amd64                 framework for managing administrative policies and privileges
      ii  pollinate                         4.25-0ubuntu1~16.04.1 all                   seed the pseudo random number generator
      ii  popularity-contest                1.64ubuntu2           all                   Vote for your favourite packages automatically
      ii  powermgmt-base                    1.31+nmu1             all                   Common utils and configs for power management
      ii  procps                            2:3.3.10-4ubuntu2.3   amd64                 /proc file system utilities
      ii  psmisc                            22.21-2.1build1       amd64                 utilities that use the proc file system
      ii  python-apt-common                 1.1.0~beta1build1     all                   Python interface to libapt-pkg (locales)
      ii  python3                           3.5.1-3               amd64                 interactive high-level object-oriented language (default python3 version
      ii  python3-apport                    2.20.1-0ubuntu2.15    all                   Python 3 library for Apport crash report handling
      ii  python3-apt                       1.1.0~beta1build1     amd64                 Python 3 interface to libapt-pkg
      ii  python3-blinker                   1.3.dfsg2-1build1     all                   fast, simple_parser object-to-object and broadcast signaling library
      ii  python3-cffi-backend              1.5.2-1ubuntu1        amd64                 Foreign Function Interface for Python 3 calling C code - runtime
      ii  python3-chardet                   2.3.0-2               all                   universal character encoding detector for Python3
      ii  python3-commandnotfound           0.3ubuntu16.04.2      all                   Python 3 bindings for command-not-found.
      ii  python3-configobj                 5.0.6-2               all                   simple_parser but powerful config file reader and writer for Python 3
      ii  python3-cryptography              1.2.3-1ubuntu0.1      amd64                 Python library exposing cryptographic recipes and primitives (Python 3)
      ii  python3-dbus                      1.2.0-3               amd64                 simple_parser interprocess messaging system (Python 3 interface)
      ii  python3-debian                    0.1.27ubuntu2         all                   Python 3 modules to work with Debian-related data formats
      ii  python3-distupgrade               1:16.04.23            all                   manage release upgrades
      ii  python3-gdbm:amd64                3.5.1-1               amd64                 GNU dbm database support for Python 3.x
      ii  python3-gi                        3.20.0-0ubuntu1       amd64                 Python 3 bindings for gobject-introspection libraries
      ii  python3-idna                      2.0-3                 all                   Python IDNA2008 (RFC 5891) handling (Python 3)
      ii  python3-jinja2                    2.8-1                 all                   small but fast and easy to use stand-alone template engine
      ii  python3-json-pointer              1.9-3                 all                   resolve JSON pointers - Python 3.x
      ii  python3-jsonpatch                 1.19-3                all                   library to apply JSON patches - Python 3.x
      ii  python3-jwt                       1.3.0-1ubuntu0.1      all                   Python 3 implementation of JSON Web Token
      ii  python3-markupsafe                0.23-2build2          amd64                 HTML/XHTML/XML string library for Python 3
      ii  python3-minimal                   3.5.1-3               amd64                 minimal subset of the Python language (default python3 version)
      ii  python3-newt                      0.52.18-1ubuntu2      amd64                 NEWT module for Python3
      ii  python3-oauthlib                  1.0.3-1               all                   generic, spec-compliant implementation of OAuth for Python3
      ii  python3-pkg-resources             20.7.0-1              all                   Package Discovery and Resource Access using pkg_resources
      ii  python3-prettytable               0.7.2-3               all                   library to represent tabular data in visually appealing ASCII tables (Py
      ii  python3-problem-report            2.20.1-0ubuntu2.15    all                   Python 3 library to handle problem reports
      ii  python3-pyasn1                    0.1.9-1               all                   ASN.1 library for Python (Python 3 module)
      ii  python3-pycurl                    7.43.0-1ubuntu1       amd64                 Python bindings to libcurl (Python 3)
      ii  python3-requests                  2.9.1-3               all                   elegant and simple_parser HTTP library for Python3, built for human beings
      ii  python3-serial                    3.0.1-1               all                   pyserial - module encapsulating access for the serial port
      ii  python3-six                       1.10.0-3              all                   Python 2 and 3 compatibility library (Python 3 interface)
      ii  python3-software-properties       0.96.20.7             all                   manage the repositories that you install software from
      ii  python3-systemd                   231-2build1           amd64                 Python 3 bindings for systemd
      ii  python3-update-manager            1:16.04.10            all                   python 3.x module for update-manager
      ii  python3-urllib3                   1.13.1-2ubuntu0.16.04 all                   HTTP library with thread-safe connection pooling for Python3
      ii  python3-yaml                      3.11-3build1          amd64                 YAML parser and emitter for Python3
      ii  python3.5                         3.5.2-2ubuntu0~16.04. amd64                 Interactive high-level object-oriented language (version 3.5)
      ii  python3.5-minimal                 3.5.2-2ubuntu0~16.04. amd64                 Minimal subset of the Python language (version 3.5)
      ii  readline-common                   6.3-8ubuntu2          all                   GNU readline and history libraries, common files
      ii  rename                            0.20-4                all                   Perl extension for renaming multiple files
      ii  resolvconf                        1.78ubuntu5           all                   name server information handler
      ii  rsync                             3.1.1-3ubuntu1.2      amd64                 fast, versatile, remote (and local) file-copying tool
      ii  rsyslog                           8.16.0-1ubuntu3       amd64                 reliable system and kernel logging daemon
      ii  run-one                           1.17-0ubuntu1         all                   run just one instance of a command and its args at a time
      ii  sbsigntool                        0.6-0ubuntu10.1       amd64                 utility for signing and verifying files for UEFI Secure Boot
      ii  screen                            4.3.1-2build1         amd64                 terminal multiplexer with VT100/ANSI terminal emulation
      ii  secureboot-db                     1.1                   amd64                 Secure Boot updates for DB and DBX
      ii  sed                               4.2.2-7               amd64                 The GNU sed stream editor
      ii  sensible-utils                    0.0.9                 all                   Utilities for sensible alternative selection
      ii  sgml-base                         1.26+nmu4ubuntu1      all                   SGML infrastructure and SGML catalog file support
      ii  shared-mime-info                  1.5-2ubuntu0.1        amd64                 FreeDesktop.org shared MIME database and spec
      ii  shim                              0.9+1474479173.6c180c amd64                 boot loader to chain-load signed boot loaders under Secure Boot
      ii  shim-signed                       1.32~16.04.1+0.9+1474 amd64                 Secure Boot chain-loading bootloader (Microsoft-signed binary)
      ii  snapd                             2.29.4.2              amd64                 Daemon and tooling that enable snap packages
      ii  software-properties-common        0.96.20.7             all                   manage the repositories that you install software from (common)
      ii  sosreport                         3.4-1~ubuntu16.04.1   amd64                 Set of tools to gather troubleshooting data from a system
      ii  squashfs-tools                    1:4.3-3ubuntu2.16.04. amd64                 Tool to create and append to squashfs filesystems
      ii  ssh-import-id                     5.5-0ubuntu1          all                   securely retrieve an SSH public key and install it locally
      ii  strace                            4.11-1ubuntu3         amd64                 System call tracer
      ii  sudo                              1.8.16-0ubuntu1.5     amd64                 Provide limited super user privileges to specific users
      ii  systemd                           229-4ubuntu21         amd64                 system and service manager
      ii  systemd-sysv                      229-4ubuntu21         amd64                 system and service manager - SysV links
      ii  sysv-rc                           2.88dsf-59.3ubuntu2   all                   System-V-like runlevel change mechanism
      ii  sysvinit-utils                    2.88dsf-59.3ubuntu2   amd64                 System-V-like utilities
      ii  tar                               1.28-2.1ubuntu0.1     amd64                 GNU version of the tar archiving utility
      ii  tcpd                              7.6.q-25              amd64                 Wietse Venema's TCP wrapper utilities
      ii  tcpdump                           4.9.2-0ubuntu0.16.04. amd64                 command-line network traffic analyzer
      ii  telnet                            0.17-40               amd64                 basic telnet client
      ii  thermald                          1.5-2ubuntu4          amd64                 Thermal monitoring and controlling daemon
      ii  time                              1.7-25.1              amd64                 GNU time program for measuring CPU resource usage
      ii  tmux                              2.1-3build1           amd64                 terminal multiplexer
      ii  tzdata                            2017c-0ubuntu0.16.04  all                   time zone and daylight-saving time data
      ii  ubuntu-cloudimage-keyring         2013.11.11            all                   GnuPG keys of the Ubuntu Cloud Image builder
      ii  ubuntu-core-launcher              2.29.4.2              amd64                 Transitional package for snapd
      ii  ubuntu-keyring                    2012.05.19            all                   GnuPG keys of the Ubuntu archive
      ii  ubuntu-minimal                    1.361.1               amd64                 Minimal core of Ubuntu
      ii  ubuntu-release-upgrader-core      1:16.04.23            all                   manage release upgrades
      ii  ubuntu-server                     1.361.1               amd64                 The Ubuntu Server system
      ii  ubuntu-standard                   1.361.1               amd64                 The Ubuntu standard system
      ii  ucf                               3.0036                all                   Update Configuration File(s): preserve user changes to config files
      ii  udev                              229-4ubuntu21         amd64                 /dev/ and hotplug management daemon
      ii  ufw                               0.35-0ubuntu2         all                   program for managing a Netfilter firewall
      ii  uidmap                            1:4.2-3.1ubuntu5.3    amd64                 programs to help use subuids
      ii  unattended-upgrades               0.90ubuntu0.9         all                   automatic installation of security upgrades
      ii  update-manager-core               1:16.04.10            all                   manage release upgrades
      ii  update-notifier-common            3.168.7               all                   Files shared between update-notifier and other packages
      ii  ureadahead                        0.100.0-19            amd64                 Read required files in advance
      ii  usbutils                          1:007-4               amd64                 Linux USB utilities
      ii  util-linux                        2.27.1-6ubuntu3.3     amd64                 miscellaneous system utilities
      ii  uuid-runtime                      2.27.1-6ubuntu3.3     amd64                 runtime components for the Universally Unique ID library
      ii  vim                               2:7.4.1689-3ubuntu1.2 amd64                 Vi IMproved - enhanced vi editor
      ii  vim-common                        2:7.4.1689-3ubuntu1.2 amd64                 Vi IMproved - Common files
      ii  vim-runtime                       2:7.4.1689-3ubuntu1.2 all                   Vi IMproved - Runtime files
      ii  vim-tiny                          2:7.4.1689-3ubuntu1.2 amd64                 Vi IMproved - enhanced vi editor - compact version
      ii  vlan                              1.9-3.2ubuntu1.16.04. amd64                 user mode programs to enable VLANs on your ethernet devices
      ii  wget                              1.17.1-1ubuntu1.3     amd64                 retrieves files from the web
      ii  whiptail                          0.52.18-1ubuntu2      amd64                 Displays user-friendly dialog boxes from shell scripts
      ii  wireless-regdb                    2015.07.20-1ubuntu1   all                   wireless regulatory database
      ii  xauth                             1:1.0.9-1ubuntu2      amd64                 X authentication utility
      ii  xdg-user-dirs                     0.15-2ubuntu6         amd64                 tool to manage well known user directories
      ii  xfsprogs                          4.3.0+nmu1ubuntu1.1   amd64                 Utilities for managing the XFS filesystem
      ii  xkb-data                          2.16-1ubuntu1         all                   X Keyboard Extension (XKB) configuration data
      ii  xml-core                          0.13+nmu2             all                   XML infrastructure and XML catalog file support
      ii  xz-utils                          5.1.1alpha+20120614-2 amd64                 XZ-format compression utilities
      ii  zerofree                          1.0.3-1               amd64                 zero free blocks from ext2, ext3 and ext4 file-systems
      ii  zlib1g:amd64                      1:1.2.8.dfsg-2ubuntu4 amd64                 compression library - runtime
      """

    When I execute Patton search with type "pkg_ubuntu2"
    Then I get at least these vulnerabilities
      | Library Name           | Library Version         | CVE ID                |
      | libpython3.5:amd64     | 3.5.2-2ubuntu0~16.04.   | CVE-2019-5736         |
      | python3-jinja2         | 2.8-1                   | CVE-2016-10745        |
      | bind9-host             | 1:9.10.3.dfsg.P4-8ubu   | CVE-2018-5741         |
      | docker-ce              | 17.09.1~ce-0~ubuntu     | CVE-2017-14992        |

    And Not found these false positives
      | Library Name           | Library Version         | CVE ID                |
      | python3-cryptography   | 1.2.3-1ubuntu0.1        | CVE-2019-5736         |
      | python3-jwt            | 1.3.0-1ubuntu0.1        | CVE-2017-11424         |
