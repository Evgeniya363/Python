# Функция ввода целого натурального числа из заданного диапозона
def input_number(inp_str, begin = 0, end = 1):
    resalt = -1
    while not(resalt in range(begin, end+1)):
        resalt = int(input(inp_str))
    return resalt

# Функция вывода заголовков
def print_header(sp, title):
    space = ' '*sp
    print(space + title +'\n' + space + '-'*len(title))

# Адаптация числовых значений матрицы для вывода на экран
def get_symbol(matr_str: list) -> str:
    out_str = []
    for it in matr_str:
        if it == 1:
            out_str.append('O')
        elif it == -1:
            out_str.append('X')
        else:
            out_str.append(' ')
    return out_str