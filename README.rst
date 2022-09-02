#################
sphinx-pyproject
#################

.. start short_desc

**Move some of your Sphinx configuration into pyproject.toml**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/sphinx-pyproject/latest?logo=read-the-docs
	:target: https://sphinx-pyproject.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/sphinx-toolbox/sphinx-pyproject/workflows/Docs%20Check/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/sphinx-toolbox/sphinx-pyproject/workflows/Linux/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/sphinx-toolbox/sphinx-pyproject/workflows/Windows/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/sphinx-toolbox/sphinx-pyproject/workflows/macOS/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/sphinx-toolbox/sphinx-pyproject/workflows/Flake8/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/sphinx-toolbox/sphinx-pyproject/workflows/mypy/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/sphinx-toolbox/sphinx-pyproject/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/sphinx-toolbox/sphinx-pyproject/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/sphinx-toolbox/sphinx-pyproject/master?logo=coveralls
	:target: https://coveralls.io/github/sphinx-toolbox/sphinx-pyproject?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sphinx-toolbox/sphinx-pyproject?logo=codefactor
	:target: https://www.codefactor.io/repository/github/sphinx-toolbox/sphinx-pyproject
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/sphinx-pyproject
	:target: https://pypi.org/project/sphinx-pyproject/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sphinx-pyproject?logo=python&logoColor=white
	:target: https://pypi.org/project/sphinx-pyproject/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sphinx-pyproject
	:target: https://pypi.org/project/sphinx-pyproject/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/sphinx-pyproject
	:target: https://pypi.org/project/sphinx-pyproject/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/sphinx-pyproject?logo=anaconda
	:target: https://anaconda.org/domdfcoding/sphinx-pyproject
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/sphinx-pyproject?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/sphinx-pyproject
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/sphinx-toolbox/sphinx-pyproject
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/sphinx-toolbox/sphinx-pyproject
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/sphinx-pyproject/v0.1.0
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/sphinx-pyproject
	:target: https://github.com/sphinx-toolbox/sphinx-pyproject/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2022
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/sphinx-pyproject
	:target: https://pypi.org/project/sphinx-pyproject/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``sphinx-pyproject`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install sphinx-pyproject

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install sphinx-pyproject

.. end installation

Usage
-------

The ``SphinxConfig`` class will load the configuration from ``pyproject.toml``.
By passing ``globalns=globals()`` to the class constructor, the keys parsed from the
``pyproject.toml`` file will be added to the global namespace of the ``conf.py`` file.

For example:

.. code-block:: python3

	# conf.py

	from sphinx_pyproject import SphinxConfig

	config = SphinxConfig("../pyproject.toml", globalns=globals())

	author  # This name *looks* to be undefined, but it isn't.

The ``SphinxConfig`` class also provides a ``collections.abc.Mapping`` interface.
If you are going to override or modify one of the configuration values after parsing it,
the recommended approach is to explicitly assign the name:

.. code-block:: python

	extensions = config["extensions"]
	extensions.append("sphinx.ext.autodoc")

This will prevent warnings from linters etc., but is not necessary for Sphinx to see the configuration.


Configuration
^^^^^^^^^^^^^^^

``sphinx-pyproject`` parses the configuration from the ``[project]`` and ``[tool.sphinx-pyproject]`` tables in ``pyproject.toml``.
The ``[project]`` table is defined in `PEP 621`_.
``sphinx-pyproject`` only uses the following keys:

* name_ – The name of the project.
* version_ – The version of the project.
* description_ – The summary description of the project.
* One of `authors/maintainers`_.

The remaining `Sphinx configuration values`_ can be provided in the ``[tool.sphinx-pyproject]`` table.

See `this project's pyproject.toml file`_ for an example of this configuration.

.. _PEP 621: https://www.python.org/dev/peps/pep-0621/#authors-maintainers
.. _name: https://www.python.org/dev/peps/pep-0621/#name
.. _version: https://www.python.org/dev/peps/pep-0621/#version
.. _description: https://www.python.org/dev/peps/pep-0621/#description
.. _authors/maintainers: https://www.python.org/dev/peps/pep-0621/#authors-maintainers
.. _Sphinx configuration values: https://www.sphinx-doc.org/en/master/usage/configuration.html
.. _this project's pyproject.toml file: https://github.com/sphinx-toolbox/sphinx-pyproject/blob/master/pyproject.toml
