#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pipenv.utils import convert_deps_to_pip
from pipenv.project import Project

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    readme = f.read()

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name='patton',
    version='0.0.1',
    entry_points={
        'console_scripts': ['patton=patton.command_line:main'],
    },
    author='BBVA',
    description=readme,
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    keywords='patton',
    classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
