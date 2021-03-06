"""
3.	Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.

"""


class MyException:
    @staticmethod
    def my_try_catch(str_1):
        if str_1.isdigit():
            return int(str_1)
        elif 'stop' == str_1:
            return 'stop'
        else:
            print('Это не число!')
            return None


my_list = []
temp = MyException.my_try_catch(input(f"Введите число: "))
while temp != 'stop':
    if temp:
        my_list.append(temp)
    temp = MyException.my_try_catch(input(f"Введите число: "))

print(my_list)
