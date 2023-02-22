def show_data(cnts, title_list='Список контактов: '):
    print('\n'+title_list)
    if cnts:
        for ID in cnts:
            print(ID, *cnts[ID])
    else:
        print('Не найдено')


def find_data(contacts, search_p):
    if type(search_p) == int:
        if search_p in contacts:
            return {search_p: contacts[search_p]}
        else:
            return 0
    else:
        selected_id = {}
        search_p = [item for item in enumerate(search_p[0]) if item[1]]

        for c_key in contacts:
            access = True
            c_data = contacts[c_key]

            for i, item in search_p:
                if not c_data[i].lower().startswith(item.lower()):
                    access = False
                    break
            if access:
                selected_id[c_key] = c_data
        return selected_id
