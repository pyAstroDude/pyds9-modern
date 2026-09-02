#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from pathlib import Path

from setuptools import find_packages, setup


README = Path(__file__).resolve().parent / "README.md"

setup(
    name="pyds9",
    description="Python connection to ds9 via XPA",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Bill Joye and Eric Mandel",
    author_email="saord@cfa.harvard.edu",
    license="BSD",
    url="https://github.com/pyAstroDude/pyds9-modern",
    packages=find_packages(include=["pyds9", "pyds9.*"]),
    include_package_data=True,
    package_data={
        "pyds9": ["data/*"],
        "pyds9.tests": ["data/*.fits"],
    },
    install_requires=["astropy", "numpy"],
    extras_require={
        "test": ["pytest", "pytest-cov"],
    },
    python_requires=">=3.10",
    zip_safe=False,
)
