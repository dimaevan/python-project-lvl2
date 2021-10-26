from gen_diff.scripts.main import generate_diff
from .fixtures.fixtures import *


def testing_json():
    out = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert out == simple_dict


def testing_yaml():
    out = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert out == simple_dict


def test_recursive_dict_json():
    out = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json')
    assert out == big_dict


def test_recursive_dict_yaml():
    out = generate_diff('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml')
    assert out == big_dict


def test_plain():
    """ Test big data dict with plain formatter """
    out = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json', "plain")
    assert out == plain_format
