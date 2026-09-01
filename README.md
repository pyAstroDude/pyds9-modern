# Python connection to ds9 via XPA

The [XPA messaging system](https://github.com/ericmandel/xpa) provides
seamless communication between many kinds of Unix programs, including Tcl/Tk
programs such as ds9. The ``pyds9`` module uses a Python interface to XPA to
communicate with ds9. It supports communication with all of ds9's XPA access
points.

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

## Installation

Install from PyPI:

    pip install pyds9

For a local checkout:

    git clone https://github.com/ericmandel/pyds9.git
    cd pyds9
    python -m pip install -e .

## Usage

    >>> import pyds9
    >>> print(pyds9.ds9_targets())
    >>> d = pyds9.DS9()  # open a new ds9 window or connect to an existing one
    >>> d.set("file /path/to/fits")  # send the file to the open ds9 session

## Notes

- The public Python API remains the compatibility contract for the project.
- The package is being modernized toward a pip-first install flow.
- During the migration period, a legacy compatibility import path remains in place.
- If DS9 or XPA is not installed and visible on your system, the package will
  fail with a clear runtime error rather than a confusing build-time issue.

To report a bug, ask for a new feature, or request support, please contact us at
https://github.com/ericmandel/pyds9/issues

The PyDS9 team
