import re


def get_ans(line):
    """
    Эта функция проверяет: может ли являться входная строка
    (целиком) корректной записью цвета в одном из трёх web форматов.

    Примеры:

    >>> get_ans('#21f48D')
    True
    >>> get_ans('#888')
    True
    >>> get_ans('rgb(255, 255,255)')
    True
    >>> get_ans('rgb(10%, 20%, 0%)')
    True
    >>> get_ans('hsl(200,100%,50%)')
    True
    >>> get_ans('hsl(0, 0%, 0%)')
    True
    >>> get_ans('#2345')
    False
    >>> get_ans('ffffff')
    False
    >>> get_ans('rgb(257, 50, 10)')
    False
    >>> get_ans('hsl(20, 10, 0.5)')
    False
    >>> get_ans('hsl(34%, 20%, 50%)')
    False
    """
    if re.match(r'rgb', line) is not None:
        p = r'^rgb\(\s*(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%?\s*,\s*){2}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%?\s*\)$'
        return not (re.search(p, line) is None)

    if re.match(r'hsl', line) is not None:
        p = r'^hsl\(\s*(\d{1,3})\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%\s*\)$'
        return not (re.search(p, line) is None)

    if re.match(r'#', line) is not None:
        p = r'^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$'
        return not (re.search(p, line) is None)

    return False
