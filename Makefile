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
	@poetry run pytest
run-test:
	@poetry run gendiff file1.json file2.json