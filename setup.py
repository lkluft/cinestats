# -*- coding: utf-8 -*-
import sys
from distutils.core import setup
from os.path import dirname, join
from setuptools import find_packages


if not sys.version_info >= (3, 5, 1):
    sys.exit('Only support Python version >=3.5.1.\n'
             'Found version is {}'.format(sys.version))

# Parse version information from plain ASCII file.
versionfile = join(dirname(__file__), 'cinestats', 'VERSION')
__version__ = open(versionfile).read().strip()

setup(
    name='cinestats',
    author='Lukas Kluft',
    author_email='lukas.kluft@gmail.com',
    url='https://github.com/lkluft/cinestats',
    version=__version__,
    packages=find_packages(),
    license='GPL-3.0',
    description='Analyse and visualise statistics around movies and cinema.',
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: End User/Desktop',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    install_requires=[
        'matplotlib',
        'numpy',
        'nose',
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'flake8',
        'pytest',
    ],
)
