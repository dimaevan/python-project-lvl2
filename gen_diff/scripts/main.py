import argparse
import json
import os
import yaml


def main():
    # Args parser
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--format', help='set format of output')
    args = parser.parse_args()
    # Неправильный ход мысли, исправить
    first_file = os.path.join(os.getcwd(), args.first_file)
    second_file = os.path.join(os.getcwd(), args.second_file)
    # Проверка расширения файла, добавить для двух
    extend = str(args.first_file).split('.')[-1]

    if extend == 'json':
        example = json.load(open(first_file))
        compared = json.load(open(second_file))
    else:
        example = yaml.safe_load(open(first_file))
        compared = yaml.safe_load(open(second_file))

    print(generate_diff(example, compared))


def generate_diff(obj1, obj2):
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


def find_differences(key, dict_a, dict_b):
    if dict_a[key] == dict_b[key]:
        return beauty_string(key, dict_a[key])
    else:
        if isinstance(dict_a[key], dict) and isinstance(dict_b[key], dict):
            return generate_diff(dict_a[key], dict_b[key])
        else:
            start = beauty_string(key, dict_a[key], 'remove')
            end = beauty_string(key, dict_b[key], 'add')
            return start + end


def beauty_string(key, value, method=''):
    place_holder = '  '
    if method == 'remove':
        place_holder = '- '
    elif method == 'add':
        place_holder = '+ '
    return f"    {place_holder}{key}: {value} \n"


if __name__ == '__main__':
    main()
