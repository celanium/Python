'''7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.'''

from itertools import count
from math import factorial


def factorial_generator():
    for el in count(1):
        yield factorial(el)


generator = factorial_generator()
n = 0
for i in generator:
    if n < 11:
        print(i)
        n += 1
    else:
        break
