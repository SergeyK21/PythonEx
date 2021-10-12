"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""
with open("text_ex2.txt", 'r', encoding='utf-8') as f_obj:
    list_content = f_obj.readlines()
sum_words = 0
print(f'Колличество строк: {len(list_content)}')
for i, temp in enumerate(list_content, 1):
    sum_words += len(temp.split())
    print(f'{i} строка - {len(temp.split())} (слов)')


print(f'Всего в файле слов {sum_words}')
