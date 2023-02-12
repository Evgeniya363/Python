#     Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import os.path

def text_extraction(text):
    print('\nИсходный текст: ', text)
    list_in = text.split()
    list_rez = [item for item in list_in if not ('абв' in item)]
    print('\nПреобразованный текст: ', ' '.join(list_rez))

file_path = "file1.txt"
if os.path.exists(file_path):
    file = open("file1.txt")
    text = text_extraction(file.read())
    file.close()
else:
    print('Файл отсутствует')
