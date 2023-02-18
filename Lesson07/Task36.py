# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы(подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def sum(a, b):
    return a + b


def print_operation_table(operation, num_rows=6, num_columns=6):
    list_r = [[operation(i + 1, j + 1) for i in range(num_columns)]
              for j in range(num_rows)]
    for i in range(num_rows):
        print(*["%3d" % elem for elem in list_r[i]])


print('\nВывод результата вычисления операции f(i, j), где i - строка, j - столбец')
print('\nСумма i + j:\n')
print_operation_table(sum)

print('\nПроизведение i * j\n')
print_operation_table(lambda x, y: x * y, 5)

print('\nВыражение x^2 + y^2 - x*y\n')
print_operation_table(lambda x, y: x**2 + y**2 - x*y, num_columns=4)
