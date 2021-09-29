"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    """
    Возведение в степень

    :param x:
    :param y:
    :return: x ** y
    """
    try:
        return x ** y
    except Exception as e:
        return f'Ошибка - {e}'


def my_func2(x, y):
    """
    Возведение в степень

    :param x:
    :param y:
    :return: x ** y
    """
    try:
        if y < 0:
            y *= -1
            result = 1
            for i in range(y):
                result *= x
            return 1 / result
        else:
            result = 1
            for i in range(y):
                result *= x
            return result
    except Exception as e:
        return f'Ошибка - {e}'


if __name__ == '__main__':
    print(my_func2(3, 3))
