'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
необходимо запускать скрипт с параметрами.'''
from sys import argv

if len(argv) > 1:
    name_script, worktime, rate, bonus = argv
    worktime = int(worktime)
    rate = int(rate)
    bonus = int(bonus)
    print((worktime * rate) + bonus)
else:
    worktime = int(input("Введите выработку в часах: "))
    rate = int(input("Введите почасовую ставку: "))
    bonus = int(input("Введите премию: "))
    print((worktime * rate) + bonus)