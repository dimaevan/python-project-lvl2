from gen_diff.scripts.main import generate_diff
from .fixtures.fixtures import *
from gen_diff.scripts.utils.functions import is_dict, is_have_stat, return_status


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
