#!/usr/bin/env python3

# stdlib
import os
import re

# this package
from sphinx_pyproject import SphinxConfig


config = SphinxConfig(globalns=globals())

github_url = "https://github.com/{github_username}/{github_repository}".format_map(config)

rst_prolog = f""".. |pkgname| replace:: sphinx-pyproject
.. |pkgname2| replace:: ``sphinx-pyproject``
.. |browse_github| replace:: `Browse the GitHub Repository <{github_url}>`__
"""

project = config.name
slug = re.sub(r'\W+', '-', project.lower())
htmlhelp_basename = slug

release = config.version
documentation_summary = config.description

todo_include_todos = bool(os.environ.get("SHOW_TODOS", 0))

intersphinx_mapping = {
		"python": ("https://docs.python.org/3/", None),
		"sphinx": ("https://www.sphinx-doc.org/en/stable/", None),
		"sphinx-toolbox": ("https://sphinx-toolbox.readthedocs.io/en/latest", None),
		}

latex_documents = [("index", f'{slug}.tex', project, config.author, "manual")]
man_pages = [("index", slug, project, [config.author], 1)]
texinfo_documents = [("index", slug, project, config.author, slug, project, "Miscellaneous")]

toctree_plus_types = {
		"class",
		"function",
		"method",
		"data",
		"enum",
		"flag",
		"confval",
		"directive",
		"role",
		"confval",
		"protocol",
		"typeddict",
		"namedtuple",
		"exception",
		}


autodoc_default_options = {
		"members": None,  # Include all members (methods).
		"special-members": None,
		"autosummary": None,
		"show-inheritance": None,
		"exclude-members": ','.join(config["autodoc_exclude_members"]),
		}
