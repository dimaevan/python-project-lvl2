from gen_diff.main import generate_diff, open_file
from .fixtures.fixtures import *
from gen_diff.utils.functions import is_dict, is_have_stat, return_status


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


def test_plain():
    """ Test big data dict with plain formatter """
    file1 = open_file('tests/fixtures/file3.json')
    file2 = open_file('tests/fixtures/file4.json')
    out = generate_diff(file1, file2, 'plain')
    assert out == plain_format


def test_is_dict():
    assert is_dict({})
    assert not is_dict('')
    assert not is_dict(1)


def test_is_have_status():
    assert is_have_stat({'status': '1'})
    assert is_have_stat({""}) is False


def test_return_status():
    test_dict = {'status': ''}
    test_dict_2 = {'status': 0}
    assert return_status(None) is None
    assert return_status(test_dict) == ''
    assert return_status(test_dict_2) == 0
