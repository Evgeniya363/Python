"""
Напишите программу, которая принимает на вход координаты точки(X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка(или на какой оси она находится).
Пример:
- x = 34
y = -30 -> 4
- x = 2
y = 4 -> 1
- x = -34
y = -30 -> 3
"""
print('Определение положения точки в четверти координатной плоскости по ее координатам X и Y, X!=0, Y!=0')
x = int(input('Введите X = '))
y = int(input('Введите Y = '))
if x*y == 0:
    print('Неверный ввод')
elif x > 0 and y > 0:
    print('I четверть')
elif x > 0 and y < 0:
    print('IV четверть')
elif y > 0:
    print('II четверть')
else:
    print('III четверть')


"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти(x и y).

Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A(3, 6)
B(2, 1) -> 5, 09
- A(7, -5)
B(1, -1) -> 7, 21
"""
