from gen_diff.scripts.main import generate_diff, check_file_type


def testing_json():
    out = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    with open('tests/fixtures/output.txt', 'r') as output:
        x = output.read()
    assert out == x


def testing_yaml():
    out = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    with open('tests/fixtures/output.txt', 'r') as output:
        x = output.read()
    assert out == x


def test_check_test_file():
    for x in ['*.json', '1.json', '_.json']:
        assert 'json' == check_file_type(x)
    for x in ['*.yaml', '1.yaml', '_.yaml']:
        assert 'yaml' == check_file_type(x)

