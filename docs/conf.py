# -*- coding: utf-8 -*-

# -- Project information -----------------------------------------------------

project = "Sphinx Global-TOC"
copyright = "2018, Chris Holdgraf"
author = "Chris Holdgraf"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_globaltoc", "myst_parser", "myst_nb"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
globaltoc_path = "toc.yml"
