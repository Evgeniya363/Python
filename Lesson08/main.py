# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию        человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# ------------------------------------------------------------------------
# Основной модуль программы: инициализация справочника, организация меню,
# управление функциями добавления, удаления, поиска
# ------------------------------------------------------------------------

from time import sleep
from input_data import input_fields, input_int
from user_menu import menu
from contacts import show_data, find_data
from datafile import init_data, save_data


# Основной метод программы, реализующий взаимодействие с пользователем
# через циклический вызов пользовательского меню
# Данные считываются из текстового файла в словарь,
# где целочисленный уникальный номер контакта используется в качестве ключа,
# а значением выступает список набора данных: фамилии, имени, отчества и номера телефона

def communications():
    is_exit = False  # Флаг выхода из цикла
    mode = 0        # Режим вызова меню (1-3)
    ID = 0          # текущий элемент справочника (ключ словаря)

    while not is_exit:

        if mode == 0:           # Работа со справочником контактов
            show_data(contacts)
        if mode == 1:           # Работа с выбранными контактами
            show_data(select_contacts, 'Найдены контакты:')

        exit_code = menu(mode)  # Вызов меню

        if exit_code == 0:      # Выход из программы
            if input_int('Вы хотите выйти из программы? [1-да, 0-нет]: '):
                is_exit = True

        elif exit_code == 7:    # Новый контакт
            new_key = max(contacts.keys())+1 if contacts else 1
            new_contact = input_fields(
                exit_code, 'Создание нового контакта', new_key)
            mode = 2

        elif exit_code == 4:    # Изменение контакта
            new_contact = input_fields(
                exit_code, 'Изменить контакт', ID, select_contacts[ID].copy())
            mode = 2

        elif exit_code == 8:    # Удаление контакта
            parameters = ' '.join(select_contacts[ID])
            if input_int(f'Удалить контакт "{parameters}"?[1-да, 0-нет]: ', [0, 1]):
                del contacts[ID]
                print('Контакт удален')
                sleep(1)
                mode = 0

        elif exit_code == 3:  # Поиск контакта
            message_ps = 'Поиск контакта\nВведите один или несколько параметров поиска'
            search_ps = input_fields(
                exit_code, message_ps) if contacts else 0

            select_contacts = find_data(contacts, search_ps)
            if not select_contacts:
                print('Контактов не найдено')
                sleep(1)
            else:
                ID = list(select_contacts.keys())[0]
                mode = 1

        elif exit_code == 2:    # Сохранение данных при операциях добавления и корректировки
            if new_contact:
                contacts.update(new_contact)
            mode = 0

        elif exit_code == 9:  # Выход в основное меню
            mode = 0
        elif exit_code == 5:  # Отмена и выход в основное меню
            print('Действие отменено')
            sleep(1)
            mode = 0


# Точка входа
def main():
    global contacts
    contacts = dict()       # Переменная для хранения списка контактов типа dictionary
    contacts = init_data()  # Инициализация данных
    print('\nВас приветствует программа "Телефонный справочник"')
    communications()        # Основной цикл
    save_data(contacts)     # Сохранение данных в файл
    print('Работа программы завершена\n')


if __name__ == '__main__':
    main()
