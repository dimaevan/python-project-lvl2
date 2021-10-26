import json


def fjson(el):
    out = diff_2_dict(el)
    return json.dumps(out)


def diff_2_dict(element):
    result = {}

    if type(element) is not dict:
        return element

    keys = element.keys()

    for key in keys:
        el = element[key]

        if is_get_stat(el):
            prefix = el['status']

            if prefix == '- ':
                result[prefix + key] = el['children']
            elif prefix == '+ ':
                result[prefix + key] = el['children']
            elif prefix == 'diff':
                result[key] = {'-': el['children']['was'],
                               '+': el['children']['add']}
            else:
                result[key] = diff_2_dict(el['children'])

    return result


def is_get_stat(el):
    if type(el) is dict:
        if el.get('status') is not None:
            return True
