PYPKG := nplot
TESTS := $(wildcard ./examples/*.py)

.SUFFIXES:
.PHONY: help install clean count test

help:
	@echo "options are: install clean"

install:
	python3 setup.py install --user

clean:
	rm -rf build dist $(PYPKG).egg-info $(PYPKG)/*.pyc $(PYPKG)/__pycache__ *.png

count:
	@wc $(PYPKG)/*.py | sort -n -k1
	@echo "files : "$(shell echo $(PYPKG)/*.py | wc -w)
	@echo "commits : "$(shell git rev-list HEAD --count) 

test:
	@for script in $(TESTS); do \
		echo "Running $$script..."; \
		PYTHONPATH=. ./$$script; \
	done
