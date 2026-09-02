# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""Python interface to the DS9/XPA messaging system.

This package is kept intentionally small and stable: the DS9/XPA runtime
API remains the compatibility contract, while the packaging layer is being
modernized for pip-first installation.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .pyds9 import *

__version__ = "2.0.0"

# Temporary compatibility bridge for one release cycle while the project
# moves to the modern package layout.
__all__ = [
    "DS9",
    "ds9",
    "ds9_openlist",
    "ds9_targets",
    "ds9_xpans",
    "ds9Globals",
]

# Legacy import path compatibility: ``from pyds9 import pyds9`` should still
# continue to resolve while the modernized package layout is finalized.
try:
    from . import pyds9 as pyds9  # noqa: F401
except ImportError:  # pragma: no cover
    pyds9 = None
