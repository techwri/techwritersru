# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import logging

# Configure logging to stdout
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  # нужный уровень логирования (DEBUG, INFO, ERROR и т.д.)


project = 'Techwriters.ru'
copyright = '2005-2023, Сайт технических писателей - Techwriters.ru, '
author = 'Evgeny Zakharenko (info@techwriters.ru)'
release = 'ver. 1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx_tabs.tabs',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
]
plantuml = 'java -jar /app/plantuml.jar'   #  путь для сборки в github actions,  для сборки в докере изменить на  plantuml = 'java -jar /app/plantuml.jar'
plantuml_output_format = 'png'

templates_path = ['_templates']
exclude_patterns = []
languages = ['ru', 'en']  # Список поддерживаемых языков

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# -- Options for Sphinx Book Theme ------------------------------------------

html_theme = 'sphinx_book_theme'  # используемая тема сайта
html_title = "TechWriters.ru"  # название сайта
html_static_path = ['source/_static']  # путь к статичным файлам
html_css_files = ["custom.css"]  # путь к костомизированным файлам стиля


html_theme_options = {
    "repository_url": "https://github.com/techwri/techwritersweb",
    "use_source_button": True,
    "repository_branch": "develop",
    "path_to_docs": "source",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "announcement": "Чат технических писателей - https://t.me/twriters",
    "extra_footer": "Чат технических писателей - https://t.me/twriters",
    "use_sidenotes": True,   # подключение отображение блоков в тексте https://sphinx-book-theme.readthedocs.io/en/stable/content/content-blocks.html#activate-sidenotes-and-marginnotes
}

# Google analytics
def setup(app):
    app.add_js_file("google-analytics.js")


