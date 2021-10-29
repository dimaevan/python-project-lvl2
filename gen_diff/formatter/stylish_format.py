from gen_diff.utils.functions import is_have_stat


def stylish(struct):
    result = ""

    def inner(element, size, spacing='    '):
        if type(element) is not dict:
            return element

        space = spacing * size
        size += 1
        line = "{"

        for key in element.keys():
            el = element[key]
            # Проверяем обьект или обычный словарь
            if is_have_stat(el):
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
                line += f"\n{space}{key}: {inner(el, size)}"

        line += "\n" + space[:-4] + "}"
        return line

    result += inner(struct, 1)
    return result.rstrip()
