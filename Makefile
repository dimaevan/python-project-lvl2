run:
	@poetry run gendiff
run-help:
	@poetry run gendiff -h
install:
	@poetry install
lint:
	@poetry run flake8 gen_diff
build:
	@poetry build
test:
	@poetry run pytest -v
run-test:
	@poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json