from gendiff import generate_diff


def test_yaml_stylish():
    file1 = 'tests/hexlet_fixtures/file10.yml'
    file2 = 'tests/hexlet_fixtures/file11.yml'
    with open("tests/hexlet_fixtures/result_stylish", "r") as file:
        result = file.read()
    assert generate_diff(file1, file2, 'stylish') == result


def test_yaml_plain():
    file1 = 'tests/hexlet_fixtures/file10.yml'
    file2 = 'tests/hexlet_fixtures/file11.yml'
    with open("tests/hexlet_fixtures/result_plain", "r") as file:
        result = file.read()
    assert generate_diff(file1, file2, 'plain') == result
