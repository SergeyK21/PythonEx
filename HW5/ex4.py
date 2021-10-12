"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.\
"""
with open('text_ex4.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
numbers_dict = {
    '1': 'Один',
    '2': 'Два',
    '3': 'Три',
    '4': 'Четыре',
}
new_content = []
for el in content:
    list_el = el.split()
    list_el[0] = numbers_dict[list_el[2]]
    list_el.append('\n')
    new_content.append(' '.join(list_el))
with open('new_text_ex4.txt', 'w', encoding='utf-8') as new_f_obj:
    new_f_obj.writelines(new_content)
