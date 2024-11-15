# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # For Python <3.11, install `tomli`.

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Fetch version dynamically from pyproject.toml
pyproject_path = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")

with open(pyproject_path, "rb") as f:
    config = tomllib.load(f)

project = config["project"]["name"]
author = config["project"]["authors"][0]["name"]
release = config["project"]["version"]

copyright = (
    f"2024, {author}. Licensed under the "
    "GNU General Public License v3.0. See https://www.gnu.org/licenses/gpl-3.0.html for details."
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = []
