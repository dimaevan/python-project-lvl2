import json
import os
import argparse
import yaml
from .parser.parsing import parser_dict
from .formatter.stylish_format import stylish
from .formatter.plain_format import plain
from .formatter.json_format import fjson


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def main():
    # Args parser
    parser = argparse.ArgumentParser(description='Generate diff')
    # Обязательные параметры
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Необязательные пармаетры( Есть "--")
    parser.add_argument("-f", '--format', help='set format of output')
    args = parser.parse_args()
    # Получаем рабочую директорию и отсительное расположение файлов
    first_file = os.path.join(os.getcwd(), args.first_file)
    second_file = os.path.join(os.getcwd(), args.second_file)
    # Выбор форматирования
    if args.format == 'plain':
        print(generate_diff(first_file, second_file, 'plain'))
    elif args.format == 'json':
        print(generate_diff(first_file, second_file, 'json'))
    else:
        print(generate_diff(first_file, second_file))


def open_files(first, second):
    # Получаем расширения обоих фалов
    first_extend = str(first).split('.')[-1]
    second_extend = str(second).split('.')[-1]
    # Проверка,что файлы с одинаковым расширением
    if first_extend != second_extend:
        raise MyError("Wrong type of files")

    if first_extend == 'json':
        example = json.load(open(first))
        compared = json.load(open(second))
    elif first_extend in ("yaml", "yml"):
        example = yaml.safe_load(open(first))
        compared = yaml.safe_load(open(second))
    else:
        raise MyError("Wrong type of files")

    return example, compared


def generate_diff(obj1, obj2, type_format='stylish'):
    first_dict, second_dict = open_files(obj1, obj2)
    this_diff = parser_dict(first_dict, second_dict)
    # 4 develop only
    # print(this_diff)
    if type_format == "plain":
        return plain(this_diff)
    elif type_format == "json":
        return fjson(this_diff)
    else:
        return stylish(this_diff)


if __name__ == '__main__':
    main()
