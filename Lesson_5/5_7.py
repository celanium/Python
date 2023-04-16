'''7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности,
выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''

import json

profit = {}
pr = {}
profit_sum = 0
prof_aver = 0
lines_count = 0
with open('5_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        print(line)
        name, firm, revenue, loss = line.split()
        profit[name] = float(revenue) - float(loss)
        if profit.setdefault(name) >= 0:
            profit_sum += profit.setdefault(name)
            lines_count += 1
    if lines_count != 0:
        prof_aver = profit_sum / lines_count
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутствует.')
    pr = {'average_profit': round(prof_aver, 2)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('5_7.json', 'w', encoding="utf-8") as output_json:
    json.dump(profit, output_json)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
