"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
try:
    with open('test_ex3.txt', 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
    salary_rms = []
    for el in content:
        list_el = el.split()
        salary_rms.append(float(list_el[1]))
        if (float(list_el[1]) < 20000):
            print(f'{list_el[0]} - получает меньше 20000')
    print(f'Средняя величина дохода сотрудников: {sum(salary_rms) / len(salary_rms):.2f}')
except Exception as ex:
    print(f'Ошибка - {ex}')


