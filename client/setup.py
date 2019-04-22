from os import path, environ
from os.path import join, abspath, dirname
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    readme = f.read()

with open(join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(join(abspath(dirname(__file__)), "VERSION"), "r") as v:
    VERSION = v.read().replace("\n", "")

with open(join(abspath(dirname(__file__)), "PATCH"), "r") as v:
    PATCH = v.read().replace("\n", "")

setup(
    name='patton-cli',
    version=f"{VERSION}.{PATCH}",
    packages=find_packages(),
    long_description=readme,
    install_requires=required,
    url='https://github.com/bbva/patton-cli',
    license='MIT',
    author='BBVA Labs',
    description='CLI for Patton-Server: The vulnerability knowledge store',
    entry_points={'console_scripts': [
        'patton = patton_client.cli:main',
    ]},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
    ],
)

