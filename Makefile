run:
	@poetry run gendiff
run-help:
	@poetry run gendiff -h
install:
	@poetry install
package-install:
	python -m pip install  dist/*.whl --force-reinstall
lint:
	@poetry run flake8
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
run3:
	@poetry run gendiff tests/fixtures/simple/file1.yaml tests/fixtures/simple/file2.yaml
run4:
	@poetry run gendiff tests/fixtures/complicated/file3.yaml tests/fixtures/complicated/file4.yaml
run5:
	@poetry run gendiff tests/hexlet_fixtures/file10.json tests/hexlet_fixtures/file11.json
run6:
	@poetry run gendiff -f plain tests/hexlet_fixtures/file10.json tests/hexlet_fixtures/file11.json
run7:
	@poetry run gendiff tests/hexlet_fixtures/file10.yml tests/hexlet_fixtures/file11.yml
run8:
	@poetry run gendiff -f plain tests/hexlet_fixtures/file10.yml tests/hexlet_fixtures/file11.yml
