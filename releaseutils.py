#!/usr/bin/python -tt

# Copyright Red Hat Inc 2013-2015
# Licensed under the terms of the LGPLv2+

from __future__ import print_function

import glob
import os
import shutil
import sys
import textwrap

from contextlib import contextmanager
from distutils.sysconfig import get_python_lib

import subprocess
from importlib.metadata import distribution

import fedora.release
from six.moves import configparser, map


#
# Helper functions
#

@contextmanager
def pushd(dirname):
    '''Contextmanager so that we can switch directories that the script is
    running in and have the current working directory restored  afterwards.
    '''
    curdir = os.getcwd()
    os.chdir(dirname)
    try:
        yield curdir
    finally:
        os.chdir(curdir)


class MsgFmt(object):
    def run(self, args):
        cmd = subprocess.Popen(args, shell=False)
        cmd.wait()


def setup_message_compiler():
    # Look for msgfmt
    try:
        # Prefer msgfmt because it will throw errors on misformatted messages
        subprocess.Popen(['msgfmt', '-h'], stdout=subprocess.PIPE)
    except OSError:
        import babel.messages.frontend

        return (
            babel.messages.frontend.CommandLineInterface(),
            'pybabel compile -D %(domain)s -d locale -i %(pofile)s -l %(lang)s'
        )
    else:
        return (
            MsgFmt(),
            'msgfmt -c -o locale/%(lang)s/LC_MESSAGES/%(domain)s.mo %(pofile)s'
        )


def _add_destdir(path):
    if ENVVARS['DESTDIR'] is not None:
        if path.startswith('/'):
            path = path[1:]
        path = os.path.join(ENVVARS['DESTDIR'], path)
    return path


def usage():
    print ('Subcommands:')
    for command in sorted(SUBCOMMANDS.keys()):
        print('%-15s  %s' % (command, SUBCOMMANDS[command][1]))

    print()
    print('This script can be customized by setting the following ENV VARS:')
    for var in sorted(ENVVARDESC.keys()):
        lines = textwrap.wrap(
            '%-15s  %s' % (var, ENVVARDESC[var]),
            subsequent_indent=' '*8
        )
        for line in lines:
            print(line.rstrip())
    sys.exit(1)

SUBCOMMANDS = {
}

ENVVARDESC = {
    'DESTDIR': 'Alternate root directory hierarchy to install into',
    'PACKAGENAME': 'Pypi packagename (commonly the setup.py name field)',
    'MODULENAME': 'Python module name (commonly used with import NAME)',
    'INSTALLSTRATEGY': 'One of FHS, EGG, SITEPACKAGES.  FHS will work'
    ' for system packages installed using'
    ' --single-version-externally-managed.  EGG install into an egg'
    ' directory.  SITEPACKAGES will install into a $PACKAGENAME'
    ' directory directly in site-packages.  Default FHS'
}

ENVVARS = dict(map(lambda k: (k, os.environ.get(k)), ENVVARDESC.keys()))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('At least one subcommand is needed\n')
        usage()
    try:
        SUBCOMMANDS[sys.argv[1]][0]()
    except KeyError:
        print ('Unknown subcommand: %s\n' % sys.argv[1])
        usage()
