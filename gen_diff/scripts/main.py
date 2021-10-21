import json
import os
import pprint

import argparse
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
    a = make_diff(obj1, obj2)
    # pprint.pprint(a)
    # print('OUT:')
    return formatter(a)


def make_diff(el1, el2):
    result = {}

    if type(el1) is dict and type(el2) is dict:
        keys_el1 = set(el1.keys())
        keys_el2 = set(el2.keys())

        children = sorted(keys_el1.union(keys_el2))

        for key in children:
            if key in keys_el1 and key in keys_el2:
                if el1.get(key) == el2.get(key):
                    result[key] = {'status': 'eqo', 'children': el1[key]}
                else:
                    rec = make_diff(el1.get(key), el2.get(key))
                    if rec.get('diff'):
                        result[key] = rec
                    else:
                        result[key] = {'status': 'both', 'children': rec}
            elif key in keys_el1:
                result[key] = {'status': 'was', 'children': el1[key]}
            else:
                result[key] = {'status': 'add', 'children': el2[key]}
    else:
        return {'status': 'diff', "children": {'was': el1, 'add': el2}}
    return result


def formatter(element):
    result = "{"

    if type(element) is not dict:
        return element

    children = element.keys()

    for key in children:
        el = element[key]
        if el.get('status'):
            if el['status'] is 'was':
                result += f"\n- {key}: {el['children']}"
            elif el['status'] is 'add':
                result += f"\n+ {key}: {el['children']}"
            elif el['status'] is 'eqo':
                result += f"\n  {key}: {el['children']}"
            elif el['status'] is 'both':
                result += f"\n  {key}: {el['children']}"
            else:
                result += f"\n  {key}: {el['children']}"
        else:
            result = f"{el}"

    result += "\n}"
    return result


if __name__ == '__main__':
    main()
