# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""Compatibility shim for older Astropy-style package imports.

This project no longer relies on the legacy astropy_helpers bootstrap at
runtime. This module remains only as a migration shim so that older import
patterns still resolve cleanly while the modernization is taking place.
"""

__all__ = ["__version__", "__githash__", "_ASTROPY_SETUP_"]

_ASTROPY_SETUP_ = False
__version__ = "2.0.0"
__githash__ = ""


def test(*args, **kwargs):
    """Compatibility wrapper for legacy ``pyds9.test()`` callers.

    The modern project uses pytest directly; this shim preserves the historical
    import surface while avoiding the astropy bootstrap dependency.
    """
    import pytest

    print(
        "Note: pyds9.test() is preserved as a compatibility wrapper. "
        "Use pytest directly for modern test runs."
    )
    return pytest.main(list(args) if args else [])
