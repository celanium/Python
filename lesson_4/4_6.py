'''6. Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.'''

from itertools import cycle, count

start_number = int(input('Начальное число: '))
end_number = start_number + 25

# 1
for i in count(start_number):
    if i < end_number:
        print(i)
    else:
        break
print ("2nd option")
# 2
my_list = [i for i in range(end_number)]
print(my_list)
count = 0
for value in cycle(my_list):
    if count < end_number + 10:
        print(value)
        count += 1
    else:
        break