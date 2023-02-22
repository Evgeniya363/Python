import input_data as id

# Метод вывода меню программы и ввода кода команды управления списком


def menu(case=0):
    menu_lst = ['Выход', '', 'Сохранить', 'Поиск контакта', 'Изменить контакт', 'Отмена', '',
                'Новый контакт', 'Удалить контакт', 'Назад/Отмена']
    menu_set = [[3, 7, 0], [4, 8, 9], [2, 5]]

    print('\nДействия:')
    if case <= len(menu_set[0]):
        ls = menu_set[case]
        for i in ls:
            print('{}. {}'.format(i, menu_lst[i]))
        return id.input_int('Ваш выбор: ', ls)
    else:
        print(f'Ошибка вызова {case}')
        return case
