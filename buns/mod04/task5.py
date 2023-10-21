def get_aplh() -> set:
    m = [[97, 122], [65, 90], [1040, 1103]]
    return set([chr(i) for t in m for i in range(t[0], t[1] + 1)])


def get_dict_from_file(file_name) -> dict:
    file = open(file_name, encoding='UTF-8')
    d = dict()
    s = file.readline()
    while s:
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        s = file.readline()
    return d


def print_answer_to_file(m: list, file_name) -> None:
    f = open(file_name, mode='w')
    for i in m:
        f.write(f'{i[-1]}: {i[0]}\n')


line = input()
dict_alph = get_dict_from_file(line)
alph = get_aplh()
ans = [[dict_alph[i], i] for i in dict_alph if i in alph]
ans.sort()
print_answer_to_file(ans, 'output5.txt')
