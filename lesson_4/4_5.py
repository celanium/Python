'''5. Реализовать формирование списка, используя функцию range()
и возможности генератора. В список должны войти чётные числа от 100 до 1000
(включая границы). Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''

from functools import reduce


def mult(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


initial_list = [i for i in range(100, 1000) if i % 2 == 0]
summa = reduce(mult, initial_list)
print(summa)
