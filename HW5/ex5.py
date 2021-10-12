"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
try:
    str_1 = input('Введите числа: ')
    print(*(int(el) for el in str_1.split()))
    with open('text_ex5.txt', 'w') as f_obj:
        f_obj.writelines(str_1)
    with open('text_ex5.txt') as f_obj:
        numbers_1 = (int(el) for el in f_obj.read().split())
    print(f'Сумма элементов: {sum(numbers_1)}')
except ValueError as ex:
    print(f'Ошибка - {ex}')
