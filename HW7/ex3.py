"""
3)	Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12,
количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15,
количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

"""


class Organic_cell:
    def __init__(self, cell):
        self.__cell = cell

    @property
    def cell(self):
        return self.__cell

    @cell.setter
    def cell(self, cell):
        self.__cell = cell

    def __add__(self, other):
        return Organic_cell(self.__cell + other.cell)

    def __sub__(self, other):
        if (self.__cell >= other.cell):
            return Organic_cell(self.__cell - other.cell)
        else:
            raise Exception('Отрицательное значение при вычитании!')

    def __mul__(self, other):
        return Organic_cell(self.__cell * other.cell)

    def __truediv__(self, other):
        return Organic_cell(int(round(self.__cell / other.cell, 0)))

    def make_order(self, row, other=None):
        if other == None:
            str_1 = ''.join(('*' for el in range(self.__cell)))
            for i in range(0, len(str_1), row):
                print(str_1[i:i + row])
        else:
            str_1 = ''.join(('*' for el in range(other.cell)))
            for i in range(0, len(str_1), row):
                print(str_1[i:i + row])


oc = Organic_cell(15)
oc_1 = Organic_cell(12)
oc.make_order(5)
print()
oc.make_order(5, oc_1)
print()
oc.make_order(5, oc - oc_1)
print()
oc.make_order(10, oc + oc_1)
print()
oc.make_order(20, oc * oc_1)
print()
oc.make_order(20, oc / oc_1)