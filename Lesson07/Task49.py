# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

import math

# Метод 1


def find_farthest_orbit(list_of_orbits):
    lo = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    ls = [(item[0]*item[1]*math.pi, i) for i, item in enumerate(lo)]
    maxS = max(ls[1])
    ls = list(filter(lambda x: x[0] == maxS, ls))
    return lo[ls[0][1]]

# Метод 2


def find_farthest_orbit2(list_of_orbits):
    maxS = 0
    res = ()
    for elem in list_of_orbits:
        if elem[0] != elem[1]:
            S = elem[0]*elem[1]*math.pi
            if maxS < S:
                maxS, res = S, elem
    return res


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(find_farthest_orbit(orbits))
print(find_farthest_orbit2(orbits))
