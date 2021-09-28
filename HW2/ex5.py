"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]

try:
    number = int(input('Введите натуральное число: '))
except ValueError:
    print('Ошибка! Введите натуральное число!')
else:
    my_list = my_list[::-1]
    for i in range(len(my_list)):
        if my_list[i] == number:
            my_list.insert(i, number)
            my_list = my_list[::-1]
            break
    else:
        my_list = my_list[::-1]
        my_list.append(number)
        for i in range(len(my_list) - 1):
            for j in range(len(my_list) - 1 - i):
                if my_list[j] < my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # Крутая штука!
    print(my_list)

'''
# сортировка пузырьком
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # Крутая штука!
    print(my_list)
'''
