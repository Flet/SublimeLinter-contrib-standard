# SublimeLinter-contrib-standard

Linter plugin for [SublimeLinter][https://www.sublimelinter.com/en/latest/] to provide linting with [standardjs](https://standardjs.com/). It will be used with files that match `source.js` and `source.jsx`

## Requirements

1. SublimeLinter is a requirement, please follow the installation instructions [here][https://www.sublimelinter.com/en/latest/installation.html].
2. Standard JS is a requirement, please follow the installation instructions [here][https://standardjs.com/index.html#install].

## Install

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Select **Package Control: Install Package**
3. Select **SublimeLinter-contrib-standard**

### Linter Executable

If a linter executable cannot be found, [follow these steps](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) to locate the source of the problem.

## Automatic Formatting

Automatic formatting is not a task for a Linter. However it can be provided by the [StandardFormat](https://packagecontrol.io/packages/StandardFormat) package.

## Contributing

If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
2. Hack on a separate topic branch created from the latest `master`.
3. Commit and push the topic branch.
4. Make a pull request.

Please note: contributions should follow the guidelines specified in the `pyproject.toml` file. (**flake8**, **black** with minor tweaks).
