'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. Алгоритм: Слова в строке разделены пробелами, но не обязательно одним пробелом.'''


def count():
    try:
        with open('5_2.txt', 'r', encoding="utf-8") as f_obj:
            line_counter = 0
            for line in f_obj:
                line_counter += 1
                print(f'{line} - Количество слов в строке: {len(line.split())}')
            print(f'Количество строк: {line_counter}')
    except IOError:
        print("Произошла ошибка ввода-вывода!")


count()