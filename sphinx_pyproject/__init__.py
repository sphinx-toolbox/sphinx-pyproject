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

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.0.0"
__email__: str = "dominic@davis-foster.co.uk"
