# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

def transformation(x):
    return x


values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))

print('Исходный список:   ', values)
print('Полученный список: ', transformed_values)

answer = '' if values == transformed_values else 'не'
print('Полученный список {}является копией исходного'.format(answer))
