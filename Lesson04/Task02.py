# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

N = int(input('Введите натуральное число\n  N = '))

d  = abs(N)
if d > 0:
    d_i = d + 1
    r_list = [-1, 1]

    while d < d_i:
        d_i = d
        i = 2
        while i <= round(d / 2) and d_i == d:
            if d % i == 0:
                d //= i
                if r_list[-1] < i:
                    r_list.append(i)
                    r_list.insert(0, -i)
            else:
                i += 1

    if d > 1 and d > r_list[-1]:
        r_list.append(d)
        r_list.insert(0, -d)

    print('Простые делители N:\n ', r_list)
else:
    print('Простые делители N: все числа, кроме 0 ')