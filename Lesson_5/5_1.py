'''Основная цель практического задания - работа с файлами: корректное открытие и закрытие. Считывание и запись данных.
В этом задании вы будеет создавать свои файлы данных, обязательно прикрепляйте их, когда сдаете ПЗ.
Если в условии не указано "ввод данных пользователем/с клавиатуры" - можно занести нужные данные сразу в код программы.
Всегда указывайте кодировки при открытии файла на чтение/запись.тарайтесь использовать оптимальный (по расходу памяти) алгоритм.
Не загружайте весь файл в память без необходимости, используйте итератор по строкам.
Больше используйте менеджеры контекста для работы с файлами.

1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

file_open = open('1.txt', 'w')
while True:
    text_line = str(input("Input text line: \n"))
    if text_line == "print":
        file_open = open('1.txt', 'r')
        print("\nPrint file:\n----------\n" + file_open.read() + "---------- \nEnd file.")
        break
    elif not text_line:
        print("Exit.\n")
        break
    elif text_line:
        file_open.write(text_line + "\n")
file_open.close()