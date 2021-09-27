"""
3.	Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
try:
    N = input('Введите натуральное положительное число: ')
    number = int(N)
    if (number < 0):
        raise ValueError
except (ValueError):
    print('Ошибка ввода! Попробуйте еще раз!')
else:
    print(f'n + nn + nnn = {N} + {N+N} + {N+N+N} = {int(N) +int(N+N) +int(N+N+N)}')