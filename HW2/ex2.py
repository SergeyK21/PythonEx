"""
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""
print('Заполните список! \nДля остановки заполнения введите слово - "стоп"\n')
count = 1
temp = input(f'Введите {count} элемент - ')
listtt = []
while temp != 'стоп':
    listtt.append(temp)
    count += 1
    temp = input(f'Введите {count} элемент - ')
if len(listtt) != 0:
    print('до')
    print(listtt)
    # Тернарным оператором опреднляем является ли кол-во объектов четным или не четным
    # Если четное то len(listtt) оставляем без изменений, в противном случае из len(listtt) - 1
    # Ставим в "pange()" шаг = 2
    for i in range(0, len(listtt) if len(listtt) % 2 == 0 else len(listtt) - 1, 2):
        listtt[i], listtt[i + 1] = listtt[i + 1], listtt[i]  # Крутая штука!
    print('после')
    print(listtt)
else:
    print('Вы ничего не ввели!')