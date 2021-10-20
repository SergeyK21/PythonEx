"""
4.	Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Equipment:

    def __init__(self, name, company=None, country_manufacturer=None, serial_number=None, model=None):
        self.Equipment = {
            'Наименование': name,
            'Фирма производитель': company,
            'Страна изготовления': country_manufacturer,
            'Серийный номер': serial_number,
            'Модель': model
        }


class Printer(Equipment):
    def __init__(self):
        self.printer = []

    @property
    def printer(self):
        return self.printer

    @printer.setter
    def printer(self, company=None, country_manufacturer=None, serial_number=None, model=None):
        self.printer.append(Equipment('Принтер', company, country_manufacturer, serial_number, model))


class Scanner(Equipment):
    def __init__(self):
        self.scanner = []

    @property
    def scanner(self):
        return self.quantity

    @scanner.setter
    def scanner(self, company=None, country_manufacturer=None, serial_number=None, model=None):
        self.scanner.append(Equipment('Сканер', company, country_manufacturer, serial_number, model))


class MFP(Equipment):
    def __init__(self):
        self.mfp = []

    @property
    def mfp(self):
        return self.mfp

    @mfp.setter
    def quantity(self, company=None, country_manufacturer=None, serial_number=None, model=None):
        self.mfp.append(Equipment('МФУ', company, country_manufacturer, serial_number, model))
