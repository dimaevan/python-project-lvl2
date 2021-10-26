result = ''


def plain(element, parent=''):
    global result
    if type(element) is not dict:
        return

    pr = ''
    if parent:
        pr = parent + '.'

    child = element.keys()

    for _ in child:
        el = element[_]
        if is_get_stat(el) == '- ':
            result += f"Property '{pr}{_}' was removed\n"
        elif is_get_stat(el) == '+ ':
            value = check_type(el['children'])
            result += f"Property '{pr}{_}' was added with value: {value}\n"
        elif is_get_stat(el) == 'diff':
            was = check_type(el['children']['was'])
            add = check_type(el['children']['add'])
            result += f"Property '{pr}{_}' was updated. From {was} to {add}\n"
        else:
            plain(el['children'], parent=pr+_)

    return result


def is_get_stat(el):
    """ Return status of dict-object """
    if type(el) is dict:
        if el.get('status') is not None:
            return el['status']


def check_type(el):
    """ Function for better formatting """
    if type(el) is dict:
        return "[complex value]"
    else:
        return str("'" + str(el) + "'")


if __name__ == "__main__":
    pass
