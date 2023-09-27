# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
IMAGE         = techwriters
DOCKER_BUILD  = docker run --rm --volume $(shell pwd):/docs $(IMAGE)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build Docker image
docker-build:
	docker build-image \
		--tag techwriters \
		.

docker-build-dirhtml:
	$(DOCKER_BUILD) make dirhtml

docker-build-html:
	$(DOCKER_BUILD) make html

docker-build-linkcheck:
	$(DOCKER_BUILD) make linkcheck


server:
	python3 -m http.server -d build/html -b 127.0.0.1 8080
