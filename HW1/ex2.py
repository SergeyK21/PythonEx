"""
2.	Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
try:
    second = int(input('Введите секунды: '))
except (ValueError):
    print('Введите натуральное положительное число!')
else:
    print(f'Вы ввели: {(second // 60) // 60}:{(second // 60) % 60}:{second % 60} (часы:минуты:секунды)')