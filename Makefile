VERSION = 0.1.0

PACKAGE = brigid-api-client

clean:
	rm -rf *.tar.gz dist build *.egg-info *.rpm
	find . -name "*.pyc" | xargs rm
	find . -name "__pycache__" | xargs rm -rf

version:
	@echo $(VERSION)

dist: clean
	@python setup.py sdist
	@python setup.py bdist_wheel --universal

pypi: dist
	@twine upload dist/*

tox:
	@tox

