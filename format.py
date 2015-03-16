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
import os

settings = None


def plugin_loaded():
    global settings
    settings = sublime.load_settings(
        "SublimeLinter-contrib-standard.sublime-settings")

def is_javascript(view):
    """Checks if the current view is javascript or not.  Used pre_save event"""
    # Check the file extension
    name = view.file_name()
    excludes = set(settings.get('excludes', []))
    includes = set(settings.get('includes', ['js']))
    if name and os.path.splitext(name)[1][1:] in includes - excludes:
        return True
    # If it has no name (?) or it's not a JS, check the syntax
    syntax = view.settings().get("syntax")
    if syntax and "javascript" in syntax.split("/")[-1].lower():
        return True
    return False

class StandardFormatEventListener(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        if settings.get("format_on_save") and is_javascript(view):
            view.run_command("standard_format")

class StandardFormatCommand(sublime_plugin.TextCommand):

    """Provides an interface to standard-format."""

    def run(self, edit):
        """Command to run when standard_format is executed."""
        v = self.view
        regions = []
        sel = v.sel()

        for region in sel:
            if not region.empty():
                regions.append(region)

        if len(regions) < 1:
            # No selected regions, so format the whole file.
            allreg = sublime.Region(0, v.size())
            regions.append(allreg)

        for region in regions:
            self.doFormat(edit, region, v)

    def doFormat(self, edit, region, v):
        """Format a region of text using standard --format command."""
        cmd = []
        cmd.append(util.which("standard"))
        cmd.append("--stdin")
        cmd.append("--format")

        if not region.empty():
                s = v.substr(region)
                s = util.communicate(cmd, code=s)
                if len(s) > 0:
                    v.replace(edit, region, s)
                else:
                    args = cmd, code = s, output_stream = util.STREAM_STDERR
                    error = util.communicate(args)
                    sublime.error_message(error)
