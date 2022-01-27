develop: 
	python -m pip install -e .[dev] --upgrade --upgrade-strategy eager --

pre-commit: 
	pre-commit install

pre-commit-update:
	pre-commit autoupdate

install:
	python -m pip install . --upgrade --upgrade-strategy eager

code-format: pre-commit-update
	pre-commit run yapf --all-files

code-lint: pre-commit-update
	pre-commit run flake8 --all-files

code-typing:
	mypy --pretty xyz

test::
	python -m pytest --exitfirst

test-cov::
	python -m pytest --cov=xyz  --exitfirst -vv --cov-report=xml

mdformat: pre-commit-update
	pre-commit run mdformat --all-files

docs-validate::
	mkdocs build -c -s
	rm -rf site

docs-serve:
	mkdocs serve
