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

    file_1 = open_file(first_file)
    file_2 = open_file(second_file)

    # Выбор форматирования
    if args.format == 'plain':
        print(generate_diff(file_1, file_2, 'plain'))
    elif args.format == 'json':
        print(generate_diff(file_1, file_2, 'json'))
    else:
        print(generate_diff(file_1, file_2))


def open_file(file):
    ext = str(file).split('.')[-1]
    if ext == 'json':
        return json.load(open(file))
    elif ext in ("yaml", "yml"):
        return yaml.safe_load(open(file))
    raise MyError("Wrong type of files")


def generate_diff(obj1, obj2, type_format='stylish'):
    this_diff = parser_dict(obj1, obj2)

    if type_format == "plain":
        return plain(this_diff)
    elif type_format == "json":
        return fjson(this_diff)
    else:
        return stylish(this_diff)


if __name__ == '__main__':
    main()
