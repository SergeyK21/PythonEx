"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from random import randint
from functools import reduce


def my_sum(a, b):
    """
    Суммирование

    :param a:
    :param b:
    :return:a + b
    """
    return a + b


print(reduce(my_sum, (randint(100, 1000) for i in range(4))))
