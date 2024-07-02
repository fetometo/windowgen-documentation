# Configuration file for the Sphinx documentation builder.



# -- Project information

project = 'WindowGen'
copyright = '2024, Mikhail Shevchenko'
author = 'Mikhail Shevchenko'

release = '2.0'
version = '2.0.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgconverter',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output

html_theme = 'press'

globaltoc_maxdepth = -1

# -- Options for EPUB output

epub_show_urls = 'footnote'
