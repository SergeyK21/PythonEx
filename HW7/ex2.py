"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.

"""
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, dimension):
        self.dimension = dimension

    def fabric_consumption(self):
        return self.dimension / 6.5 + 0.5


class Costume(Cloth):
    def __init__(self, height):
        self.height = height

    def fabric_consumption(self):
        return 2 * self.height + 0.3


class Clothes:
    __fabric_consumption = 0

    def __init__(self, dimension=None, height=None):
        self.height = height
        self.dimension = dimension
        self.list_coat = []
        if self.dimension != None:
            self.list_coat.append(Coat(self.dimension))
            Clothes.__fabric_consumption += self.list_coat[0].fabric_consumption()
        self.list_costume = []
        if self.height != None:
            self.list_costume.append(Costume(self.height))
            Clothes.__fabric_consumption += self.list_costume[0].fabric_consumption()

    def add_coat(self, dimension):
        self.list_coat.append(Coat(dimension))
        Clothes.__fabric_consumption += self.list_coat[len(self.list_coat) - 1].fabric_consumption()

    def add_costume(self, height):
        self.list_costume.append(Costume(height))
        Clothes.__fabric_consumption += self.list_costume[len(self.list_costume) - 1].fabric_consumption()

    @property
    def general_calculation(self):
        return Clothes.__fabric_consumption

    @property
    def quantity_coat(self):
        return len(self.list_coat)

    @property
    def quantity_costume(self):
        return len(self.list_costume)


clothets = Clothes()
clothets.add_coat(200)
clothets.add_costume(300)
clothets.add_coat(100)
clothets.add_coat(120)
clothets.add_coat(340)
clothets.add_costume(234)
clothets.add_costume(123)
print(f'пальто {clothets.quantity_coat} шт.')
print(f'костюмы {clothets.quantity_costume} шт.')
print(clothets.general_calculation)
