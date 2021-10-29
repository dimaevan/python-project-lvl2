from gen_diff.utils.functions import is_dict, is_have_stat
import json


def fjson(el):
    out = diff_2_dict(el)
    return json.dumps(out)


def diff_2_dict(element):
    result = {}

    if not is_dict(element):
        return element

    for key in element.keys():
        el = element[key]

        if is_have_stat(el):
            prefix = el['status']

            if prefix in ('- ', '+ '):
                result[prefix + key] = el['children']
            elif prefix == 'diff':
                result[key] = {'-': el['children']['was'],
                               '+': el['children']['add']}
            else:
                result[key] = diff_2_dict(el['children'])
    return result
