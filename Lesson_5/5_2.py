'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. Алгоритм: Слова в строке разделены пробелами, но не обязательно одним пробелом.'''

def generator_file():
    f_file_open = open('2.txt', 'w')
    data_list = [
                'This', 'method', 'is', 'supplied', 'with', 'the', 'MersenneTwister', 'generator',
                'and', 'some', 'other', 'generators', 'may', 'also', 'provide',
                'it', 'as', 'an', 'optional', 'part', 'of', 'the', 'API2'
                ]
    data = [
        f_file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))
    ]
    f_file_open.close()
generator_file()

def count():
    file_open = open('2.txt', 'r')
    print("Count strings: " + str(len(file_open.readlines())) + ".")
    file_open = open('2.txt', 'r')
    print("Count elements: " + str(len(file_open.read())) + ".")

count()