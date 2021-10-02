"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary_calculation(hours, rate, prize=0):
    '''
    формула: (выработка в часах*ставка в час) + премия.

    :param hours:
    :param rate:
    :param prize:
    :return: (hours * rate) * prize
    '''
    try:
        print((float(hours) * float(rate)) + float(prize))
    except Exception as e:
        print(f'Ошибка - {e}!')


if __name__ == '__main__':
    try:
        salary_calculation(argv[2], argv[3], argv[4])
    except IndexError:
        salary_calculation(argv[2], argv[3])
