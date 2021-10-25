import json
import os
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
    this_diff = make_diff(obj1, obj2)
    return format_dict(this_diff)


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
                    rec = make_diff(el1.get(key), el2.get(key))
                    if rec.get('was') is not None:
                        result[key] = {'status': 'diff', 'children': rec}
                    else:
                        result[key] = {'status': '  ', 'children': rec}
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


def format_dict(struct):
    result = ""
    left_space = '    '

    def sub_format(element, spacing, size):
        if type(element) is not dict:
            return element
        space = spacing * size
        size += 1
        line = "{"
        keys = element.keys()

        for key in keys:
            el = element[key]
            # Проверяем обьект или обычный словарь
            if is_get_stat(el):
                prefix = el['status']
                if prefix == 'diff':
                    line += f"\n{space[:-2]}- {key}: {sub_format(el['children']['was'], left_space, size)}"
                    line += f"\n{space[:-2]}+ {key}: {sub_format(el['children']['add'], left_space, size)}"
                # Если обьект без диффа
                else:
                    line += f"\n{space[:-2]}{prefix}{key}: {sub_format(el['children'], left_space, size)}"
            else:
                line += f"\n{space[:-2]}{key}: {sub_format(el, left_space, size)} "

        line += "\n" + space[:-4] + "}"
        return line

    result += sub_format(struct, left_space, 1)
    return result


def is_get_stat(el):
    if type(el) is dict:
        if el.get('status') is not None:
            return True


if __name__ == '__main__':
    main()
