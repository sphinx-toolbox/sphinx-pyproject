=======
Usage
=======

The :class:`~.SphinxConfig` class will load the configuration from ``pyproject.toml``.
By passing :func:`globalns=globals() <globals>` to the class constructor, the keys parsed from the
``pyproject.toml`` file will be added to the global namespace of the ``conf.py`` file.

.. compound::

	For example:

	.. code-block:: python3

		# conf.py

		from sphinx_pyproject import SphinxConfig

		config = SphinxConfig("../pyproject.toml", globalns=globals())

		author  # This name *looks* to be undefined, but it isn't.


.. compound::

	The :class:`~.SphinxConfig` class also provides a :class:`collections.abc.Mapping` interface.
	If you are going to override or modify one of the configuration values after parsing it,
	the recommended approach is to explicitly assign the name:

	.. code-block:: python

		extensions = config["extensions"]
		extensions.append("sphinx.ext.autodoc")

	This will prevent warnings from linters etc., but is not necessary for Sphinx to see the configuration.


.. note::

   At time of writing the "Poetry" tool does not support PEP 621. To enable a mode compatible with
   the ``[tool.poetry]`` heading supply the argument ``style="poetry"``. For example:

   .. code-block:: python

      config = SphinxConfig("../pyproject.toml", style="poetry")


Configuration
----------------

``sphinx-pyproject`` parses the configuration from the ``[project]`` and ``[tool.sphinx-pyproject]`` tables in ``pyproject.toml``.
The ``[project]`` table is defined in :pep:`621`.
``sphinx-pyproject`` only uses the following keys:

* :pep621:`name` – The name of the project.
* :pep621:`version` – The version of the project.
* :pep621:`description` – The summary description of the project.
* One of :pep621:`authors/maintainers`.

The remaining `Sphinx configuration values`_ can be provided in the ``[tool.sphinx-pyproject]`` table.

See `this project's pyproject.toml file`_ for an example of this configuration.

.. _Sphinx configuration values: https://www.sphinx-doc.org/en/master/usage/configuration.html
.. _this project's pyproject.toml file: https://github.com/sphinx-toolbox/sphinx-pyproject/blob/master/pyproject.toml
