from gen_diff.scripts.main import generate_diff


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

