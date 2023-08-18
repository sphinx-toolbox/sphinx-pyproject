# stdlib
import textwrap
from typing import Any, Dict

# 3rd party
import pytest
from coincidence.regressions import AdvancedDataRegressionFixture
from dom_toml.parser import BadConfigError
from domdf_python_tools.paths import PathPlus

# this package
from sphinx_pyproject import SphinxConfig, __version__

root_dir = PathPlus(__file__).parent.parent


def test_parse_our_config(advanced_data_regression: AdvancedDataRegressionFixture):
	globalns: Dict[str, Any] = {}

	config = SphinxConfig(root_dir / "pyproject.toml", globalns=globalns)

	assert config.name == "sphinx-pyproject"
	assert config.author == "Dominic Davis-Foster"
	assert config.version == __version__
	assert config.description == "Move some of your Sphinx configuration into pyproject.toml"

	assert config["language"] == "en"
	assert config["package_root"] == "sphinx_pyproject"
	assert config["github_repository"] == "sphinx-pyproject"
	assert config["sphinxemoji_style"] == "twemoji"
	assert config["templates_path"] == ["_templates"]
	assert config["add_module_names"] is False
	assert "html_theme_options" not in config

	advanced_data_regression.check(globalns)


MINIMUM = """\
[project]
name = 'foo'
version = '1.2.3'
description = 'Description'

[[project.authors]]
name = "Dominic Davis-Foster"
"""

MAINTAINERS = """\
[project]
name = 'foo'
version = '1.2.3'
description = 'Description'

[[project.maintainers]]
name = "Dominic Davis-Foster"
"""

MULTIPLE_KEYS = f"""\
{MINIMUM}
[tool.sphinx-pyproject]
html_show_sourcelink = true
language = 'en'
extensions = ['sphinx-toolbox']
github_repository = 'repo'
"""


@pytest.mark.parametrize(
		"config, size",
		[
				pytest.param(MINIMUM, 0, id="minimum"),
				pytest.param(MAINTAINERS, 0, id="maintainers"),
				pytest.param(
						f"{MINIMUM}\n[tool.sphinx-pyproject]\ngithub_username = 'username'",
						1,
						id="github_username"
						),
				pytest.param(
						f"{MINIMUM}\n[tool.sphinx-pyproject]\ngithub_repository = 'repo'",
						1,
						id="github_repository"
						),
				pytest.param(f"{MINIMUM}\n[tool.sphinx-pyproject]\nlanguage = 'en'", 1, id="language"),
				pytest.param(
						f"{MINIMUM}\n[tool.sphinx-pyproject]\nextensions = ['sphinx-toolbox']", 1, id="extensions"
						),
				pytest.param(
						f"{MINIMUM}\n[tool.sphinx-pyproject]\nhtml_show_sourcelink = true",
						1,
						id="html_show_sourcelink"
						),
				pytest.param(MULTIPLE_KEYS, 4, id="multiple_keys"),
				]
		)
def test_parse_config(
		tmp_pathplus: PathPlus,
		config: str,
		size: int,
		advanced_data_regression: AdvancedDataRegressionFixture,
		):
	(tmp_pathplus / "pyproject.toml").write_text(config)

	loaded_config = SphinxConfig(tmp_pathplus / "pyproject.toml")
	advanced_data_regression.check(loaded_config)
	assert len(loaded_config) == size


def test_empty_config(tmp_pathplus: PathPlus):
	(tmp_pathplus / "pyproject.toml").touch()

	with pytest.raises(BadConfigError, match="No 'project' table found in .*"):
		SphinxConfig(tmp_pathplus / "pyproject.toml")


def test_empty_authors(tmp_pathplus: PathPlus):
	minimum = "[project]\nname = 'foo'\nversion = '1.2.3'\ndescription = 'Description'"

	(tmp_pathplus / "pyproject.toml").write_text(f"{minimum}\n[[project.authors]]\nemail = 'bob@example.com'")

	with pytest.raises(BadConfigError, match="The 'project.authors' key cannot be empty."):
		SphinxConfig(tmp_pathplus / "pyproject.toml")


def test_authors_commas(tmp_pathplus: PathPlus):
	minimum = "[project]\nname = 'foo'\nversion = '1.2.3'\ndescription = 'Description'"

	(tmp_pathplus / "pyproject.toml").write_text(f"{minimum}\n[[project.authors]]\nname = 'Bob, Alice and Claire'")

	with pytest.raises(BadConfigError, match=r"The 'project.authors\[0\].name' key cannot contain commas."):
		SphinxConfig(tmp_pathplus / "pyproject.toml")


@pytest.mark.parametrize(
		"config",
		[
				pytest.param("[project]", id="empty_project"),
				pytest.param("[project]\n", id="name_only"),
				pytest.param("[project]\nversion = '1.2.3'", id="version_only"),
				pytest.param("[project]\ndescription = 'Description'", id="description_only"),
				pytest.param("[project]\nname = 'foo'\ndescription = 'Description'", id="name_description"),
				pytest.param("[project]\nname = 'foo'\nversion = '1.2.3'", id="name_description"),
				pytest.param(
						"[project]\nname = 'foo'\nversion = '1.2.3'\ndescription = 'Description'", id="no_authors"
						),
				]
		)
def test_missing_keys(tmp_pathplus: PathPlus, config: str):
	(tmp_pathplus / "pyproject.toml").write_text(config)

	err = (
			"Either '.*' was not declared in the 'project' table "
			"or it was marked as 'dynamic', which is unsupported by 'sphinx-pyproject'."
			)

	with pytest.raises(BadConfigError, match=err):
		SphinxConfig(tmp_pathplus / "pyproject.toml")


POETRY_AUTHORS = """
[tool.poetry]
name = 'foo'
version = '1.2.3'
description = 'desc'
authors = ["Person <example@email.com>"]
"""

POETRY_MAINTAINERS = """
[tool.poetry]
name = 'foo'
version = '1.2.3'
description = 'desc'
maintainers = ["Person <example@email.com>"]
"""


@pytest.mark.parametrize(
		"toml", [
				pytest.param(POETRY_AUTHORS, id="authors"),
				pytest.param(POETRY_MAINTAINERS, id="maintainers"),
				]
		)
def test_poetry(tmp_pathplus: PathPlus, toml: str):
	(tmp_pathplus / "pyproject.toml").write_text(toml)

	config = SphinxConfig(tmp_pathplus / "pyproject.toml", style="poetry")
	assert config.name == "foo"
	assert config.version == "1.2.3"
	assert config.author == "Person"
	assert config.description == "desc"


def test_poetry_missing_heading(tmp_pathplus: PathPlus):
	toml = textwrap.dedent("""
		[other.table]
		name = 'foo'
		""")

	(tmp_pathplus / "pyproject.toml").write_text(toml)

	err = "No 'tool.poetry' table found in"
	with pytest.raises(BadConfigError, match=err):
		SphinxConfig(tmp_pathplus / "pyproject.toml", style="poetry")


def test_invalid_style(tmp_pathplus: PathPlus):
	(tmp_pathplus / "pyproject.toml").write_text('')

	err = "'style' argument must be one of: pep621, poetry"
	with pytest.raises(ValueError, match=err):
		SphinxConfig(tmp_pathplus / "pyproject.toml", style="other")
