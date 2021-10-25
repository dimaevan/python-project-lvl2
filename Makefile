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
	@poetry run pytest -vv
run1:
	@poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
run2:
	@poetry run gendiff tests/fixtures/file3.json tests/fixtures/file4.json
run3:
	@poetry run gendiff tests/fixtures/file5.json tests/fixtures/file6.json