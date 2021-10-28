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
	@poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
run2:
	@poetry run gendiff tests/fixtures/file3.json tests/fixtures/file4.json
run3:
	@poetry run gendiff tests/fixtures/file5.json tests/fixtures/file6.json
run4:
	@poetry run gendiff --format plain tests/fixtures/file1.json tests/fixtures/file2.json
run5:
	@poetry run gendiff --format plain tests/fixtures/file3.json tests/fixtures/file4.json
run6:
	@poetry run gendiff --format json tests/fixtures/file3.json tests/fixtures/file4.json
run2.1:
	@poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml
run2.2:
	@poetry run gendiff tests/fixtures/file3.yaml tests/fixtures/file4.yaml
run2.3:
	@poetry run gendiff --format plain tests/fixtures/file3.yaml tests/fixtures/file4.yaml
run3.1:
	@poetry run gendiff tests/fixtures/file3.json tests/fixtures/file7.json
run4.1:
	@poetry run gendiff tests/fixtures/hexlet_fixtures/file10.yml tests/fixtures/hexlet_fixtures/file11.yml
run4.2:
	@poetry run gendiff --format plain tests/hexlet_fixtures/file10.yml tests/hexlet_fixtures/file11.yml
run5.1:
	@poetry run gendiff tests/hexlet_fixtures/file10.json tests/hexlet_fixtures/file11.json
run5.2:
	@poetry run gendiff --format plain tests/hexlet_fixtures/file10.json tests/hexlet_fixtures/file11.json