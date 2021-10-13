"""
1.	Создать класс TrafficLight (светофор).

●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.


"""
import time


class TrafficLight:
    __color = None

    def runing(self, color=None):
        TrafficLight.__color = color
        if TrafficLight.__color == "Красный":
            print(f'{TrafficLight.__color}')
            time.sleep(7)
            TrafficLight.__color = "Желтый"
            print(f'{TrafficLight.__color}')
            time.sleep(2)
            TrafficLight.__color = "Зеленый"
            print(f'{TrafficLight.__color}')
            time.sleep(5)
        elif TrafficLight.__color == "Желтый":
            print(f'{TrafficLight.__color}')
            time.sleep(2)
            TrafficLight.__color = "Красный"
            print(f'{TrafficLight.__color}')
            time.sleep(7)
            TrafficLight.__color = "Зеленый"
            print(f'{TrafficLight.__color}')
            time.sleep(5)
        elif TrafficLight.__color == "Зеленый":
            print(f'{TrafficLight.__color}')
            time.sleep(5)
            TrafficLight.__color = "Желтый"
            print(f'{TrafficLight.__color}')
            time.sleep(2)
            TrafficLight.__color = "Красный"
            print(f'{TrafficLight.__color}')
            time.sleep(7)
        elif not TrafficLight.__color:
            TrafficLight.__color = "Красный"
            print(f'{TrafficLight.__color}')
            time.sleep(7)
            TrafficLight.__color = "Желтый"
            print(f'{TrafficLight.__color}')
            time.sleep(2)
            TrafficLight.__color = "Зеленый"
            print(f'{TrafficLight.__color}')
            time.sleep(5)
        else:
            print("Введите 'Касный', 'Желтый' или 'Зеленый'!")


a = TrafficLight()
a.runing("Красный")
