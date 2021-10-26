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
                    result[key] = {'status': '  ', 'children': el1[key]}
                else:
                    recurs = parser_dict(el1.get(key), el2.get(key))
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


if __name__ == "__main__":
    from tests.fixtures.fixtures import json3, json4
    print(parser_dict(json3, json4))
