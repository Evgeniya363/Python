#     Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

a = '97*x^5 + 92*x^4 + 60*x^3 + 21*x^2 + 28 = 0'
b = '7*x^3 + 85*x^2 + 35*x + 98 = 0'

in_list = list(map(int, (a+' '+b).replace('*x ',' 1 ').replace(' = 0', ' 0').replace('*x^',' ').replace(' +','').split()))
print(in_list)

# Пока что я слабо представляю как выполнить это задание "красиво"  с помощью коллекций и агрегатных функций
# Нужно подумать, а некрасиво всегда можно решить)

# print(max(r_list[0]))
# for i in (0, len(r_list), 2):
#     res_list.append(r_list[i],r_list[i])

# # pol_list = []
# # a_dict = []

# # # print(a_list) 


# # # a_dict=[(a_list[i+1], a_list[i]) for i in range(0, len(a_list), 2)]
# # print(a_dict) 
# # for i in range(0,len(a_list), 2):
# #     print(a_list[i+1])
# #     a_dict.append([a_list[i]],a_list[i+1])
# # # for i in range(0, len(a_list), 2):
# # #     print(a_list[i])

# # print(a_dict)    

# # # # # res = [tuple(map(int, sub.split(', '))) for sub in test_list] 
# # # # a_ls = [tuple(map(int, sub.split())) for sub in a_list]
# # # # a_ls = [(map(dict, sub.split())) for sub in a_list]
# # # # print(a_ls)

# # # # # elements = a_list.split()
# # # # a_tuple = tuple(tuple(a_list))
# # # # # int(item) for item in s.split(',')
# # # # print(a_list)
