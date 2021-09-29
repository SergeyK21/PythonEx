"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    Принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

    :param a:
    :param b:
    :param c:
    :return: sum([...])
    """
    try:
        ls = [a, b, c]
        ls.remove(min(ls))
        s_ls = sum(ls)
        return s_ls
    except Exception as e:
        return f'Произошла ошибка - {e}'


if __name__ == '__main__':
    print(my_func(1, 4, 2))
