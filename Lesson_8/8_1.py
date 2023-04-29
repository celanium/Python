'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_date(cls, date_str):
        try:
            day, month, year = map(int, date_str.split("-"))
            return day, month, year
        except ValueError:
            print(f"Ошибочная строка {date_str}")


    @staticmethod
    def validate_date(day, month, year):
        if not 1 <= day <= 31:
            return False
        if not 1 <= month <= 12:
            return False
        if year < 1900 or year > 2100:
            return False
        return True


def check_date(date_str):
    try:
        day, month, year = Date.extract_date(date_str)
        if Date.validate_date(day, month, year):
            print(f"Дата {date_str} верна")
        else:
            print(f"Неверный формат даты {date_str}")
    except TypeError:
        print(f"Ошибочная строка {date_str}")


check_date("25-04-2023")
check_date("25-04-1423")
check_date("25-04-2223")
check_date("25-223")