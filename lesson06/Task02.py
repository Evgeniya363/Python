# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

# Функция ввода целого натурального числа из заданного диапазона
def input_number(inp_str, begin = 0, end = 1):
    resalt = -1
    while not(resalt in range(begin, end+1)):
        resalt = int(input(inp_str))
    return resalt

n = input_number(f'\nДан массив M[1, n]\nВведите размерность массива n: ', 1, 100)

# Задавать массив для данной задачи смысла нет
# my_list = [randint(1,99) for i in range(n)]

d1  = input_number(f'Введите индекс d1 в диапазоне [1, {n}]: ', 1, n)
d2  = input_number(f'Введите индекс d2 в диапазоне [{d1}, {n}]: ', d1, n)

print(f'\nИндексы массива M[1, n], принадлежащие диапазону [{d1}, {d2}]: {[i for i in range(d1, d2 + 1)]}\n')