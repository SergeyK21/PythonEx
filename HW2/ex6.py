"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами,
то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
Тогда значение — список значений-характеристик, например, список названий товаров.

Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""
check = input('Ввести товар?(да/нет): ')
count = 1
cpicok = []
try:
    while check != 'нет':
        cpicok.append((count, {
            'название': input('Введите название: '),
            'цена': float(input('Введите цену: ')),
            'колличество': int(input('Введите колличество: ')),
            'ед': input('Введите единицы: ')
        }))
        count += 1
        check = input('Ввести еще товар?(да/нет): ')
except ValueError:
    print('Ошибка! Неверный формат ввода!')
else:
    """
    cpicok = [(1, {'название': 'компьютер', 'цена': 20000, 'колличество': 5, 'eд': 'шт.'}),
              (2, {'название': 'принтер', 'цена': 6000, 'колличество': 2, 'eд': 'шт.'}),
              (3, {'название': 'сканер', 'цена': 2000, 'колличество': 7, 'eд': 'шт.'})
              ]
    """
    name = []
    price = []
    number_of = []
    units = []
    for cp in cpicok:
        name.append(cp[1]['название']),
        price.append(cp[1]['цена']),
        number_of.append(cp[1]['колличество']),
        units.append(cp[1]['eд'])
    units = list(set(units))
    new_cpicok = {
        "название": name,
        "цена": price,
        "колличество": number_of,
        "ед": units
    }
    print(f'“название”:    {new_cpicok["название"]}')
    print(f'“цена”:        {new_cpicok["цена"]}')
    print(f'“колличество”: {new_cpicok["колличество"]}')
    print(f'“ед”:          {new_cpicok["ед"]}')
