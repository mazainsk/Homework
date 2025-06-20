def palindrome (in_str=''):
    if len(in_str) < 2:
        return 0, 0, ''
    else:
        pal_counter = 0
        substr_len = len(in_str)
        sub_str = ''
        while substr_len > 1:
            i = substr_len // 2     # длина половинки подстроки для проверки на палиндром
            # начальная позиция левой части подстроки в исходной стоке
            lps = 0
            # начальная позиция правой части подстроки в исходной стоке
            rps = lps + substr_len // 2
            if substr_len % 2 != 0:    # если длина подстроки нечетная, то нужно сместить нач.поз-ю ее правой части на 1
                rps += 1
            sub_str_shifts = len(in_str) - substr_len       # количество циклов сдвига подстроки в строке
            for j in range(0, sub_str_shifts + 1):
                sub_str_1 = in_str[lps + j:lps + j + i]
                sub_str_2 = in_str[rps + j:rps + j + i]
                sub_str_3 = sub_str_2[-1::-1]
                # print(in_str, substr_len, sub_str_1, sub_str_2, end='') # контрольный вывод в консоль
                if sub_str_1 == sub_str_3:
                    pal_counter += 1
                    sub_str = in_str[lps + j : lps + j + substr_len]
                    # print(' -->', sub_str, end='')        # контрольный вывод в консоль
                # print()       # контрольный вывод в консоль
            if pal_counter != 0:
                return pal_counter, len(sub_str), sub_str
            substr_len -= 1
        return 0, 1, ''


pal_str = input('Введите строку для поиска палиндромов: ')
i, j, pal_str = palindrome(pal_str)
if i == j == 0:
    print('Слишком короткая строка')
elif i == 0 and j == 1:
    print('Нет палиндрома длиннее, чем один символ')
else:
    results_message = 'Найден'
    i_str = str(i)
    i_count = int(i_str[-1])
    if i_count > 1:
        results_message += 'о'
    results_message += ' ' + str(i) + ' палиндром'
    if 1 < i_count < 5:
        results_message += 'а'
    elif i_count >= 5 or i_count == 0:
        results_message += 'ов'
    print(results_message, 'длиной', j)
    if i > 1:
        print('Последний из них ', end='')
    print(pal_str)