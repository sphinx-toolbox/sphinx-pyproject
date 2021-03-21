#!/usr/bin/env python3
#
#  __init__.py
"""
Move some of your Sphinx configuration into ``pyproject.toml``.


* `project <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-project>`_ --
  ``project.name``, with underscores replaced by dashes but otherwise verbatim.
  :pep:`508` normalization is *not* applied.

* `author <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-author>`_ --
  Parsed from ``project.authors`` (falls back to ``project.maintainers``)

* `version <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version>`_ /
  `release <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-release>`_ --
  Parsed from ``project.version``

* ``description`` -- Parsed from ``project.description``. May be useful for :mod:`sphinx_toolbox.documentation_summary`.

* `extensions <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions>`_ --
  Parsed from ``tool.sphinx-pyproject.extensions``, a list of strings.

* `source_suffix <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_suffix>`_ --
  Parsed from ``tool.sphinx-pyproject.source_suffix``.
  Either a string, a list of strings, or a mapping of strings to strings.

* `source_encoding <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_encoding>`_ --
  Parsed from ``tool.sphinx-pyproject.source_encoding``, a string.

* `source_parsers <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_parsers>`_ --
  Parsed from ``tool.sphinx-pyproject.source_parsers``, a mapping of strings to strings.

* `master_doc <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master_doc>`_ --
  Parsed from ``tool.sphinx-pyproject.master_doc``, a string.

* `exclude_patterns <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-exclude_patterns>`_ --
  Parsed from ``tool.sphinx-pyproject.exclude_patterns``, a list of strings.

* `templates_path <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path>`_ --
  Parsed from ``tool.sphinx-pyproject.templates_path``, a list of strings.

* `manpages_url <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-manpages_url>`_ --
  Parsed from ``tool.sphinx-pyproject.manpages_url``, a string.

* `nitpicky <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpicky>`_ --
  Parsed from ``tool.sphinx-pyproject.nitpicky``, :py:obj:`True` or :py:obj:`False`.

* `pygments_style <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-pygments_style>`_ --
  Parsed from ``tool.sphinx-pyproject.pygments_style``, a string.

* `add_function_parentheses <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_function_parentheses>`_ --
  Parsed from ``tool.sphinx-pyproject.add_function_parentheses``, :py:obj:`True` or :py:obj:`False`.

* `add_module_names <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_module_names>`_ --
  Parsed from ``tool.sphinx-pyproject.add_module_names``, :py:obj:`True` or :py:obj:`False`.

* `show_authors <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-show_authors>`_ --
  Parsed from ``tool.sphinx-pyproject.show_authors``, :py:obj:`True` or :py:obj:`False`.

* `trim_footnote_reference_space <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-trim_footnote_reference_space>`_ --
  Parsed from ``tool.sphinx-pyproject.trim_footnote_reference_space``, :py:obj:`True` or :py:obj:`False`.

* `trim_doctest_flags <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-trim_doctest_flags>`_ --
  Parsed from ``tool.sphinx-pyproject.trim_doctest_flags``, :py:obj:`True` or :py:obj:`False`.

* `strip_signature_backslash <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-strip_signature_backslash>`_ --
  Parsed from ``tool.sphinx-pyproject.strip_signature_backslash``, :py:obj:`True` or :py:obj:`False`.

* `language <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language>`_ --
  Parsed from ``tool.sphinx-pyproject.language``, a string.

* `html_theme <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme>`_ --
  Parsed from ``tool.sphinx-pyproject.html_theme``, a string.

* `html_theme_options <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options>`_ --
  Parsed from ``tool.sphinx-pyproject.html_theme_options``, a table.

* `html_logo <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo>`_ --
  Parsed from ``tool.sphinx-pyproject.html_logo``, a string.

* `html_static_path <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path>`_ --
  Parsed from ``tool.sphinx-pyproject.html_static_path``, a list of strings.

* `html_show_sourcelink <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_show_sourcelink>`_ --
  Parsed from ``tool.sphinx-pyproject.html_show_sourcelink``, :py:obj:`True` or :py:obj:`False`.

* `html_context <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context>`_ --
  Parsed from ``tool.sphinx-pyproject.html_context``, a table.


``sphinx-pyproject`` will validate the *type* of values provided in ``pyproject.toml``,
but leaves it to Sphinx to check the value is correct.

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
import functools
from typing import Any, Iterator, Mapping, Set

# 3rd party
import dom_toml
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.typing import PathLike

# this package
from sphinx_pyproject.parser import ProjectParser, SphinxPyprojectParser

__all__ = [
		"PyProjectConfig",
		"get_add_function_parentheses",
		"get_add_module_names",
		"get_description",
		"get_exclude_patterns",
		"get_extensions",
		"get_html_context",
		"get_html_logo",
		"get_html_show_sourcelink",
		"get_html_static_path",
		"get_html_theme",
		"get_html_theme_options",
		"get_language",
		"get_manpages_url",
		"get_master_doc",
		"get_name",
		"get_nitpicky",
		"get_pygments_style",
		"get_show_authors",
		"get_source_encoding",
		"get_source_parsers",
		"get_source_suffix",
		"get_strip_signature_backslash",
		"get_templates_path",
		"get_trim_doctest_flags",
		"get_trim_footnote_reference_space",
		"get_version"
		]

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.0.0"
__email__: str = "dominic@davis-foster.co.uk"


class PyProjectConfig(Mapping[str, Any]):

	def __init__(self, pyproject_file: PathLike):
		self.pyproject_file = PathPlus(pyproject_file)

		config = dom_toml.load(self.pyproject_file)

		self._621parser = ProjectParser()
		self._parser = SphinxPyprojectParser()

		if "project" in config:
			self._621config = self._621parser.parse(config["project"])
		else:
			self._621config = {}

		if "sphinx-pyproject" in config.get("tool", {}):
			self._config = self._parser.parse(config["tool"])
		else:
			self._config = {}

	@property
	def valid_keys(self) -> Set[str]:
		return {*self._621parser.keys, *self._parser.keys}

	def __len__(self) -> int:
		return len(self._621config) + len(self._config)

	def __iter__(self) -> Iterator[str]:
		yield from self._621config
		yield from self._config

	def __getitem__(self, item):
		if item not in self.valid_keys:
			raise KeyError(f"Unsupported configuration value {item!r}")

		elif item in self._621config:
			return self._621config[item]
		elif item in self._config:
			return self._config[item]
		else:
			raise KeyError(f"Undefined configuration value {item!r}")

	def __getattr__(self, item):
		if item.startswith("get_") and item[4:] in self.valid_keys:
			return lambda: self[item[4:]]
		else:
			return super().__getattribute__(item)


_621parser = ProjectParser()
_parser = SphinxPyprojectParser()


def get_name(pyproject_file: PathLike):
	return _621parser.parse_name(dom_toml.load(pyproject_file)["project"])


def get_version(pyproject_file: PathLike):
	return _621parser.parse_version(dom_toml.load(pyproject_file)["project"])


def get_description(pyproject_file: PathLike):
	return _621parser.parse_description(dom_toml.load(pyproject_file)["project"])


# TODO: author


@functools.lru_cache(3)
def _cached_loads(filename: PathLike):
	return dom_toml.load(filename).get("tool", {})["sphinx-pyproject"]


def get_extensions(pyproject_file: PathLike):
	return _parser.parse_extensions(_cached_loads(pyproject_file))


def get_source_suffix(pyproject_file: PathLike):
	return _parser.parse_source_suffix(_cached_loads(pyproject_file))


def get_source_encoding(pyproject_file: PathLike):
	return _parser.parse_source_encoding(_cached_loads(pyproject_file))


def get_source_parsers(pyproject_file: PathLike):
	# return _parser.parse_source_parsers(_cached_loads(pyproject_file))
	return _cached_loads(pyproject_file)["source_parsers"]


def get_master_doc(pyproject_file: PathLike):
	return _parser.parse_master_doc(_cached_loads(pyproject_file))


def get_exclude_patterns(pyproject_file: PathLike):
	return _parser.parse_exclude_patterns(_cached_loads(pyproject_file))


def get_templates_path(pyproject_file: PathLike):
	return _parser.parse_templates_path(_cached_loads(pyproject_file))


def get_manpages_url(pyproject_file: PathLike):
	return _parser.parse_manpages_url(_cached_loads(pyproject_file))


def get_nitpicky(pyproject_file: PathLike):
	return _parser.parse_nitpicky(_cached_loads(pyproject_file))


def get_pygments_style(pyproject_file: PathLike):
	return _parser.parse_pygments_style(_cached_loads(pyproject_file))


def get_add_function_parentheses(pyproject_file: PathLike):
	return _parser.parse_add_function_parentheses(_cached_loads(pyproject_file))


def get_add_module_names(pyproject_file: PathLike):
	return _parser.parse_add_module_names(_cached_loads(pyproject_file))


def get_show_authors(pyproject_file: PathLike):
	return _parser.parse_show_authors(_cached_loads(pyproject_file))


def get_trim_footnote_reference_space(pyproject_file: PathLike):
	return _parser.parse_trim_footnote_reference_space(_cached_loads(pyproject_file))


def get_trim_doctest_flags(pyproject_file: PathLike):
	return _parser.parse_trim_doctest_flags(_cached_loads(pyproject_file))


def get_strip_signature_backslash(pyproject_file: PathLike):
	return _parser.parse_strip_signature_backslash(_cached_loads(pyproject_file))


def get_language(pyproject_file: PathLike):
	return _parser.parse_language(_cached_loads(pyproject_file))


def get_html_theme(pyproject_file: PathLike):
	return _parser.parse_html_theme(_cached_loads(pyproject_file))


def get_html_theme_options(pyproject_file: PathLike):
	# return _parser.parse_html_theme_options(_cached_loads(pyproject_file))
	return _cached_loads(pyproject_file)["html_theme_options"]


def get_html_logo(pyproject_file: PathLike):
	return _parser.parse_html_logo(_cached_loads(pyproject_file))


def get_html_static_path(pyproject_file: PathLike):
	return _parser.parse_html_static_path(_cached_loads(pyproject_file))


def get_html_show_sourcelink(pyproject_file: PathLike):
	return _parser.parse_html_show_sourcelink(_cached_loads(pyproject_file))


def get_html_context(pyproject_file: PathLike):
	# return _parser.parse_html_context(_cached_loads(pyproject_file))
	return _cached_loads(pyproject_file)["html_context"]
