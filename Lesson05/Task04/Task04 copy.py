# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Добавлено кодирование цифр

# Функция сжатияповторяющихся (count) символов (item)
def rle_encode(item, count):
    sep = ('', ' ')[item.isdigit() or item==' ']
    return f'{count}{sep}{item}{sep}'

# Функция, обработки выделения последовательностей повторяющихся символов 
# и их дальнейшего сжатия
def rle_compress(str):
    str_comp = ''
    if len(str)>0:
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
    if len(str)>0:
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
           
# Инициализация строки и использование функций RLE сжатия и восстановления 
str = 'TThh3333TTT222ERRAAlllddnnWWPP^^2GGGGG*$$$$cCCCCvbNNNmm'
print(str)
str2=rle_compress(str)
print(str2)
print(rle_decompress(str2))