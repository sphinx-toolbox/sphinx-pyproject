#!/usr/bin/env python3
#
#  __init__.py
"""
Move some of your Sphinx configuration into ``pyproject.toml``.
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
from typing import Any, Dict, Iterator, List, Mapping, MutableMapping, Optional

# 3rd party
import dom_toml
from dom_toml.decoder import TomlPureDecoder
from dom_toml.parser import TOML_TYPES, AbstractConfigParser, BadConfigError
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.typing import PathLike
from domdf_python_tools.words import word_join

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["SphinxConfig", "ProjectParser"]


class SphinxConfig(Mapping[str, Any]):
	"""
	Read the Sphinx configuration from ``pyproject.toml``.

	:param pyproject_file: The path to the ``pyproject.toml`` file.
	:param globalns: The global namespace of the ``conf.py`` file.
		The variables parsed from the ``[tool.sphinx-pyproject]`` table will be added to this namespace.
		By default, or if explicitly :py:obj:`None`, this does not happen.
	:no-default globalns:

	.. autosummary-widths:: 1/4
	"""

	name: str
	"""
	The value of the :pep621:`project.name <name>` key in the :pep:`621` metadata.

	Underscores are replaced by dashes but :pep:`508` normalization is *not* applied.

	The recommendation is to assign this to the
	`project <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-project>`_
	variable in ``conf.py``:

	.. code-block:: python

		from sphinx_pyproject import SphinxConfig

		config = SphinxConfig()
		project = config.name
	"""

	version: str
	"""
	The value of the :pep621:`project.version <version>` key in the :pep:`621` metadata.

	Converted to a string if the value was a number in the ``pyproject.toml`` file.
	"""

	description: str
	"""
	The value of the :pep621:`project.description <description>` key in the :pep:`621` metadata.
	"""

	author: str
	"""
	A string giving the names of the authors.

	This is parsed from the :pep621:`project.authors <authors>` key in the :pep:`621` metadata,
	or the :pep621:`project.maintainers <maintainers>` key as a fallback.

	The names are joined together, e.g.:

	.. code-block:: TOML

		# pyproject.toml

		[[project.authors]]
		name = "Dominic Davis-Foster"

		[[project.authors]]
		name = "Joe Bloggs"

		[[project.authors]]
		name = "Jane Doe"

	.. code-block:: python

		>>> SphinxConfig("pyproject.toml").author
		'Dominic Davis-Foster, Joe Bloggs and Jane Doe'
	"""

	def __init__(
			self,
			pyproject_file: PathLike = "../pyproject.toml",
			*,
			globalns: Optional[MutableMapping] = None,
			):

		pyproject_file = PathPlus(pyproject_file).abspath()
		config = dom_toml.load(pyproject_file, decoder=TomlPureDecoder)

		if "project" not in config:
			raise BadConfigError(f"No 'project' table found in {pyproject_file.as_posix()}")

		pep621_config = ProjectParser().parse(config["project"])

		for key in ("name", "version", "description"):
			if key not in pep621_config:
				raise BadConfigError(
						f"Either {key!r} was not declared in the 'project' table "
						f"or it was marked as 'dynamic', which is unsupported by 'sphinx-pyproject'."
						)

		if "author" not in pep621_config:
			raise BadConfigError(
					f"Either 'authors/maintainers' was not declared in the 'project' table "
					f"or it was marked as 'dynamic', which is unsupported by 'sphinx-pyproject'."
					)

		self.name = pep621_config["name"]
		self.version = pep621_config["version"]
		self.description = pep621_config["description"]
		self.author = pep621_config["author"]

		self._freeform = config.get("tool", {}).get("sphinx-pyproject", {})

		if globalns is not None:
			globalns.update(pep621_config)
			globalns.update(self._freeform)

	def __getitem__(self, item) -> Any:
		"""
		Returns the value of the given key in the  ``tool.sphinx-pyproject`` table.

		:param item:
		"""

		return self._freeform[item]

	def __len__(self) -> int:
		"""
		Returns the number of keys in the ``tool.sphinx-pyproject`` table.
		"""

		return len(self._freeform)

	def __iter__(self) -> Iterator[str]:
		"""
		Returns an iterator over the keys in the ``tool.sphinx-pyproject`` table.

		:rtype:

		.. latex:clearpage::
		"""

		yield from self._freeform


class ProjectParser(AbstractConfigParser):
	"""
	Parser for :pep:`621` metadata from ``pyproject.toml``.

	.. autosummary-widths:: 7/16
	"""

	def parse_name(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the :pep621:`name` key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		name = config["name"]
		self.assert_type(name, str, ["project", "name"])
		return str(name).replace('_', '-')

	def parse_version(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the :pep621:`version` key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		version = config["version"]
		self.assert_type(version, (str, int), ["project", "version"])
		return str(version)

	def parse_description(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the :pep621:`description` key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		description = config["description"]
		self.assert_type(description, str, ["project", "description"])
		return description

	@staticmethod
	def parse_author(config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the :pep621:`authors/maintainers` key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		all_authors: List[Optional[str]] = []

		for idx, author in enumerate(config["author"]):
			name = author.get("name", None)

			if name is not None and ',' in name:
				raise BadConfigError(f"The 'project.authors[{idx}].name' key cannot contain commas.")

			all_authors.append(name)

		all_authors = list(filter(bool, all_authors))

		if not all_authors:
			raise BadConfigError(f"The 'project.authors' key cannot be empty.")

		return word_join(all_authors)  # type: ignore

	@property
	def keys(self) -> List[str]:
		"""
		The keys to parse from the TOML file.
		"""

		return [
				"name",
				"version",
				"description",
				"author",
				]

	def parse(
			self,
			config: Dict[str, TOML_TYPES],
			set_defaults: bool = False,
			) -> Dict[str, TOML_TYPES]:
		"""
		Parse the TOML configuration.

		:param config:
		:param set_defaults: Has no effect in this class.
		"""

		if "authors" in config:
			config["author"] = config.pop("authors")
		elif "maintainers" in config:
			config["author"] = config.pop("maintainers")

		return super().parse(config)
