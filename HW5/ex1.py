"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""
with open('text_ex1.txt', 'a', encoding='utf-8') as f_obj:
    str_1 = input('Введите строку: ')
    while (str_1 != ''):
        f_obj.write(str_1 + '\n')
        str_1 = input('Введите строку: ')
