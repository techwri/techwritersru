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

"""
Нужный уровень логирования (DEBUG, INFO, ERROR и т. д.).
"""
logger.setLevel(logging.DEBUG)


project = "Techwriters.ru"
copyright = "2005-2023, Сайт технических писателей - Techwriters.ru, "
author = "Evgeny Zakharenko (info@techwriters.ru)"
release = "ver. 1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx_tabs.tabs",
    "sphinx.ext.graphviz",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.googleanalytics",
]
plantuml_output_format = "png"

templates_path = ["_templates"]
exclude_patterns = []
languages = ["ru", "en"]  # Список поддерживаемых языков
gettext_auto_build = False  # Отключает автоматическую генерацию локализации для темы sphinx_book_theme

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# -- Options for Sphinx Book Theme ------------------------------------------

html_theme = "sphinx_book_theme"  # используемая тема сайта
html_title = "TechWriters.ru"  # название сайта
html_static_path = ["_static"]  # путь к статичным файлам
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
    "use_sidenotes": True,  # подключение отображение блоков в тексте https://sphinx-book-theme.readthedocs.io/en/stable/content/content-blocks.html#activate-sidenotes-and-marginnotes
}

# Google analytics
googleanalytics_id = "G-XTLRDH4VHT"

# Параметры проверки ссылок)
linkcheck_ignore = [
    r"http://127.0.0.1:\d+/",
    r"https://apiary\.io/",
    r"https://linkedin\.com/",
    r"https://www\.linkedin\.com",
    r"https://www\.pluralsight\.com/courses/technical-writing-software-documentation",
]

linkcheck_allowed_redirects = {
    r"https://yadi\.sk/[i/]*.*": r"https://disk\.yandex\.[ru|com]*/[i/]*.*",
    r"https://yadi\.sk/.*": r"https://yadi\.sk/showcaptcha.*",
    r"https://youtu\.be/.*": r"https://www\.youtube\.com/.*",
}

linkcheck_timeout = 30  # seconds
