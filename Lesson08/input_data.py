import keyboard

# Метод ввода данных контакта


def input_fields(mode=3, title_form='Поиск', id=0, data=[]):
    print('\n'+title_form)
    column = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона']

    if not data:
        data = ['' for i in range(len(column)-1)]
    if id > 0:
        print(f'{column[0]}: {id}')   # уникальный номер (ID) контака задан
    else:
        id = input(f'{column[0]}: ')  # ID предлагается ввести пользователю
        if id.isdigit():        # при вводе ID другие параметры не запрашиваются
            return int(id)
        else:
            id = 0

    for i in range(len(data)):    # ввод параметров в цикле
        keyboard.write(data[i])
        data[i] = input(f'{column[i+1]}: ')

    return {id: data}


# Метод ввода целого числа из списка
def input_int(title, lst=[]):
    inlist = len(lst) != 0
    answ = 0
    access = False
    while not access:
        try:
            answer = int(input(title))
        except:
            print('Неверный ввод')
            continue
        access = not inlist or answer in lst
    return answer


if __name__ == '__main__':
    input_fields(3, 'Поиск')  # 40:['Иванов','Иван','Иванович','1912917294']
    # input_int('Введите число: ')
