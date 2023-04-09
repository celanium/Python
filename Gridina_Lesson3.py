'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def divide(*args):
    if len(args) == 0:
        return "нет входных параметров!"
    try:
        res = args[0] / args[1]
    except ZeroDivisionError:
        return "Нельзя делить на ноль!"
    return res


try:
    arg1 = int(input("Введите делимое "))
    arg2 = int(input("Введите делитель "))
    print(f'Результат:  {divide(arg1, arg2)}')
except ValueError:
    print('Ошибка значения')

'''2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.'''

name_param = input('Введите имя')
surname_param = input('Введите фамилию')
year_param = int(input('Введите год рождения'))
city_param = input('Введите город проживания')
email_param = input('Введите электронную почту')
phone_param = input('Введите номер телефона')


def my_func(name, surname, year, city, email, phone):
    return ' '.join([str(name), str(surname), str(year), str(city), str(email),
                     str(phone)])


print(my_func(surname=surname_param, name=name_param, year=year_param,
              city=city_param, email=email_param, phone=phone_param))


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.


def my_func(*args):
    try:
        if len(args) > 3:
            print("Слишком много чисел")
            return
        max_list = []
        for x in args:
            max_list.append(int(x))
        sorted_list = sorted(max_list, reverse=True)
        print(sorted_list)
        max1 = sorted_list[0]
        max2 = sorted_list[1]
        print (f'''max1 - {max1} max2 - {max2}''')
        return max1 + max2
    except ValueError:
        print('Ошибка значения')


print(f'''Результат - {my_func(input("Введите 1 число "),
                               input("Введите 2 число "), input("Введите 3 число "))}''')

'''4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.'''


def my_func(x, y):
    try:
        value = int(x)
        power = int(y)
        result = 1
        if power == 0:
            return result
        for x in range(power):
            result *= value
        return result
    except ValueError:
        print('Ошибка значения')


print(f'''Результат - {my_func(input("Введите 1 число "),
                               input("Введите 2 число "))}''')

'''5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться 
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ 
введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''

sum_of_numbers = 0
exit_asked = False
while not exit_asked:
    number_list = input(
        'Введите числа, разделенные пробелом, или x для выхода').split()
    sum_of_current_input = 0
    for number in number_list:
        if number.lower() == 'x':
            exit_asked = True
            break
        else:
            try:
                value = int(number)
                sum_of_current_input += value
            except ValueError:
                print(f'Ошибка значения {number}')
    sum_of_numbers += sum_of_current_input
    print(f'Текущая сумма {sum_of_numbers}')
print(f'Финальная сумма {sum_of_numbers}')


'''6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
Перевести первую букву каждого слова в верхний регистр, остальные - в нижний
print("ехал грека через реку".title())
-> Ехал Грека Через Реку'''


def int_func(word):
    return str(word).title()


print(int_func(input("Введите слово:")))


'''7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().'''


def format_words(words):
    res = ""
    for word in str(words).split():
        res += int_func(word)
    return res


print(int_func(input("Введите слова, разделенные пробелами:")))

