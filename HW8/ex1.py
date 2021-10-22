"""
1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, str_date=None):
        self.str_date = str_date

    @classmethod
    def method_1(cls, str_date):
        list_date = str(str_date).split('-')
        if len(list_date) != 3:
            raise MyError('Неверный формат!')
        try:
            list_date[0] = int(list_date[0])
            if list_date[0] < 0 or list_date[0] > 31:
                raise MyError("Нест такой даты!")
            list_date[1] = int(cls().method_2(list_date[1]))
            list_date[2] = int(list_date[2])
            print(f'{list_date[0]:02}.{list_date[1]:02}.{list_date[2]:04}')
        except Exception as ex:
            print(f'Ошибка - {ex}')

    @staticmethod
    def method_2(str_month):
        str_month = str(str_month).lower()
        dict_month = {
            'янв': 1,
            'фев': 2,
            'мар': 3,
            'апр': 4,
            'мая': 5,
            'июн': 6,
            'июл': 7,
            'авг': 8,
            'сен': 9,
            'окт': 10,
            'ноя': 11,
            'дек': 12
        }
        for key, val in dict_month.items():
            if key in str_month:
                return val
        else:
            raise MyError('Нет такого месяца')


date = Date()
date.method_1("1 - янв - 2021")
