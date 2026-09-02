pyds9-modern Documentation
===========================

.. currentmodule:: pyds9

**A Python Connection to DS9 via XPA**

The XPA messaging system (https://github.com/ericmandel/xpa) provides
seamless communication between many kinds of Unix programs, including Tcl/Tk
programs such as ds9. The pyds9 module uses a Python interface to XPA to
communicate with ds9. It supports communication with all of ds9's XPA access
points. See https://ds9.si.edu/doc/ref/xpa.html for more information on DS9's access
points.

Install the package from the independent GitHub repository after installing
Python 3.10 or newer, DS9, and the native XPA runtime::

    git clone https://github.com/pyAstroDude/pyds9-modern.git
    cd pyds9-modern
    python -m pip install .

The package uses the system XPA runtime; it does not build or bundle XPA.

The DS9 Class
-------------

.. autoclass:: DS9
   :members: __init__, get, set, info, access, get_fits, set_fits, get_arr2np, set_np2arr
   :noindex:

Auxiliary Routines
------------------

.. autofunction:: ds9_targets
   :noindex:

.. autofunction:: ds9_openlist
   :noindex:

.. autofunction:: ds9_xpans
   :noindex:

.. toctree::
   :maxdepth: 2

Reference/API
-------------
.. automodule:: pyds9
	:members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

