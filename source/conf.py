# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ReadTheDocs_tutorial documentation'
copyright = '2025, Toto'
author = 'Toto'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

suppress_warnings = [
    "toc.duplicate",  # Supprime les doublons dans le sommaire
    "toc.excluded",   # Optionnel : supprime les avertissements de fichiers exclus
]

#highlight_language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 2,      # profondeur d’affichage de la table des matières
    'collapse_navigation': False,
    'titles_only': False,
}
html_static_path = ['_static']
