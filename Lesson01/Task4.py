"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
координат точек в этой четверти(x и y).
"""
print('Определение диапозона возможных значений x и y по номеру четверти в координатной плоскости XOY')
quarter = int(input('Введите нимер четверти (1-4) = '))
if quarter < 1 or quarter > 4:
    print('Неверный ввод')
else:
    if quarter == 1 or quarter == 4:
        print('x > 0')
    else:
        print('x < 0')
    if quarter < 3:
        print('y > 0')
    else:
        print('y < 0')
