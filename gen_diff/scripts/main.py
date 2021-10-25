import json
import os
import argparse
import yaml
from .formatter.stylish_format import stylish
# from .formatter.plain_format import plain


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


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

    print(generate_diff(first_file, second_file))


def open_files(first, second):
    first_extend = str(first).split('.')[-1]
    second_extend = str(second).split('.')[-1]

    if first_extend != second_extend:
        raise MyError("Wrong type of files")

    if first_extend == 'json':
        example = json.load(open(first))
        compared = json.load(open(second))
    else:
        example = yaml.safe_load(open(first))
        compared = yaml.safe_load(open(second))

    return example, compared


def generate_diff(obj1, obj2):
    first_dict, second_dict = open_files(obj1, obj2)
    this_diff = make_diff(first_dict, second_dict)
    return stylish(this_diff)


def make_diff(el1, el2):
    result = {}
    # Если сравниваемые значения - словари
    if type(el1) is dict and type(el2) is dict:

        keys_el1 = set(el1.keys())
        keys_el2 = set(el2.keys())

        children = sorted(keys_el1.union(keys_el2))

        for key in children:

            if key in keys_el1 and key in keys_el2:
                # Ключи в обоих словарях, ключи равны
                if el1.get(key) == el2.get(key):
                    result[key] = {'status': '  ', 'children': el1[key]}
                else:
                    recurs = make_diff(el1.get(key), el2.get(key))
                    result[key] = check_children(recurs)
            # Ключ только в первом словаре - удален
            elif key in keys_el1:
                result[key] = {'status': '- ', 'children': el1[key]}
            # Ключ только во втором словаре - добавлен
            else:
                result[key] = {'status': '+ ', 'children': el2[key]}
    # Если сравниваемые значения - разные типы
    else:
        return {'was': el1, 'add': el2}

    return result


def check_children(some_dict):
    if some_dict.get('was') is not None:
        return {'status': 'diff', 'children': some_dict}
    else:
        return {'status': '  ', 'children': some_dict}


if __name__ == '__main__':
    main()
