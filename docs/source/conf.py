# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "WhiFuN"
copyright = "2025, Jain et. al"
author = "Pratik Jain"

release = "3.3"
version = "3.3.1"

# -- General configuration

extensions = [
    "myst_parser",
    "sphinx.ext.mathjax",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
]

myst_heading_anchors = 4


templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "api.rst",
    "functional_networks.rst",
    "getting_started.rst",
    "preprocessing_and_qc.rst",
    "scripting.rst",
    "setup.rst",
    "visualization.rst",
    "architecture.md",
    "anomalies.md",
]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# -- Options for EPUB output
epub_show_urls = "footnote"
