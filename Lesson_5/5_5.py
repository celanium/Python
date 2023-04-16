'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
Алгоритм: Сначала создать файл и записать в него данные, затем его прочитать и выполнить подсчет суммы.'''


def summary():
    filename = '5_5_new.txt'
    try:
        with open(filename, 'w+', encoding="utf-8") as file_write:
            line = '1 2 4 5 5 6 3 66 6 63 3 3 2\n'
            file_write.writelines(line)
        with open(filename, 'r', encoding="utf-8") as file_read:
            for line in file_read:
                my_numb = line.split()
                print(f'Сумма: {sum(map(int, my_numb))}')
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка значения')


summary()