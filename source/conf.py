# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Orquesta's Python SDK"
copyright = "2023, orquesta"
author = "orquesta"

import os
import sys

sys.path.insert(0, os.path.abspath("../orquesta_sdk"))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Include documentation from docstrings
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.napoleon",  # Support for Google-style docstrings
]

templates_path = ["_templates"]
exclude_patterns = []

autodoc_default_options = {
    "member-order": "bysource",
    "special-members": "__init__",
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# The master toctree document.
master_doc = "index"

# The short X.Y version.
version = "2.0"

release = "2.0.0"
language = "en"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
