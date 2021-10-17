"""
2.	Реализовать класс Road (дорога).

●	определить атрибуты: length (длина), width (ширина);
●	значения атрибутов должны передаваться при создании экземпляра класса;
●	атрибуты сделать защищёнными;
●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
●	проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


class Road:
    _width = None
    _length = None

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    def asphalt_mass(self, weight=25, thickness=5):
        return f'{Road._width} м*{Road._length} м*{weight} кг*{thickness} см = {(Road._width * Road._length * weight * thickness)/1000:.0f} т.'


road = Road(5000, 20)
print(road.asphalt_mass())
