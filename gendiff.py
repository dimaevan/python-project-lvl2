#!/usr/bin/env python

from gen_diff.main import generate_diff as gen, open_file as of


def generate_diff(file1, file2):
    """  Shell   """
    return gen(of(file1), of(file2))


# from gendiff import generate_diff
# generate_diff("/home/dimaevan/Study/Python/python-project-lvl2/tests/fixtures/file1.json","/home/dimaevan/Study/Python/python-project-lvl2/tests/fixtures/file2.json")
