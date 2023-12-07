import re


def get_ans(line):
    """
    Эта функция проверяет пароль на корректность.

    Примеры:

    >>> get_ans('rtG3FG!Tr^e')
    True
    >>> get_ans('aA1!*!1Aa')
    True
    >>> get_ans('oF^a1D@y5e6')
    True
    >>> get_ans('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> get_ans('пароль')
    False
    >>> get_ans('password')
    False
    >>> get_ans('qwerty')
    False
    >>> get_ans('lOngPa$$$W0Rd')
    False
    """

    def chesk_1_2(s):
        pattern = r'^[a-zA-Z0-9^$%@#&*!?]{6,}$'
        return re.search(pattern, s) is None

    def chesk_3(s):
        pattern = r'(?:[A-Z].*){2,}'
        return re.search(pattern, s) is None

    def chesk_4(s):
        pattern = r'.*\d.*'
        return re.search(pattern, s) is None

    def chesk_5(s):
        t = r'[\^$%@#&*!?]'
        matched_t = re.search(t, s)
        if matched_t is None:
            return True
        val = matched_t.group(0)
        line_temp = re.sub(rf'\{val}', '', s)
        t = r'[\^$%@#&*!?]'
        return re.search(t, line_temp) is None

    def chesk_6(s):
        pattern = r'^(?!.*(.)\1\1).*$'
        return re.search(pattern, s) is None

    ans = []
    ans.append(chesk_1_2(line))
    ans.append(chesk_3(line))
    ans.append(chesk_4(line))
    ans.append(chesk_5(line))
    ans.append(chesk_6(line))

    return not any(ans)
