# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Добавлено кодирование цифр, напимер, '222222' -> '6 2 '

import os.path

# Функция сжатия повторяющихся (count) символов (item)


def rle_encode(item, count):
    sep = ('', ' ')[item.isdigit() or item == ' ']
    return f'{count}{sep}{item}{sep}'

# Функция, обработки выделения последовательностей повторяющихся символов
# и их дальнейшего сжатия


def rle_compress(str):
    str_comp = ''
    if len(str) > 0:
        count = 0
        liter = str[0]
        for item in str:
            if item == liter:
                count += 1
            else:
                str_comp += rle_encode(liter, count)
                liter = item
                count = 1
        str_comp += rle_encode(liter, count)
    return str_comp

# Функция выделения из строки блоков, представляющих собой RLE последовательности,
# и их дальнейшее восстановление в исходную строку


def rle_decompress(str):
    str_uncomp = ''
    if len(str) > 0:
        num = ''
        issp = False

        for item in str:
            if item.isdigit() and not issp:
                num += item
            else:
                if item.isspace():
                    issp = len(num)
                else:
                    str_uncomp += item * int(num)
                    num = ''
                    issp = False
    return str_uncomp


def compress(file_name, compsess=True):

    if os.path.exists(file_name):
        file = open(file_name)
        text = file.read()
        print('\nИсходный:   ', text)

        if compsess:
            text = rle_compress(text)
        else:
            text = rle_decompress(text)
        print('\nПолученный: ', text)
        file.close()
    else:
        print('Файл отсутствует')


compress("file4.txt", True)
compress("file4.rle", False)
print()
