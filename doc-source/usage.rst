=================
Usage
=================


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
