# Configuration file for the Sphinx documentation builder.



# -- Project information

project = 'WindowGen'
copyright = '2026, Mikhail Shevchenko'
author = 'Mikhail Shevchenko'

release = '4.0'
version = '4.0.0'

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

# -- Translations
# English is the source. Translations live in locale/<lang>/LC_MESSAGES/<page>.po,
# one file per page. Read the Docs builds each language from its own project
# (set to that language), which passes -D language=<lang> to Sphinx.
# To refresh after editing the English pages:
#   sphinx-build -b gettext docs/source docs/build/gettext
#   sphinx-intl update -p docs/build/gettext -d docs/source/locale -l fr -l it -l ru -l es -l de
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False
gettext_uuid = False

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output

html_theme = 'press'

globaltoc_maxdepth = -1

# -- Options for EPUB output

epub_show_urls = 'footnote'
