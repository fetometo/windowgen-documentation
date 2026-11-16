# Translations

English (`docs/source/*.rst`) is the source. Translations are in
`docs/source/locale/<lang>/LC_MESSAGES/<page>.po`: French (fr), Italian (it),
Russian (ru), Spanish (es) and German (de).

UI labels of WindowGen and Blender (**Add Window**, *Random Type*, Edit Mode, ...)
are kept in English on purpose, so they match the interface and the screenshots.

## After editing the English pages

```bash
pip install sphinx-intl
sphinx-build -b gettext docs/source docs/build/gettext
sphinx-intl update -p docs/build/gettext -d docs/source/locale -l fr -l it -l ru -l es -l de
```

Changed sentences become empty or `#, fuzzy` entries in the .po files. Translate those,
remove the `fuzzy` flag, and commit. Untranslated sentences show in English.

## Check a language locally

```bash
sphinx-build -W -D language=de -b html docs/source docs/build/de
```

## Read the Docs

Each language is its own Read the Docs project built from this same repository,
with **Language** set in its settings. The English project lists them under
**Settings > Translations**, which adds the language switcher.
