def parser_dict(el1, el2):
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
                    value = convert(el1[key])
                    result[key] = {'status': '  ', 'children': value}
                else:
                    recurs = parser_dict(convert(el1[key]), convert(el2[key]))
                    result[key] = check_children(recurs)
            # Ключ только в первом словаре - удален
            elif key in keys_el1:
                result[key] = {'status': '- ', 'children': convert(el1[key])}
            # Ключ только во втором словаре - добавлен
            else:
                result[key] = {'status': '+ ', 'children': convert(el2[key])}
    # Если сравниваемые значения - разные типы
    else:
        return {'was': convert(el1), 'add': convert(el2)}

    return result


def check_children(some_dict):
    if some_dict.get('was') is not None:
        return {'status': 'diff', 'children': some_dict}
    return {'status': '  ', 'children': some_dict}


def convert(obj):
    dictionary = {
        'False': 'false',
        'True': 'true',
        'None': 'null',
    }
    return dictionary.get(str(obj), obj)


if __name__ == "__main__":
    pass
    # from pprint import pprint
    # from gen_diff.main import open_file
    # from gen_diff.formatter.plain_format import plain
    # from gen_diff.formatter.stylish_format import stylish
    # file1 = open_file(
    #           "/home/dimaevan/Projects/Python/python-project-lvl2/tests/fixtures/complicated/file3.json")
    # file2 = open_file(
    #          "/home/dimaevan/Projects/Python/python-project-lvl2/tests/fixtures/complicated/file4.json")
    # answer = parser_dict(file1, file2)
    # pprint(answer)
    # print(stylish(answer))
