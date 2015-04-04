#!/usr/bin/env python

import argparse
import os
from os import path


DATA_TESTS = """
from nose.tools import *
import NAME

def setup():
    print "SETUP"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

"""

DATA_SETUP = """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Enter some useful description here',
    'author': 'AUTHOR',
    'url': 'URL',
    'download_url': 'URL',
    'author_email': 'EMAIL',
    'version': 'VERSION',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'NAME'
}

setup(**config)
"""


def make_directory(path, opts):
    os.makedirs(path)
    if opts.verbose:
        print 'Created directory %s' % path


def make_file(path, opts, data=""):
    f = open(path, 'w')
    f.write(data)
    f.close()
    if opts.verbose:
        print 'Created file %s' % path


def make_data_tests(data, opts):
    return data.replace('NAME', opts.name)


def make_data_setup(data, opts):
    data = data.replace('NAME', opts.name)
    data = data.replace('AUTHOR', opts.author)
    data = data.replace('EMAIL', opts.email)
    data = data.replace('URL', opts.url)
    data = data.replace('VERSION', opts.sversion)
    return data


def init():
    """parse the command line and initialize the whole thing"""
    parser = argparse.ArgumentParser(
        description='Create a generic skeleton for a Python project',
        epilog='written by Jonas Gorauskas')

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s 0.1.0 - written by Jonas Gorauskas')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')

    parser.add_argument('-r', '--root', help='The root directory to work from',
                        default=path.dirname(path.realpath(__file__)))

    parser.add_argument('-n', '--name', help='The project name',
                        required=True)
    parser.add_argument('-a', '--author', help="The author's name",
                        default="Author Name")
    parser.add_argument('-e', '--email', help="The author's email",
                        default='author@emaildomain.com')
    parser.add_argument('-u', '--url', help='The download URL',
                        default='https://github.com/author/package')
    parser.add_argument('-s', '--sversion', help='The software version',
                        default='0.1.0')

    return parser.parse_args()


def main():
    opts = init()
    d = path.join(opts.root, opts.name)
    if not path.exists(d):
        make_directory(d, opts)
        make_directory(path.join(d, 'bin'), opts)
        make_directory(path.join(d, opts.name), opts)
        make_directory(path.join(d, 'tests'), opts)
        make_directory(path.join(d, 'docs'), opts)
        make_file(path.join(path.join(d, opts.name), '__init__.py'), opts)
        make_file(path.join(path.join(d, 'tests'), '__init__.py'), opts)
        make_file(path.join(d, 'setup.py'), opts,
                  make_data_setup(DATA_SETUP, opts))
        make_file(path.join(path.join(d, 'tests'), opts.name + '_tests.py'),
                  opts, make_data_tests(DATA_TESTS, opts))


if __name__ == '__main__':
    main()
