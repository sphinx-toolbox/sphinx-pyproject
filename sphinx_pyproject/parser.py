#!/usr/bin/env python3
#
#  parser.py
"""
The ``pyproject.toml`` parser.
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
from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple, Type, Union

# 3rd party
import toml

__all__ = ["AbstractConfigParser", "BadConfigError", "ProjectParser", "SphinxPyprojectParser", "construct_path"]

TOML_TYPES = Any


class BadConfigError(ValueError):
	"""
	Indicates an error in the ``pyproject.toml`` configuration.
	"""


def construct_path(path: Iterable[str]) -> str:
	"""
	Construct a dotted path to a key.

	:param path: The path elements.
	"""

	return '.'.join([toml.dumps({elem: 0})[:-5] for elem in path])


class AbstractConfigParser(ABC):
	"""
	Abstract base class for TOML configuration parsers.
	"""

	@staticmethod
	def assert_type(
			obj: Any,
			expected_type: Union[Type, Tuple[Type, ...]],
			path: Iterable[str],
			what: str = "type",
			) -> None:
		"""
		Assert that ``obj`` is of type ``expected_type``, otherwise raise an error with a helpful message.

		:param obj: The object to check the type of.
		:param expected_type: The expected type.
		:param path: The elements of the path to ``obj`` in the TOML mapping.
		:param what: What ``obj`` is, e.g. ``'type'``, ``'key type'``, ``'value type'``.

		.. seealso:: :meth:`~.assert_key_type` and :meth:`~.assert_value_type`
		"""

		if not isinstance(obj, expected_type):
			name = construct_path(path)
			raise TypeError(f"Invalid {what} for {name!r}: expected {expected_type!r}, got {type(obj)!r}")

	@staticmethod
	def assert_indexed_type(
			obj: Any,
			expected_type: Union[Type, Tuple[Type, ...]],
			path: Iterable[str],
			idx: int = 0,
			) -> None:
		"""
		Assert that ``obj`` is of type ``expected_type``, otherwise raise an error with a helpful message.

		:param obj: The object to check the type of.
		:param expected_type: The expected type.
		:param path: The elements of the path to ``obj`` in the TOML mapping.
		:param idx: The index of ``obj`` in the array.

		.. seealso:: :meth:`~.assert_type`, :meth:`~.assert_key_type` and :meth:`~.assert_value_type`
		"""

		if not isinstance(obj, expected_type):
			name = construct_path(path) + f"[{idx}]"
			raise TypeError(f"Invalid type for {name!r}: expected {expected_type!r}, got {type(obj)!r}")

	def assert_key_type(
			self,
			obj: Any,
			expected_type: Union[Type, Tuple[Type, ...]],
			path: Iterable[str],
			):
		"""
		Assert that the key ``obj`` is of type ``expected_type``, otherwise raise an error with a helpful message.

		:param obj: The object to check the type of.
		:param expected_type: The expected type.
		:param path: The elements of the path to ``obj`` in the TOML mapping.

		.. seealso:: :meth:`~.assert_type` and :meth:`~.assert_value_type`
		"""

		self.assert_type(obj, expected_type, path, "key type")

	def assert_value_type(
			self,
			obj: Any,
			expected_type: Union[Type, Tuple[Type, ...]],
			path: Iterable[str],
			):
		"""
		Assert that the value ``obj`` is of type ``expected_type``, otherwise raise an error with a helpful message.

		:param obj: The object to check the type of.
		:param expected_type: The expected type.
		:param path: The elements of the path to ``obj`` in the TOML mapping.

		.. seealso:: :meth:`~.assert_type` and :meth:`~.assert_key_type`
		"""

		self.assert_type(obj, expected_type, path, "value type")

	@property
	@abstractmethod
	def keys(self) -> List[str]:
		"""
		The keys to parse from the TOML file.
		"""

		raise NotImplementedError

	def parse(self, config: Dict[str, TOML_TYPES]) -> Dict[str, TOML_TYPES]:
		"""
		Parse the TOML configuration.

		:param config:
		"""

		parsed_config = {}

		for key in self.keys:
			if key not in config:
				# Ignore absent values
				pass

			elif hasattr(self, f"parse_{key.replace('-', '_')}"):
				parsed_config[key] = getattr(self, f"parse_{key.replace('-', '_')}")(config)

			elif key in config:
				parsed_config[key] = config[key]

		return parsed_config


class ProjectParser(AbstractConfigParser):
	"""
	Parser for :pep:`621` metadata from ``pyproject.toml``.
	"""

	def parse_name(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the `name <https://www.python.org/dev/peps/pep-0621/#name>`_ key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		name = config["name"]
		self.assert_type(name, str, ["project", "name"])
		return str(name).replace('_', '-')

	def parse_version(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the `version <https://www.python.org/dev/peps/pep-0621/#version>`_ key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		version = config["version"]
		self.assert_type(version, (str, int), ["project", "version"])
		return str(version)

	def parse_description(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the `description <https://www.python.org/dev/peps/pep-0621/#description>`_ key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		description = config["description"]
		self.assert_type(description, str, ["project", "description"])
		return description

	@staticmethod
	def _parse_authors(config: Dict[str, TOML_TYPES], key_name: str = "authors") -> List[Optional[str]]:
		all_authors: List[Optional[str]] = []

		for idx, author in enumerate(config[key_name]):
			name = author.get("name", None)

			if name is not None and ',' in name:
				raise BadConfigError(f"The 'project.{key_name}[{idx}].name' key cannot contain commas.")

			all_authors.append(name)

		return all_authors

	def parse_authors(self, config: Dict[str, TOML_TYPES]) -> List[Optional[str]]:
		"""
		Parse the `authors <https://www.python.org/dev/peps/pep-0621/#authors-maintainers>`_ key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		return self._parse_authors(config, "authors")

	def parse_maintainers(self, config: Dict[str, TOML_TYPES]) -> List[Optional[str]]:
		"""
		Parse the `authors <https://www.python.org/dev/peps/pep-0621/#authors-maintainers>`_ key.

		:param config: The unparsed TOML config for the ``[project]`` table.
		"""

		return self._parse_authors(config, "maintainers")

	@property
	def keys(self) -> List[str]:
		"""
		The keys to parse from the TOML file.
		"""

		return [
				"name",
				"version",
				"description",
				"authors",
				"maintainers",
				]


class SphinxPyprojectParser(AbstractConfigParser):
	"""
	Parser for the ``tool.sphinx-pyproject`` table in ``pyproject.toml``.
	"""

	_base_path = ("tool", "sphinx-pyproject")

	def _parse_string(
			self,
			config: Dict[str, TOML_TYPES],
			name: str,
			) -> str:
		"""
		Parse a string.

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		:param name: The name of the key to parse.
		"""

		data = config[name]
		self.assert_type(data, str, [*self._base_path, name])
		return str(data)

	def _parse_bool(
			self,
			config: Dict[str, TOML_TYPES],
			name: str,
			) -> bool:
		"""
		Parse a boolean value.

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		:param name: The name of the key to parse.
		"""

		data = config[name]
		self.assert_type(data, bool, [*self._base_path, name])
		return bool(data)

	def _parse_list_of_string(
			self,
			config: Dict[str, TOML_TYPES],
			name: str,
			) -> List[str]:
		"""
		Parse a list of strings.

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		:param name: The name of the key to parse.
		"""

		data = config[name]

		for idx, keyword in enumerate(data):
			self.assert_indexed_type(keyword, str, [*self._base_path, name], idx=idx)

		return data

	def parse_extensions(self, config: Dict[str, TOML_TYPES]) -> List[str]:
		"""
		Parse the ``extensions`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_list_of_string(config, "extensions")

	def parse_source_suffix(self, config: Dict[str, TOML_TYPES]) -> Union[List[str], Dict[str, str]]:
		"""
		Parse the ``source_suffix`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_suffix

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		source_suffix = config["source_suffix"]

		if isinstance(source_suffix, str):
			return [source_suffix]
		elif isinstance(source_suffix, Mapping):
			return dict(source_suffix)
		elif isinstance(source_suffix, Iterable):
			return list(source_suffix)
		else:
			name = construct_path([*self._base_path, "source_suffix"])
			raise TypeError(
					f"Invalid type for {name!r}: expected a string, sequence or mapping, got {type(source_suffix)!r}"
					)

	def parse_source_encoding(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``source_encoding`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_encoding

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "source_encoding")

	# TODO: source_parsers

	def parse_master_doc(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``master_doc`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master_doc

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "master_doc")

	def parse_exclude_patterns(self, config: Dict[str, TOML_TYPES]) -> List[str]:
		"""
		Parse the ``exclude_patterns`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-exclude_patterns

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_list_of_string(config, "exclude_patterns")

	def parse_templates_path(self, config: Dict[str, TOML_TYPES]) -> List[str]:
		"""
		Parse the ``templates_path`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_list_of_string(config, "templates_path")

	def parse_manpages_url(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``manpages_url`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-manpages_url

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "manpages_url")

	def parse_nitpicky(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``nitpicky`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpicky

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "nitpicky")

	def parse_pygments_style(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``pygments_style`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-pygments_style

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "pygments_style")

	def parse_add_function_parentheses(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``add_function_parentheses`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_function_parentheses

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "add_function_parentheses")

	def parse_add_module_names(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``add_module_names`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_module_names

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "add_module_names")

	def parse_show_authors(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``show_authors`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-show_authors

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "show_authors")

	def parse_trim_footnote_reference_space(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``trim_footnote_reference_space`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-trim_footnote_reference_space

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "trim_footnote_reference_space")

	def parse_trim_doctest_flags(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``trim_doctest_flags`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-trim_doctest_flags

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "trim_doctest_flags")

	def parse_strip_signature_backslash(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``strip_signature_backslash`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-strip_signature_backslash

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "strip_signature_backslash")

	def parse_language(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``language`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "language")

	def parse_html_theme(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``html_theme`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "html_theme")

	# TODO: html_theme_options

	def parse_html_logo(self, config: Dict[str, TOML_TYPES]) -> str:
		"""
		Parse the ``html_logo`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_string(config, "html_logo")

	def parse_html_static_path(self, config: Dict[str, TOML_TYPES]) -> List[str]:
		"""
		Parse the ``html_static_path`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_list_of_string(config, "html_static_path")

	def parse_html_show_sourcelink(self, config: Dict[str, TOML_TYPES]) -> bool:
		"""
		Parse the ``html_show_sourcelink`` key.

		.. seealso:: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_show_sourcelink

		:param config: The unparsed TOML config for the ``[tool.sphinx-pyproject]`` table.
		"""

		return self._parse_bool(config, "html_show_sourcelink")

	# TODO: html_context

	@property
	def keys(self) -> List[str]:
		"""
		The keys to parse from the TOML file.
		"""

		return [
				"extensions",
				"source_suffix",
				"source_encoding",
				"source_parsers",
				"master_doc",
				"exclude_patterns",
				"templates_path",
				"manpages_url",
				"nitpicky",
				"pygments_style",
				"add_function_parentheses",
				"add_module_names",
				"show_authors",
				"trim_footnote_reference_space",
				"trim_doctest_flags",
				"strip_signature_backslash",
				"language",
				"html_theme",
				"html_theme_options",
				"html_logo",
				"html_static_path",
				"html_show_sourcelink",
				"html_context",
				]
