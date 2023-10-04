a = int(input())


def get_format(x: float) -> str:
    int_num = ''
    float_num = '.'
    num_after_point = 0
    flag_point = False
    for i in str(x):
        if flag_point:
            float_num += i
            num_after_point += 1

        if num_after_point > 2:
            break

        if i == '.':
            flag_point = True
        if not flag_point:
            int_num += i

    if num_after_point == 2:
        return int_num + float_num
    if num_after_point == 1:
        return int_num + float_num + '0'

    if float_num[-2] == '9' and int(float_num[-1]) >= 5:
        if float_num[-3] == '9':
            return str(int(int_num) + 1) + '.00'
        return int_num + '.' + str(int(float_num[1]) + 1) + '0'
    if int(float_num[-1]) >= 5:
        return int_num + float_num[:-2] + str(int(float_num[-2]) + 1)
    return int_num + float_num[:-1]


perimeter = float(4 * a)
square = float(a * a)
diagonal = a * (2 ** 0.5)

print(get_format(perimeter), get_format(square),
      get_format(diagonal), sep=', ')
