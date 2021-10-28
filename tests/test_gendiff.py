from gen_diff.main import generate_diff, open_file
from tests.fixtures.fixtures import *


def testing_json():
    file1 = open_file('tests/fixtures/file1.json')
    file2 = open_file('tests/fixtures/file2.json')
    out = generate_diff(file1, file2)
    assert out == simple_dict


def testing_yaml():
    file1 = open_file('tests/fixtures/file1.yaml')
    file2 = open_file('tests/fixtures/file2.yaml')
    out = generate_diff(file1, file2)
    assert out == simple_dict


def test_recursive_dict_json():
    file1 = open_file('tests/fixtures/file3.json')
    file2 = open_file('tests/fixtures/file4.json')
    out = generate_diff(file1, file2)
    assert out == big_dict


def test_recursive_dict_yaml():
    file1 = open_file('tests/fixtures/file3.yaml')
    file2 = open_file('tests/fixtures/file4.yaml')
    out = generate_diff(file1, file2)
    assert out == big_dict

