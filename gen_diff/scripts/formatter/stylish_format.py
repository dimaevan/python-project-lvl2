def stylish(struct):
    result = ""

    def inner(element, size, spacing='    '):
        if type(element) is not dict:
            return element
        space = spacing * size
        size += 1
        line = "{"
        keys = element.keys()

        for key in keys:
            el = element[key]
            # Проверяем обьект или обычный словарь
            if is_get_stat(el):
                prefix = el['status']
                if prefix == 'diff':
                    line += f"\n{space[:-2]}- {key}:" \
                            f" {inner(el['children']['was'], size)}"
                    line += f"\n{space[:-2]}+ {key}:" \
                            f" {inner(el['children']['add'], size)}"
                # Если обьект без диффа
                else:
                    line += f"\n{space[:-2]}{prefix}{key}:" \
                            f" {inner(el['children'], size)}"
            else:
                line += f"\n{space[:-2]}{key}: {inner(el, size)} "

        line += "\n" + space[:-4] + "}"
        return line

    result += inner(struct, 1)
    return result


def is_get_stat(el):
    if type(el) is dict:
        if el.get('status') is not None:
            return True
