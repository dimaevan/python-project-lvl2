from gen_diff.scripts.main import generate_diff


def testing():
    out = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    with open('tests/fixtures/output.txt', 'r') as output:
        x = output.read()
    assert out == x
