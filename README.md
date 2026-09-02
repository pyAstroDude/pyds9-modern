# pyds9-modern

An independently maintained modernized version of the legacy
[pyds9](https://github.com/ericmandel/pyds9) project: a Python interface for
communicating with [SAOImage DS9](https://ds9.si.edu/) through the
[XPA messaging system](https://github.com/ericmandel/xpa).

This repository began as a clone of the original pyds9 source tree and was
refactored to use modern Python packaging and maintenance practices. The
runtime import remains `pyds9` so existing Python code can continue to use the
same public API.

## Project status

- Independent repository: `https://github.com/pyAstroDude/pyds9-modern`
- Current release: `2.0.0`
- Supported Python: `3.10` and newer
- Installation source: GitHub only; this project is not currently published on PyPI

## What changed

The modernization removed the obsolete bundled build system and replaced it
with a pip-first project configuration.

Removed:

- Bundled XPA C source and build files
- The legacy `astropy_helpers` and `ah_bootstrap.py` machinery
- Obsolete Travis CI and AppVeyor configuration
- Unused package and test configuration placeholders

Added or updated:

- Standard `pyproject.toml` build configuration
- Explicit Python `>=3.10` requirement
- System XPA runtime discovery and installation guidance
- Updated pytest and Sphinx configuration
- Reliable DS9/XPA integration-test startup
- Documentation for installing directly from this GitHub repository

The previous project documentation is preserved in
[`README-legacy.md`](README-legacy.md).

## Prerequisites

This package expects a system-installed ``ds9`` and the native XPA runtime to be
available before using the Python client.

On macOS, install XPA into the same conda environment where you will install and
run ``pyds9``. For example, to use an environment named ``pyds9-modern``:

    conda activate pyds9-modern
    conda install -c conda-forge xpa

Then install ``pyds9`` in that activated environment. Confirm that XPA is
available before importing the package:

    python - <<'PY'
    import ctypes.util
    print("XPA:", ctypes.util.find_library("xpa"))
    PY

If this prints a path or library name, the XPA library is available. If it prints
``None``, verify that the intended conda environment is activated and rerun the
``conda install`` command above.

## Requirements

Before installing this package, install Python 3.10 or newer, [SAOImage
DS9](https://ds9.si.edu/), and the native XPA runtime in the same environment as
Python.

The recommended conda setup installs all runtime, test, build, and
documentation dependencies from [`environment.yml`](environment.yml):

```bash
git clone https://github.com/pyAstroDude/pyds9-modern.git
cd pyds9-modern
conda env create -f environment.yml
conda activate pyds9-modern
```

The environment file installs the package from the local checkout. To install
the package manually in an existing environment, first install XPA:

```bash
conda install -c conda-forge xpa
```

Then install the package from the checkout or directly from GitHub as described
below. Confirm that XPA is visible to the active Python environment:

```bash
python -c "import ctypes.util; print(ctypes.util.find_library('xpa'))"
```

This should print an XPA library path or name rather than `None`.

## Installation from GitHub

This project is intentionally installed directly from the non-PyPI GitHub
repository:

```bash
git clone https://github.com/pyAstroDude/pyds9-modern.git
cd pyds9-modern
python -m pip install .
```

To install the current `master` branch without cloning first:

```bash
python -m pip install \
    git+https://github.com/pyAstroDude/pyds9-modern.git
```

For development and tests:

```bash
python -m pip install ".[test]"
python -m pytest -q
```

## Usage

```python
import pyds9

print(pyds9.ds9_targets())
d = pyds9.DS9()
d.set("file /path/to/file.fits")
```

The DS9 application must be installed and available for the integration
operations to work.

## Development

The test suite includes conversion tests and DS9/XPA integration tests. The
validated baseline for version `2.0.0` is **39 passing tests**.

Issues and contributions can be opened at
https://github.com/pyAstroDude/pyds9-modern/issues.
