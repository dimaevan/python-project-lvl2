def is_dict(obj):
    """ Return True if type(atr) is dictionary """
    if type(obj) is dict:
        return True
    return False


def is_have_stat(obj):
    """ If obj is dictionary and have key "status" return True """
    if is_dict(obj) and obj.get('status') is not None:
        return True
    return False


def return_status(obj):
    """ Return value of key"status" if it exists or "None" """
    if is_have_stat(obj):
        return obj['status']
    return None


def check_type(obj):
    """ Function for better formatting """
    if is_dict(obj):
        return "[complex value]"
    return str("'" + str(obj) + "'")
