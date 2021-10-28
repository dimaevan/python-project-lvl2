#!/usr/bin/env python

from gen_diff.main import generate_diff as gen, open_file as of


def generate_diff(file1, file2, style='stylish'):
    """  Shell   """
    return gen(of(file1), of(file2), style)
