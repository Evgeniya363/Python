"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

При
- A(3, 6)
B(2, 1) -> 5, 09
- A(7, -5)
B(1, -1) -> 7, 21
"""
import math

print('Введите координаты точек A(x1, y1) и B(x2, y2):')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
print(f'Расстояние между точками A({x1},{y1}) и B({x2},{y2}) равно ', round(math.sqrt((x2-x1)**2+(y2-y1)**2), 1))
