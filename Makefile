# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile build run clean

# Добавленное правило для сборки HTML документации
html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Добавленное правило для сборки Docker-образа
build:
	docker build -t "$(shell basename "$(CURDIR)" | tr '[:upper:]' '[:lower:]')" .

# Добавленное правило для запуска контейнера
run:
	docker run -d -p 8000:80 --name "$(shell basename "$(CURDIR)" | tr '[:upper:]' '[:lower:]')" "$(shell basename "$(CURDIR)" | tr '[:upper:]' '[:lower:]')"

# Добавленное правило для остановки и удаления контейнера
clean:
	docker stop "$(shell basename "$(CURDIR)" | tr '[:upper:]' '[:lower:]')"
	docker rm "$(shell basename "$(CURDIR)" | tr '[:upper:]' '[:lower:]')"
