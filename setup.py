#! /usr/bin/env python
from __future__ import print_function, division

from setuptools import setup, find_packages

VERSION = '0.1'

DISTNAME = 'AKL-Test'
DESCRIPTION = 'Prime Test'
LONG_DESCRIPTION = open('README.md').read()
MAINTAINER = 'Jim Holmstrom'
MAINTAINER_EMAIL = 'jim.holmstroem@gmail.com'
URL = 'http://jim.pm'
LICENSE = open('LICENSE').read()
DOWNLOAD_URL = 'https://github.com/Jim-Holmstroem/{distname}.git'.format(distname=DISTNAME)

setup(
    name=DISTNAME,
    packages=find_packages(),
    include_package_data=True,
    version=VERSION,
    zip_safe=False,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    install_requires=[
	'sympy>=0.7.1',
    ],
    download_url=DOWNLOAD_URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Mathematics',
        'Operating System :: Unix',
        'Operating System :: MacOS'
    ],
)
