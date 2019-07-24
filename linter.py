#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dan Flettre
# Copyright (c) 2015 Dan Flettre
#
# License: MIT
#

"""This module exports the Standard plugin class."""

from SublimeLinter.lint import NodeLinter


class Standard(NodeLinter):
    """Provides an interface to standard."""

    cmd = 'standard --stdin --verbose'
    name = 'Standard'
    regex = r'^\s.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'

    defaults = {
        'enable_if_dependency': True,
        'disable_if_not_dependency': False,
        'selector': 'source.js, source.jsx'
    }
