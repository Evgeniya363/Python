"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.
"""
success = True
print('Таблица истинности:')
print('x | y | z | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z')
print('----------------------------------------')
for x in range(2):
    for y in range(2):
        for z in range(2):
            resalt = not (x or y or z)
            resalt2 = not x and not y and not z
            print(f"{x} | {y} | {z} |      {int(resalt)}       |      {int(resalt2)}")
            if resalt != resalt2:
                success = False
print('----------------------------------------')
print('Утверждение', end=' ')
if success:
    print('истинно')
else:
    print('ложно')
