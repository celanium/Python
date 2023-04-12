'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''

# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def generator_file3():
    f_file_open = open('3_1.txt', 'w')
    data_list = [
                'Иванов 23543.12',
                'Петров 16659.74',
                'Сидоров 14568.32',
                'Ацтек 24573.75',
                'Фарнух 19159.64',
                'Кузнецов 19359.95',
                'Попов 34956.96',
                'Соколов 68425.73',
                'Михайлов 15457.29',
                'Котов 39856.48',
                ]
    data = [
        f_file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))
    ]
    f_file_open.close()


generator_file3()


def check_salary():
    f_file_open = open('3_1.txt', 'r')
    data = f_file_open.read()
    data_list = data.strip().split('\n')
    data_dict = {
        data_list[list_i].split()[el] : data_list[list_i].split()[el+1]
        for list_i in range(len(data_list))
        for el in range(len(str(list_i).split()))
    }
    list_person = []
    for key, value in data_dict.items():
        if float(value) < 20000.00:
            list_person.append(key)

    return "List people with rate less 20k: " + str(list_person)


print(check_salary())


