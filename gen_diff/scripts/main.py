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
    return formatter(make_diff(obj1, obj2))


def make_diff(el1, el2):
    result = {}
    if isinstance(el1, dict) and isinstance(el2, dict):
        keys_one = set(el1.keys())
        keys_two = set(el2.keys())

        children = sorted(keys_one.union(keys_two))

        for key in children:

            if key in keys_one and key in keys_two:
                if el1.get(key) == el2.get(key):
                    result[key] = {'eqo': el1[key]}
                else:
                    result[key] = {'both': make_diff(el1.get(key), el2.get(key))}
            elif key in keys_one:
                result[key] = {'was': el1[key]}
            else:
                result[key] = {'add': el2[key]}
    else:
        return {'was': el1, 'add': el2 }
    return result


def formatter(element):
    result = ""

    if not isinstance(element, dict):
        return element

    children = element.keys()

    for key in children:
        if isinstance(element[key], dict):
            if element[key].get('was') is not None:
                result += f"  - {key}: {formatter(element[key]['was'])}\n"
            if element[key].get('add') is not None:
                result += f"  + {key}: {element[key]['add']}\n"
            if element[key].get('eqo') is not None:
                result += f"    {key}: {element[key]['eqo']} \n"
            if element[key].get('both') is not None:
                result += f"    {key}: {element[key]['both']} \n"
        else:
            result += str(element[key])
    return result


if __name__ == '__main__':
    main()
