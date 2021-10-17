"""
4.	Реализуйте базовый класс Car.

●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            self.str_1 = "Полицейский"
        else:
            self.str_1 = "Не полицейский"

    def go(self):
        print(f"{self.str_1} автомобиль {self.name}, {self.color} цвета, поехал")

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул - {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч - Превышение скорости!')
        else:
            print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч - Превышение скорости!')
        else:
            print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(61, "red", "Gaz", False)
tc.go()
tc.turn("на лево")
tc.show_speed()
tc.stop()
print()
wc = WorkCar(41, "blue", "Kamaz", False)
wc.go()
wc.turn("на право")
wc.show_speed()
wc.stop()
print()
sc = SportCar(150, "желтого", "Пежо", False)
sc.go()
sc.turn("на право")
sc.show_speed()
sc.stop()
print()
pc = SportCar(170, "синего", "Уаз", True)
pc.go()
pc.turn("на лево")
pc.show_speed()
pc.stop()