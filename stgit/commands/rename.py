__copyright__ = """
Copyright (C) 2005, Catalin Marinas <catalin.marinas@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
"""

import sys, os
from optparse import OptionParser, make_option

from stgit.commands.common import *
from stgit.utils import *
from stgit.out import *
from stgit import stack, git


help = 'rename a patch in the series'
usage = """%prog [options] <oldpatch> <newpatch>

Rename <oldpatch> into <newpatch> in a series."""

directory = DirectoryHasRepository()
options = [make_option('-b', '--branch',
                       help = 'use BRANCH instead of the default one')]


def func(parser, options, args):
    """Rename a patch in the series
    """
    if len(args) != 2:
        parser.error('incorrect number of arguments')

    out.start('Renaming patch "%s" to "%s"' % (args[0], args[1]))
    crt_series.rename_patch(args[0], args[1])
    out.done()
