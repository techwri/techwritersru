# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Techwriters.ru'
copyright = '2005-2023, Евгений Захаренко, Сайт для технических писателей - Techwriters.ru'
author = 'Евгений Захаренко, Techwriters.ru'
release = 'ver. 1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

languages = ['en', 'ru']  # Список поддерживаемых языков

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = "TechWriters.ru"  # название сайта

# -- Options for Sphinx Book Theme ------------------------------------------
# Добавьте настройки кнопок прямо в conf.py
html_theme_options = {
    "repository_url": "https://github.com/techwri/techwritersweb",
    "repository_branch": "develop",  # Или ветка, которую вы используете
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_download_button": True,
}

html_context = {
    "display_github": True,
    "github_user": "techwri",
    "github_repo": "techwritersweb",
    "github_version": "develop",  # Или ветка, которую вы используете
    "conf_py_path": "/source/",  # Путь к директории, содержащей файл conf.py относительно корня репозитория
}
