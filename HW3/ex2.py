"""
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def foo(name, surname, year_of_birth, city_of_residence, email, tel_number):
    """
    Осуществляет вывод данных о пользователе одной строкой.

    :param name:
    :param surname:
    :param year_of_birth:
    :param city_of_residence:
    :param email:
    :param tel_number:
    :return:str({
        'Имя': name,
        'Фамилия': surname,
        'Год рождения': year_of_birth,
        'Город проживания': city_of_residence,
        'email': email,
        'Номер телефона': tel_number
    })
    """
    return str({
        'Имя': name,
        'Фамилия': surname,
        'Год рождения': year_of_birth,
        'Город проживания': city_of_residence,
        'email': email,
        'Номер телефона': tel_number
    })


if __name__ == '__main__':
    print(foo("Клим", "Чугункин", 1905, "Москва", None, '01'))
