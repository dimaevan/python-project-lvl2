# from gen_diff.main import generate_diff, open_file
#
#
# def test_json_stylish():
#     file1 = open_file('../tests/fixtures/hexlet_fixtures/file10.json')
#     file2 = open_file('../tests/fixtures/hexlet_fixtures/file11.json')
#     res = generate_diff(file1, file2)
#     with open("../tests/fixtures/hexlet_fixtures/result_stylish", "r") as file:
#         result = file.read()
#     assert res == result
#
#
# def test_json_plain():
#     file1 = open_file('../tests/fixtures/hexlet_fixtures/file10.json')
#     file2 = open_file('../tests/fixtures/hexlet_fixtures/file11.json')
#     res = generate_diff(file1, file2, 'plain')
#     with open("../tests/fixtures/hexlet_fixtures/result_plain", "r") as file:
#         result = file.read()
#     assert res == result
#
#
# def test_yaml_stylish():
#     file1 = open_file('../tests/fixtures/hexlet_fixtures/file10.yml')
#     file2 = open_file('../tests/fixtures/hexlet_fixtures/file11.yml')
#     res = generate_diff(file1, file2)
#     with open("../tests/fixtures/hexlet_fixtures/result_stylish", "r") as file:
#         result = file.read()
#     assert res == result
#
#
# def test_yaml_plain():
#     file1 = open_file('../tests/fixtures/hexlet_fixtures/file10.yml')
#     file2 = open_file('../tests/fixtures/hexlet_fixtures/file11.yml')
#     res1 = generate_diff(file1, file2, 'plain')
#     with open("../tests/fixtures/hexlet_fixtures/result_plain", "r") as file:
#         result = file.read()
#     assert res1 == result
