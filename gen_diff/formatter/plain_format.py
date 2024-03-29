from gen_diff.utils.functions import return_status, check_type, is_dict

STATUSES = ('- ', '+ ', 'diff')


def plain(element, parent=''):
    if not is_dict(element):
        return
    result = ''
    pr = ''
    if parent:
        pr = parent + '.'

    for key in element.keys():
        el = element[key]

        status = return_status(el)
        first_string = f"Property '{pr}{key}' was "

        if status in STATUSES:
            result += first_string + answer(status, el)
        else:
            res = plain(el['children'], parent=pr + key)
            if type(res) is str:
                result += res + '\n'
    return result.rstrip()


def answer(status, el):
    if status == '- ':
        return "removed\n"
    elif status == '+ ':
        value = check_type(el['children'])
        return f"added with value: {value}\n"
    elif status == 'diff':
        was = check_type(el['children']['was'])
        add = check_type(el['children']['add'])
        return f"updated. From {was} to {add}\n"
    return ''
