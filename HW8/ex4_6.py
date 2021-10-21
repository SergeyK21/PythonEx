"""
4.	Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""
from abc import ABC, abstractmethod
import json
import os
import pickle
import sys
import datetime


class Equipment(ABC):

    @staticmethod
    def save_info(message):
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.now()} - {message}\n')

    @staticmethod
    def get_dict_equipment(name, company, country_manufacturer, serial_number, model):
        return {
            'Наименование': name,
            'Фирма производитель': company,
            'Страна изготовления': country_manufacturer,
            'Серийный номер': serial_number,
            'Модель': model
        }

    @staticmethod
    def equipment_search_by_serial_number(serial_number):
        data_warehouse = []
        if os.path.isfile('printer.json'):
            with open('printer.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
                for el in data:
                    data_warehouse.append(el)
        if os.path.isfile('scanner.json'):
            with open('scanner.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
                for el in data:
                    data_warehouse.append(el)
        if os.path.isfile('mfp.json'):
            with open('mfp.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
                for el in data:
                    data_warehouse.append(el)
        data = []
        for el in data_warehouse:
            if el['Серийный номер'] == serial_number:
                data.append(el)
        if len(data) != 0:
            print('По данному серийномуномеру на складе найдено следующее оборудование:')
            print(data)
        else:
            print('По данному серийному номеру на складе ничего не найдено!')
        data_shop = []
        if os.path.isfile('printer.pickle'):
            with open('printer.pickle', 'rb') as f:
                data = list(pickle.load(f))
                for el in data:
                    data_shop.append(el)
        if os.path.isfile('scanner.pickle'):
            with open('scanner.pickle', 'rb') as f:
                data = list(pickle.load(f))
                for el in data:
                    data_shop.append(el)
        if os.path.isfile('mfp.pickle'):
            with open('mfp.pickle', 'rb') as f:
                data = list(pickle.load(f))
                for el in data:
                    data_shop.append(el)
        data = []
        for el in data_shop:
            if el['Серийный номер'] == serial_number:
                data.append(el)
        if len(data) != 0:
            print('По данному серийномуномеру в магазине найдено следующее оборудование:')
            print(data)
        else:
            print('По данному серийному номеру в магазине ничего не найдено!')

    @abstractmethod
    def add_equipment(self):
        pass

    @abstractmethod
    def delete_equipment(self):
        pass

    @abstractmethod
    def save_to_warehouse(self):
        pass

    @abstractmethod
    def delete_from_warehouse(self):
        pass

    @abstractmethod
    def statistics_output(self):
        pass


class Printer(Equipment):
    """
    Класс 'Принтер'
    """

    def __init__(self):
        """
        Конструктор:
        Открываем файл 'printer.pickle', записываем данные в список self.printer.
        Если файла 'printer.pickle' не существует, то создаем пустой словарь self.printer.

        """
        if os.path.isfile('printer.pickle'):
            with open('printer.pickle', 'rb') as f:
                data = pickle.load(f)
            self.printer = data
        else:
            self.printer = []

    def add_equipment(self, serial_number, company=None, country_manufacturer=None, model=None):
        """
        1 Приверяем существует ли такой серийный номер в листе self.printer.
        2 Если такой серйный номер существует Выводим и Возвращаем сообщение
        3 Если такого серийного номера не существует - Создает словарь 'Принтер' используя статический метод
        'Equipment.get_dict_equipment(name, company, country_manufacturer, serial_number, model)'.
        4 Если такого серийного номера не существует - перезаписываем файл 'printer.pickle'

        :param serial_number:
        :param company:
        :param country_manufacturer:
        :param model:
        :return:
        """
        for el in self.printer:
            if el["Серийный номер"] == serial_number:
                print('Принтер с таким серийным номером существует')
                return 'Принтер с таким серийным номером существует'
        self.printer.append(
            Equipment.get_dict_equipment("Принтер", company, country_manufacturer, serial_number, model))
        with open('printer.pickle', 'wb') as f:
            pickle.dump(self.printer, f)

    def delete_equipment(self, serial_number):
        """
        1 Удаляем из списка self.printer элемент по серийному номеру
        2 Перезаписываем файл
        :param index:
        :return:
        """
        for el in self.printer:
            if el['Серийный номер'] == serial_number:
                self.printer.remove(el)
                with open('printer.pickle', 'wb') as f:
                    pickle.dump(self.printer, f)
                break
        else:
            print('Нет такого оборудования!')

    def save_to_warehouse(self):
        """
        Загрузка данных из файла 'printer.pickle' в файл 'printer.json'.
        Проверка на наличие повторений.
        :return:
        """
        if os.path.isfile('printer.pickle') and len(self.printer) != 0:
            if os.path.isfile('printer.json'):
                with open('printer.json', 'r', encoding='utf-8') as f_json:
                    data = list(json.load(f_json))
                for el in self.printer[:]:
                    if el not in data:  # Проверка на наличие повторений в файле 'printer.json'.
                        data.append(el)
                        self.printer.remove(el)
                with open('printer.json', 'w', encoding='utf-8') as f_json:
                    json.dump(data, f_json, ensure_ascii=False)
                with open('printer.pickle', 'wb') as f:
                    pickle.dump(self.printer, f)
                if len(self.printer) != 0:
                    print('Данные технические средства присутствуют на склааде')
                    print(self.printer)
            else:
                data = []
                for el in self.printer:
                    data.append(el)
                with open('printer.json', 'w', encoding='utf-8') as f_json:
                    json.dump(data, f_json, ensure_ascii=False)
                self.printer.clear()
                with open('printer.pickle', 'wb') as f:
                    pickle.dump(self.printer, f)
        else:
            print('Нет принтеров в наличие!')

    def delete_from_warehouse(self, serial_number):
        if os.path.isfile('printer.json'):
            with open('printer.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
            for el in data:
                if el['Серийный номер'] == serial_number:
                    data.remove(el)
                    break
            with open('printer.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

    def statistics_output(self):
        data = []
        if os.path.isfile('printer.json'):
            with open('printer.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
        print(f'Всего принтеров на складе - {len(data)}')
        print(f'Всего принтеров в магазине - {len(self.printer)}')
        print('На складе:')
        print(data)
        print('В магазине:')
        print(self.printer)


class Scanner(Equipment):
    """
    Класс 'Сканер'
    """

    def __init__(self):
        """
        Конструктор:
        Открываем файл 'scanner.pickle', записываем данные в список self.scanner.
        Если файла 'printer.pickle' не существует, то создаем пустой словарь self.scanner.

        """
        if os.path.isfile('scanner.pickle'):
            with open('scanner.pickle', 'rb') as f:
                data = list(pickle.load(f))
            self.scanner = data
        else:
            self.scanner = []

    def add_equipment(self, serial_number, company=None, country_manufacturer=None, model=None):
        """
        1 Приверяем существует ли такой серийный номер в листе self.scanner.
        2 Если такой серйный номер существует Выводим и Возвращаем сообщение
        3 Если такого серийного номера не существует - Создает словарь 'Сканер' используя статический метод
        'Equipment.get_dict_equipment(name, company, country_manufacturer, serial_number, model)'.
        4 Если такого серийного номера не существует - перезаписываем файл 'scanner.pickle'

        :param serial_number:
        :param company:
        :param country_manufacturer:
        :param model:
        :return:
        """
        for el in self.scanner:
            if el["Серийный номер"] == serial_number:
                print('Сканер с таким серийным номером существует')
                return 'Сканер с таким серийным номером существует'
        self.scanner.append(
            Equipment.get_dict_equipment("Сканер", company, country_manufacturer, serial_number, model))
        with open('scanner.pickle', 'wb') as f:
            pickle.dump(self.scanner, f)

    def delete_equipment(self, serial_number):
        """
        1 Удаляем из списка self.scanner элемент по серийному номеру
        2 Перезаписываем файл
        :param index:
        :return:
        """
        for el in self.scanner:
            if el['Серийный номер'] == serial_number:
                self.scanner.remove(el)
                with open('scanner.pickle', 'wb') as f:
                    pickle.dump(self.scanner, f)
                break
        else:
            print('Нет такого оборудования!')

    def save_to_warehouse(self):
        """
        Загрузка данных из файла 'scanner.pickle' в файл 'printer.json'.
        Проверка на наличие повторений.
        :return:
        """
        if os.path.isfile('scanner.pickle') and len(self.scanner) != 0:
            if os.path.isfile('scanner.json'):
                with open('scanner.json', 'r', encoding='utf-8') as f_json:
                    data = list(json.load(f_json))
                for el in self.scanner[:]:
                    if el not in data:  # Проверка на наличие повторений в файле 'printer.json'.
                        data.append(el)
                        self.scanner.remove(el)
                with open('scanner.json', 'w', encoding='utf-8') as f_json:
                    json.dump(data, f_json, ensure_ascii=False)
                with open('scanner.pickle', 'wb') as f:
                    pickle.dump(self.scanner, f)
                if len(self.scanner) != 0:
                    print('Данные технические средства присутствуют на склааде')
                    print(self.scanner)
            else:
                data = []
                for el in self.scanner:
                    data.append(el)
                with open('scanner.json', 'w', encoding='utf-8') as f_json:
                    json.dump(data, f_json, ensure_ascii=False)
                self.scanner.clear()
                with open('scanner.pickle', 'wb') as f:
                    pickle.dump(self.scanner, f)
        else:
            print('Нет сканеров в наличие!')

    def delete_from_warehouse(self, serial_number):
        if os.path.isfile('scanner.json'):
            with open('scanner.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
            for el in data:
                if el['Серийный номер'] == serial_number:
                    data.remove(el)
                    break
            with open('scanner.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

    def statistics_output(self):
        data = []
        if os.path.isfile('scanner.json'):
            with open('scanner.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
        print(f'Всего сканеров на складе - {len(data)}')
        print(f'Всего сканеров в магазине - {len(self.scanner)}')
        print('На складе:')
        print(data)
        print('В магазине:')
        print(self.scanner)


class Mfp(Equipment):
    """
        Класс 'МФУ'
        """

    def __init__(self):
        """
        Конструктор:
        Открываем файл 'mfp.pickle', записываем данные в список self.mfp.
        Если файла 'mfp.pickle' не существует, то создаем пустой словарь self.mfp.

        """
        if os.path.isfile('mfp.pickle'):
            with open('mfp.pickle', 'rb') as f:
                data = list(pickle.load(f))
            self.mfp = data
        else:
            self.mfp = []

    def add_equipment(self, serial_number, company=None, country_manufacturer=None, model=None):
        """
        1 Приверяем существует ли такой серийный номер в листе self.mfp.
        2 Если такой серйный номер существует Выводим и Возвращаем сообщение
        3 Если такого серийного номера не существует - Создает словарь 'МФУ' используя статический метод
        'Equipment.get_dict_equipment(name, company, country_manufacturer, serial_number, model)'.
        4 Если такого серийного номера не существует - перезаписываем файл 'mfp.pickle'

        :param serial_number:
        :param company:
        :param country_manufacturer:
        :param model:
        :return:
        """
        for el in self.mfp:
            if el["Серийный номер"] == serial_number:
                print('МФУ с таким серийным номером существует')
                return 'МФУ с таким серийным номером существует'
        self.mfp.append(
            Equipment.get_dict_equipment("МФУ", company, country_manufacturer, serial_number, model))
        with open('mfp.pickle', 'wb') as f:
            pickle.dump(self.mfp, f)

    def delete_equipment(self, serial_number):
        """
        1 Удаляем из списка self.mfp элемент по серийному номеру
        2 Перезаписываем файл
        :param index:
        :return:
        """
        for el in self.mfp:
            if el['Серийный номер'] == serial_number:
                self.mfp.remove(el)
                with open('mfp.pickle', 'wb') as f:
                    pickle.dump(self.mfp, f)
                break
        else:
            print('Нет такого оборудования!')

    def save_to_warehouse(self):
        """
        Загрузка данных из файла 'mfp.pickle' в файл 'mfp.json'.
        Проверка на наличие повторений.
        :return:
        """
        if os.path.isfile('mfp.pickle') and len(self.mfp) != 0:
            if os.path.isfile('mfp.json'):
                with open('mfp.json', 'r', encoding='utf-8') as f_json:
                    data = list(json.load(f_json))
                for el in self.mfp[:]:
                    if el not in data:  # Проверка на наличие повторений в файле 'printer.json'.
                        data.append(el)
                        self.mfp.remove(el)
                with open('mfp.json', 'w', encoding='utf-8') as f_json:
                    json.dump(data, f_json, ensure_ascii=False)
                with open('mfp.pickle', 'wb') as f:
                    pickle.dump(self.mfp, f)
                if len(self.mfp) != 0:
                    print('Данные технические средства присутствуют на склааде')
                    print(self.mfp)
            else:
                data = []
                for el in self.mfp:
                    data.append(el)
                with open('mfp.json', 'w', encoding='utf-8') as f_json:
                    json.dump(data, f_json, ensure_ascii=False)
                self.mfp.clear()
                with open('mfp.pickle', 'wb') as f:
                    pickle.dump(self.mfp, f)
        else:
            print('Нет МФУ в наличие!')

    def delete_from_warehouse(self, serial_number):
        if os.path.isfile('mfp.json'):
            with open('mfp.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
            for el in data:
                if el['Серийный номер'] == serial_number:
                    data.remove(el)
                    break
            with open('mfp.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

    def statistics_output(self):
        data = []
        if os.path.isfile('mfp.json'):
            with open('mfp.json', 'r', encoding='utf-8') as f:
                data = list(json.load(f))
        print(f'Всего МФУ на складе - {len(data)}')
        print(f'Всего МФУ в магазине - {len(self.mfp)}')
        print('На складе:')
        print(data)
        print('В магазине:')
        print(self.mfp)


Equipment.save_info('старт')
try:
    command = sys.argv[1]
except IndexError:
    print("Отсутствует название комманды!")
else:
    if command == 'help':
        print('Контроль оборудования: принтеров, сканеров и МФУ')
        print('Команды для управления:')
        print('status_printer - Отчет о состоянии принтеров.')
        print('status_scanner - Отчет о состоянии сканеров.')
        print('status_mfp - Отчет о состоянии МФУ.')
        print('add_printer_shop(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\tНеобязательный параметр:\n'
              '\tФирма производитель,\n'
              '\tСтрана изготовления,\n'
              '\tМодель)\n'
              '\t - добавить принтер в магазин.')
        print('add_scanner_shop(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\tНеобязательный параметр:\n'
              '\tФирма производитель,\n'
              '\tСтрана изготовления,\n'
              '\tМодель)\n'
              '\t - добавить сканер в магазин.')
        print('add_mfp_shop(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\tНеобязательный параметр:\n'
              '\tФирма производитель,\n'
              '\tСтрана изготовления,\n'
              '\tМодель)\n'
              '\t - добавить МФУ в магазин.')
        print('del_printer_shop(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              ' - удалить принтер из магазина.')
        print('del_scanner_shop(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\t - удалить сканер из магазина.')
        print('del_mfp_shop(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\t - удалить МФУ из магазина.')
        print('save_printer_warehouse - добавить принтер из магазина на склад.')
        print('save_scanner_warehouse - добавить сканер из магазина на склад.')
        print('save_mfp_warehouse - добавить МФУ из магазина на склад.')
        print('del_printer_warehouse(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\t - удалить принтер со склада.')
        print('del_scanner_warehouse(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\t - удалить сканер со склада.')
        print('del_mfp_warehouse(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\t - удалить МФУ со склада.')
        print('search_by_serial_number(параметры sys.argv:\n'
              '\tОбязательный параметр:\n'
              '\tСерийный номер\n'
              '\t - поиск по серийному номеру')

    elif command == 'status_printer':
        temp = Printer()
        temp.statistics_output()
        del temp
    elif command == 'status_scanner':
        temp = Scanner()
        temp.statistics_output()
        del temp
    elif command == 'status_mfp':
        temp = Mfp()
        temp.statistics_output()
        del temp
    elif command == 'add_printer_shop':
        try:
            temp = Printer()
            temp.add_equipment(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            del temp
        except IndexError:
            try:
                temp.add_equipment(sys.argv[2], sys.argv[3], sys.argv[4])
                del temp
            except IndexError:
                try:
                    temp.add_equipment(sys.argv[2], sys.argv[3])
                    del temp
                except IndexError:
                    try:
                        temp.add_equipment(sys.argv[2])
                        del temp
                    except IndexError:
                        print('Введите параметры!')
    elif command == 'add_scanner_shop':
        try:
            temp = Scanner()
            temp.add_equipment(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            del temp
        except IndexError:
            try:
                temp.add_equipment(sys.argv[2], sys.argv[3], sys.argv[4])
                del temp
            except IndexError:
                try:
                    temp.add_equipment(sys.argv[2], sys.argv[3])
                    del temp
                except IndexError:
                    try:
                        temp.add_equipment(sys.argv[2])
                        del temp
                    except IndexError:
                        print('Введите параметры!')
    elif command == 'add_mfp_shop':
        try:
            temp = Mfp()
            temp.add_equipment(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            del temp
        except IndexError:
            try:
                temp.add_equipment(sys.argv[2], sys.argv[3], sys.argv[4])
                del temp
            except IndexError:
                try:
                    temp.add_equipment(sys.argv[2], sys.argv[3])
                    del temp
                except IndexError:
                    try:
                        temp.add_equipment(sys.argv[2])
                        del temp
                    except IndexError:
                        print('Введите параметры!')
    elif command == 'del_printer_shop':
        try:
            temp = Printer()
            temp.delete_equipment(sys.argv[2])
            del temp
        except IndexError:
            print('Введите параметры!')
    elif command == 'del_scanner_shop':
        try:
            temp = Scanner()
            temp.delete_equipment(sys.argv[2])
            del temp
        except IndexError:
            print('Введите параметры!')
    elif command == 'del_mfp_shop':
        try:
            temp = Mfp()
            temp.delete_equipment(sys.argv[2])
            del temp
        except IndexError:
            print('Введите параметры!')
    elif command == 'save_printer_warehouse':
        temp = Printer()
        temp.save_to_warehouse()
        del temp
    elif command == 'save_scanner_warehouse':
        temp = Scanner()
        temp.save_to_warehouse()
        del temp
    elif command == 'save_mfp_warehouse':
        temp = Mfp()
        temp.save_to_warehouse()
        del temp
    elif command == 'del_printer_warehouse':
        try:
            temp = Printer()
            temp.delete_from_warehouse(sys.argv[2])
            del temp
        except IndexError:
            print('Введите параметры!')
    elif command == 'del_scanner_warehouse':
        try:
            temp = Scanner()
            temp.delete_from_warehouse(sys.argv[2])
            del temp
        except IndexError:
            print('Введите параметры!')

    elif command == 'del_mfp_warehouse':
        try:
            temp = Mfp()
            temp.delete_from_warehouse(sys.argv[2])
            del temp
        except IndexError:
            print('Введите параметры!')
    elif command == 'search_by_serial_number':
        try:
            Equipment.equipment_search_by_serial_number(sys.argv[2])
        except IndexError:
            print('Введите параметры!')
    else:
        print("Нет такой команды!")
Equipment.save_info('стоп')
