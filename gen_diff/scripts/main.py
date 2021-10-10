import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


def generate_diff(first_file, second_file):
    this_directory = os.getcwd()
    example_path = os.path.join(this_directory, first_file)
    compared_path = os.path.join(this_directory, second_file)

    example = json.load(open(example_path))
    compared = json.load(open(compared_path))

    example_keys = set(example.keys())
    compared_keys = set(compared.keys())
    keys = sorted(example_keys.union(compared_keys))

    result = '{\n'

    for key in keys:
        if key in example_keys and key in compared_keys:
            result += find_differences(key, example, compared)

        elif key in example_keys:
            result += beauty_string(key, example[key], 'remove')

        else:
            result += beauty_string(key, compared[key], 'add')

    result += '}'
    return result


def find_differences(key, dict_a, dict_b):
    if dict_a[key] == dict_b[key]:
        return beauty_string(key, dict_a[key])
    else:
        return beauty_string(key, dict_a[key], 'remove') + beauty_string(key, dict_b[key], 'add')


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
