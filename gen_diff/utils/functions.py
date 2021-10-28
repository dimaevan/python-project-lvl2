def is_dict(obj):
    """ Return True if type(atr) is dictionary """
    if type(obj) is dict:
        return True


def is_have_stat(obj):
    """ If obj is dictionary and have key "status" return True """
    if is_dict(obj) and obj.get('status') is not None:
        return True


def return_status(obj):
    """ Return value of key"status" if it exists or "None" """
    if is_have_stat(obj):
        return obj['status']


def check_type(obj):
    """ Function for better formatting """
    if is_dict(obj):
        return "[complex value]"
    elif obj == "false":
        return "false"
    elif obj == "true":
        return "true"
    elif obj == "null":
        return "null"
    elif type(obj) is int:
        return obj
    return str("'" + str(obj) + "'")


def walker(el):
    result = {}
    if type(el) != dict:
        return convert(el)
    for key in el.keys():
        result[key] = walker(el[key])
    return result


def convert(obj):
    dictionary = {
        'False': 'false',
        'True': 'true',
        'None': 'null',
        '': ''
    }
    return dictionary.get(str(obj), obj)
