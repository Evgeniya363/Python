# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

M = 100 # Максимальная величина элементов массива

# Функция ввода целого натурального числа из заданного диапазона
def input_number(inp_str, begin = 0, end = 1):
    resalt = -1
    while not(resalt in range(begin, end+1)):
        resalt = int(input(inp_str))
    return resalt

n = input_number(f'\nВведите размерность массива n: ', 1, M)

my_list = [randint(1, M) for i in range(n)]
print('Сформирован массив: ', my_list)

d1  = input_number(f'Введите нижнюю границу значений [1, {M}]: ', 1, M)
d2  = input_number(f'Введите верхнюю границу значений [{d1}, {M}]: ', d1, M)

ind_list = [i for i in range(len(my_list)) if d1 <= my_list[i] <= d2]

print(f'\nИндексы массива M[1, n] элементов,\nпринадлежащих диапазону  значений [{d1}, {d2}]: {ind_list}\n')