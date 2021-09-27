"""
1.	Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
"""

print(123)
print(type(123))
print(.123)
print(type(.123))
print('123')
print(type('123'))
print([1,2,3])
print(type([1,2,3]))
print((1,2,3))
print(type((1,2,3)))
print({'a':123,'b':123})
print(type({'a':123,'b':123}))
print({1,2,3})
print(type({1,2,3}))
print(False)
print(type(False))
print(None)
print(type(None))
count=input('Введите что нибудь: ')
print(count)
print(f'Вы ввели вот такой тип переменной: {type(count)}')
print(f'При вводе всегда будет такой тип {type(count)}, нужно приводить к желаемому ???("значение")')