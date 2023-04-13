'''5. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Алгоритм: Вам потребуется "разобрать" строку на составляющие, выделить цифры. Обратите внимание, что перед скобками пробелов нет.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''


def extract_hours(hour_string):
    string_val = str(hour_string)
    if string_val.count("(") > 0:
        return int(string_val.split("(", 1)[0])
    else:
        return 0


try:
    subj = {}
    with open('5_6.txt', 'r', encoding="utf-8") as file_obj:
        for line in file_obj:
            subject, lecture, practice, lab = line.split()
            lecture = extract_hours(lecture)
            practice = extract_hours(practice)
            lab = extract_hours(lab)
            subj[subject] = lecture + practice + lab
        print(f'Общее количество часов по предметам - \n {subj}')
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Ошибка значения')