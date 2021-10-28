from gen_diff.utils.functions import is_dict, is_have_stat, return_status, check_type


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


def test_check_type():
    assert check_type({"key": "value"}) == "[complex value]"
