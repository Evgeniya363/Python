# arr = [0,0,0]
# left = not (arr[0] or arr[1] or arr[2])
# right = not arr[0] and not arr[1] and not arr[2]
# print(left, right)

xyz = ["X", "Y", "Z"]
arr = []
for i in range(0,3):
    arr.append(input(f' Введите {xyz[i]}: '))

left = not (arr[0] or arr[1] or arr[2])
right = not arr[0] and not arr[1] and not arr[2]
if left == right:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")


print(arr[0] or arr[1] or arr[2])
print(not(arr[0] or arr[1] or arr[2]))
print(not(0))

# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(left,right)