#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rzcheasygui


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

packages = [
    'instrpyvisa',
]

package_data = {
}

requires = [
]

classifiers = []

setup(
    name='instrpyvisa',
    version=rzcheasygui.__version__,
    description='Skeleton package for Python modules.',
    long_description=readme,
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    author=rzcheasygui.__author__,
    author_email='',
    url='',
    license='MIT',
    classifiers=classifiers,
)
