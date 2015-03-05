#
# format.py
# Interface to JavaScript Standard Style Formatter
#
# Written by Dan Flettre
# Copyright (c) 2015 Dan Flettre
#
# License: MIT
#

"""This module exports the StandardFormatCommand class."""

import sublime
import sublime_plugin
from SublimeLinter.lint import util


class StandardFormatCommand(sublime_plugin.TextCommand):

    """Provides an interface to standard-format."""

    def run(self, edit):
        """Command to run when standard_format is executed."""
        cmd = []

        cmd.insert(0, util.which("standard-format"))
        reg = sublime.Region(0, self.view.size())
        allcode = self.view.substr(reg)

        result = util.communicate(cmd, code=allcode)

        if len(result) > 0:
            self.view.replace(edit, reg, result[:-1])
        else:
            args = cmd, code = reg, output_stream = util.STREAM_STDERR
            error = util.communicate(args)
            sublime.error_message(error)
