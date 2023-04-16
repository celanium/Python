'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''


def check_salary():
    try:
        with open('5_3.txt', 'r', encoding="utf-8") as file_open:
            count_employee = 0
            sum_wage = 0
            print('Оклад меньше 20000:')
            for line in file_open:
                data = line.split()
                wage = float(data[1])
                sum_wage += wage
                count_employee += 1
                if wage < 20000.00:
                     print(data[0])
            print(
                f'Средняя величина дохода сотрудников: {sum_wage / count_employee:.2f}')
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    except ZeroDivisionError:
        print("В файле нет сотрудников")
    except ValueError:
        print("Ошибка преобразования числа из файла")


check_salary()
