'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и
WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Алгоритм:
- метод turn(direction) должен иметь аргумент - направление поворота.
- Ограничение по скорости должно быть атрибутом класса(какого) или экземпляра?

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


# вариант 1

class Car:
    _name = None
    _speed = None
    _color = None
    _is_police = False

    def __init__(self, name, color, is_police=False):
        self._name = name
        self._speed = 0
        self._color = color
        self._is_police = is_police

    def go(self, speed):
        self._speed = speed
        return "Машина поехала со скоростью " + str(speed)

    def stop(self):
        self._speed = 0
        return "Машина остановилась"

    def turn(self, direction):
        return "машина повернула на" + direction

    def show_speed(self):
        return "Скорость машины: " + str(self._speed)


class TownCar(Car):
    #  Количество посадочных мест
    __seats = None
    __speed_limit = 60

    def __init__(self, name, color, seats):
        super().__init__(name, color)
        self.__seats = seats

    def show_speed(self):
        if self._speed > self.__speed_limit:
            print(
                f"Скорость {self._speed} превысила допустимый лимит! {self.__speed_limit}")
        return super().show_speed()


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)


class WorkCar(Car):
    __speed_limit = 40

    def __init__(self, name, color, is_police):
        super().__init__(name, color, is_police)

    def show_speed(self):
        if self._speed > self.__speed_limit:
            print(
                f"Скорость {self._speed} превысила допустимый лимит! ({self.__speed_limit})")
        return super().show_speed()


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)


honda = TownCar('Honda', 'blue', 5)
print(honda._name, honda._color, honda._speed, honda._is_police)
print(honda.go(60), honda.turn('лево'), honda.show_speed(), honda.stop(),
      honda.show_speed())
print(honda.go(100), honda.turn('лево'), honda.show_speed(), honda.stop(),
      honda.show_speed())
sportcar = SportCar('Ferrari', 'red')
print(sportcar.go(120), sportcar.turn("право"), sportcar.show_speed(),
      sportcar.stop())
workcar1 = WorkCar('Lada', 'white', True)
print(workcar1.go(100), workcar1.turn('лево'), workcar1.show_speed(),
      workcar1.stop())
print(workcar1.go(35), workcar1.turn('лево'), workcar1.show_speed(),
      workcar1.stop())
workcar2 = WorkCar('Hyundai', 'yellow', False)
print(workcar2.go(100), workcar2.turn('право'), workcar2.show_speed(),
      workcar2.stop())
police = PoliceCar('Lada', 'black')
print(police._name, police._color, police._speed, police._is_police)
print(police.go(100), police.turn('лево'), police.show_speed(), police.stop())
print(police._name, police._color, police._speed, police._is_police)
