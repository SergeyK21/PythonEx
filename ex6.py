"""
6.	Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

"""
try:
    kilometers_first_day = int(input(f'Введите сколько километров спортсмен пробежал в первый день: '))
    kilometers = int(input(f'Сколько километров должен бегать спортсмен: '))
    list_kilometers = []
    count = 0
    while kilometers_first_day < kilometers:
        count += 1
        list_kilometers.append(f'{count}-й день: {kilometers_first_day:.2f}')
        kilometers_first_day += kilometers_first_day * 0.1
    else:
        count += 1
        list_kilometers.append(f'{count}-й день: {kilometers_first_day:.2f}')
    print('Результат:')
    for ls in list_kilometers:
        print(ls)
    print(f'Ответ: на {len(list_kilometers)}-й день спортсмен достиг результата — не менее {kilometers} км.')
except ValueError:
    print("Ошибка!")
