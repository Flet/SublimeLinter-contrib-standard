# SublimeLinter-contrib-standard

[SublimeLinter](https://www.sublimelinter.com/en/latest/) plugin to provide linting with [standardjs](https://standardjs.com/). Matching `.js` and `.jsx` source files.

## Requirements

1. SublimeLinter is a requirement, please follow the installation instructions [here](https://www.sublimelinter.com/en/latest/installation.html).
2. Standard JS is a requirement, please follow the installation instructions [here](https://standardjs.com/index.html#install).

## Install

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Select **Package Control: Install Package**
3. Select **SublimeLinter-contrib-standard**

### Linter Executable

If a linter executable cannot be found, [follow these steps](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) to locate the source of the problem.

## Automatic Formatting

Automatic formatting is not a task for a linter. However, it can be provided by the [StandardFormat](https://packagecontrol.io/packages/StandardFormat) package.

## Contributing

Contributions are more than welcome :) Should you like to help out, please bear in mind that contribution should follow the guidelines specified in the [pyproject.toml](./pyproject.toml) file. (**flake8**, **black**).
