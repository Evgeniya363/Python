# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

print(('Вычисление числа пи с помощью ряда Нилаканта:\n'+
       '    π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)\n'))

str_d = input('Введите точность  (например, 0.001, 10^{-1} ≤ d ≤10^{-10}$)\nd = ')

rounding = len(str(str_d).split('.')[1])
d = abs(float(str_d))

if 0.1 >= d >= 10**(-10):
    Pi = i = 3
    sign = rate = 1

    while rate >=  d:
        Pi_i = Pi
        Pi = Pi + sign * 4 / ((i - 1) * i * (i + 1))
        rate = abs((Pi_i - Pi))
        i += 2
        sign = - sign

    # print(rate, i)
    print('π = ', round(Pi, rounding))
else:
    print('Неверный ввод')

