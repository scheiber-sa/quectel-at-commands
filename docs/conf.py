# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import configparser

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

copyright = copyright = (
    "2024, Pierre Godicheau. Licensed under the "
    "GNU General Public License v3.0. See https://www.gnu.org/licenses/gpl-3.0.html for details."
)

# Fetch version dynamically from setup.cfg
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "setup.cfg"))
project = config["metadata"]["name"]
author = config["metadata"]["author"]
release = config["metadata"]["version"]

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
