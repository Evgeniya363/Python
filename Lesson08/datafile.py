import io

# Метод чтения данных из файла в коллекцию типа dictionary


def init_data():
    cnts = set()

    with open('text.txt', 'r', encoding='utf-8') as file:
        list_1 = file.read()

    list_1 = [st.split(';') for st in list_1.splitlines()]
    cnts = {int(item[0]): item[1:] for item in list_1}
    print('\nДанные считаны')
    return cnts

# Метод сохранения данных в файл из коллекции типа dictionary


def save_data(cnts):
    list_1 = [[str(ID)] + cnts[ID] for ID in cnts]
    list_1 = [(';').join(item) for item in list_1]
    list_1 = '\n'.join(list_1)

    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(list_1)
    print('\nДанные сохранены')
