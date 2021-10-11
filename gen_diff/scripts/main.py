import argparse
import json
import os
import yaml


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--format', help='set format of output')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    this_directory = os.getcwd()
    first_file_path = os.path.join(this_directory, first_file)
    second_file_path = os.path.join(this_directory, second_file)
    print(generate_diff(first_file_path, second_file_path))


def generate_diff(first_file, second_file):
    if check_file_type(first_file) == 'json':
        example = json.load(open(first_file))
        compared = json.load(open(second_file))
    else:
        example = yaml.safe_load(open(first_file))
        compared = yaml.safe_load(open(second_file))

    return parsing(example, compared)


def parsing(obj1, obj2):
    example_keys = set(obj1.keys())
    compared_keys = set(obj2.keys())
    keys = sorted(example_keys.union(compared_keys))

    result = '{\n'
    for key in keys:
        if key in example_keys and key in compared_keys:
            result += find_differences(key, obj1, obj2)
        elif key in example_keys:
            result += beauty_string(key, obj1[key], 'remove')
        else:
            result += beauty_string(key, obj2[key], 'add')
    result += '}'
    return result


def check_file_type(file):
    word = str(file)
    if word.endswith('.json'):
        return 'json'
    elif word.endswith('.yaml'):
        return 'yaml'
    else:
        raise TypeError


def find_differences(key, dict_a, dict_b):
    if dict_a[key] == dict_b[key]:
        return beauty_string(key, dict_a[key])
    else:
        start = beauty_string(key, dict_a[key], 'remove')
        end = beauty_string(key, dict_b[key], 'add')
        return start + end


def beauty_string(key, value, method=''):
    space = ' ' * 4
    place_holder = ' ' * 2
    if method == 'remove':
        place_holder = '- '
    elif method == 'add':
        place_holder = '+ '
    return f"{space}{place_holder}{key}: {value} \n"


if __name__ == '__main__':
    main()
