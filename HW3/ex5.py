"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def foo(sum_num, str_oka):
    """
    Сумма вновь введенных чисел + sum_num
    :param sum_num:
    :param str_oka:
    :return: ('',sum_num)
    """
    try:
        list_sum_num = str(str_oka).split()
        for ls in list_sum_num:
            if ls != 'стоп':
                sum_num += int(ls)
            else:
                return ('стоп', sum_num)
        else:
            return ('поехали еще', sum_num)
        return ('стоп', sum_num)
    except Exception as e:
        return (f"Ошибка - {e}", sum_num)


if __name__ == '__main__':
    flag = True
    sum_num = 0
    while (flag):
        flag = False
        str_oka = input('Введите числа разделяя их пробелом \n(для продолжения нажмите "enter", для очтановки наберите слово "стоп"): ')
        kortezg = foo(sum_num, str_oka)
        sum_num = kortezg[1]
        if kortezg[0] == 'поехали еще':
            print(f'Общая сумма = {sum_num}')
            flag = True
        else:
            print(f'Общая сумма = {sum_num}')
            print(f'Причина выхода: {kortezg[0]}')
