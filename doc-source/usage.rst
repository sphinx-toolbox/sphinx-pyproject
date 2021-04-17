=======
Usage
=======

The :class:`~.SphinxConfig` class will load the configuration from ``pyproject.toml``.
By passing :func:`globalns=globals() <globals>` to the class constructor, the keys parsed from the
``pyproject.toml`` file will be added to the global namespace of the ``conf.py`` file.

For example:

.. code-block:: python

	# conf.py

	from sphinx_pyproject import SphinxConfig

	config = SphinxConfig("../pyproject.toml", globalns=globals())

	author  # This name *looks* to be undefined, but it isn't.

The :class:`~.SphinxConfig` class also provides a :class:`collections.abc.Mapping` interface.
If you are going to override or modify one of the configuration values after parsing it,
the recommended approach is to explicitly assign the name:

.. code-block:: python

	extensions = config["extensions"]
	extensions.append("sphinx.ext.autodoc")

This will prevent warnings from linters etc., but is not necessary for Sphinx to see the configuration.


Configuration
----------------

``sphinx-pyproject`` parses the configuration from the ``[project]`` and ``[tool.sphinx-pyproject]`` tables in ``pyproject.toml``.
The ``[project]`` table is defined in :pep:`621`.
``sphinx-pyproject`` only uses the following keys:

* name_ -- The name of the project.
* version_ -- The version of the project.
* description_ -- The summary description of the project.
* One of `authors/maintainers`_.

The remaining `Sphinx configuration values`_ can be provided in the ``[tool.sphinx-pyproject]`` table.

See `this project's pyproject.toml file`_ for an example of this configuration.

.. _name: https://www.python.org/dev/peps/pep-0621/#name
.. _version: https://www.python.org/dev/peps/pep-0621/#version
.. _description: https://www.python.org/dev/peps/pep-0621/#description
.. _authors/maintainers: https://www.python.org/dev/peps/pep-0621/#authors-maintainers
.. _Sphinx configuration values: https://www.sphinx-doc.org/en/master/usage/configuration.html
.. _this project's pyproject.toml file: https://github.com/sphinx-toolbox/sphinx-pyproject/blob/master/pyproject.toml
