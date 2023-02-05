#    Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
#   (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    Пример:
#    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#from random import random

import random 
# beg=0 
# end=100 
# random_integer = random.randint(beg, end) 
# print("The random integer is :", random_integer)

k = int(input(('Формирование многочлена степени k, Ппример:\n' +
'   k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0\nВведите степень многочлена (k > 0): ')))

polynomial = ''
for i in range(k, -1, -1):
    a_i = random.randint(0,100)

    if a_i > 0:
        if len(polynomial) > 0:
            polynomial += '+ '

        polynomial += str(a_i)

        if a_i > 0 and i > 0:
            polynomial +='*x'
            if i > 1:
                polynomial += '^' + str(i)

        polynomial += ' '

if len(polynomial) == 0:
    polynomial = '0 '

polynomial += '= 0'
    
print('Случайный многочлен: ', polynomial)
