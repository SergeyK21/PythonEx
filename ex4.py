"""
4.	Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
try:
    N = input('Введите натуральное положительное число: ')
    number = int(N)
    if (number < 0):
        raise ValueError
except (ValueError):
    print('Ошибка ввода! Попробуйте еще раз!')
else:
    String = str(N)
    max = int(String[0])
    i = 1
    while i < len(String):
        if int(String[i]) > max:
            max = int(String[i])
        i += 1
    print(f'Самая большая цифра = {max}')
