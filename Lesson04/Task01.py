# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

print(('Вычисление числа пи с помощью ряда Нилаканта:\n'+
       '    π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)\n'))

str_d = input('Введите точность  (например, 0.001, 10^{-1} ≤ d ≤10^{-10}$)\nd = ')

rounding = len(str(str_d).split('.')[1])
d = abs(float(str_d))

if 0.1 >= d >= 10**(-10):
    pi = i = 3
    sign = rate = 1
    PI = math.pi

    while rate >=  d:
        pi_i = pi
        pi = pi + sign * 4 / ((i - 1) * i * (i + 1))
        rate =  abs(pi-PI)/PI
        i += 2
        sign = - sign

    print(rate, i, rate<d)
    print('π = ', round(pi, rounding))
else:
    print('Неверный ввод')

