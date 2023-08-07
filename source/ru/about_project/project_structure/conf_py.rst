.. _configuration:

=========================
Файл конфигурации conf.py
=========================

Файл `conf.py` является главным файлом конфигурации для проекта документации Sphinx. В этом файле вы можете настроить различные параметры и настройки, влияющие на генерацию и отображение вашей документации.

Проект и базовая информация
---------------------------

.. code-block:: python

   project = 'Название вашего проекта'
   author = 'Ваше имя или организация'
   copyright = 'Защита авторских прав'

Пути и директории
------------------

.. code-block:: python

   source_suffix = '.rst'
   master_doc = 'index'
   exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

Оформление и темы
------------------

.. code-block:: python

   html_theme = 'default'
   html_theme_options = {}

Содержание, оглавление и перекрестные ссылки
------------------------------------------

.. code-block:: python

   autodoc_default_options = {
       'members': True,
       'undoc-members': True,
   }
   autodoc_mock_imports = ['numpy']

Язык и локализация
-------------------

.. code-block:: python

   language = 'ru'
   locale_dirs = ['locale/']

Ссылки и расширения
--------------------

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.intersphinx',
   ]

Ссылки и внешние ресурсы
-------------------------

.. code-block:: python

   intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

Исходники и структура
----------------------

.. code-block:: python

   source_encoding = 'utf-8'
   nitpicky = True


.. TODO: актуализировать после разработки