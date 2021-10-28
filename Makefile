run:
	@poetry run gendiff
run-help:
	@poetry run gendiff -h
install:
	@poetry install
package-install:
	python -m pip install  dist/*.whl --force-reinstall
lint:
	@poetry run flake8 gen_diff
build:
	@poetry build
test:
	@poetry run pytest -vv
check:
	make lint & make test
run1:
	@poetry run gendiff tests/fixtures/simple/file1.json tests/fixtures/simple/file2.json
run2:
	@poetry run gendiff tests/fixtures/complicated/file3.json tests/fixtures/complicated/file4.json

