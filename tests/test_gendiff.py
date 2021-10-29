from gen_diff.main import generate_diff, open_file

with open('tests/fixtures/simple/out.txt') as file:
    result = file.read()
with open('tests/fixtures/complicated/out.txt') as file:
    result_big = file.read()


def testing_json():
    file1 = 'tests/fixtures/simple/file1.json'
    file2 = 'tests/fixtures/simple/file2.json'
    assert generate_diff(file1, file2) == result


def testing_yaml():
    file1 = 'tests/fixtures/simple/file1.yaml'
    file2 = 'tests/fixtures/simple/file2.yaml'
    assert generate_diff(file1, file2) == result


def test_complicated_dict_json():
    file1 = 'tests/fixtures/complicated/file3.json'
    file2 = 'tests/fixtures/complicated/file4.json'
    assert generate_diff(file1, file2) == result_big


def test_complicated_dict_yaml():
    file1 = 'tests/fixtures/complicated/file3.yaml'
    file2 = 'tests/fixtures/complicated/file4.yaml'
    assert generate_diff(file1, file2, ) == result_big

