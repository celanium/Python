'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Алгоритм:
- метод turn(direction) должен иметь аргумент - направление поворота.
- Ограничение по скорости должно быть атрибутом класса(какого) или экземпляра?

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''

#вариант 1

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car went"
    def stop(self):
        return "The car has stopped"
    def turn(self, direction):
        return "The car turned to " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Ford', 60, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Ford', 180, 'red')
work1 = WorkCar('Ford', 90, 'white', True)
work2 = WorkCar('Audi', 90, 'white', False)
police = PoliceCar('Ford', 180, 'red')

#вариант 2

class Car:

    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = bool(is_police)
            # if (not self.speed or len(self.speed) <= 0) or \
            #         (not self.color or len(self.color) <= 0) or \
            #         (not self.name or len(self.name) <= 0) or \
            #         not bool(self.is_police):
            #     raise BaseException
        except BaseException:
            return "Error. Please, enter data."
            exit(-1)

    def go(self):
        return "Go."

    def stop(self):
        return "Stop."

    def turn_left(self):
        return "Turn left."

    def turn_right(self):
        return "Turn right."

    def show_speed(self):
        print("Machine normal speed.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Over speed."
        else:
            return "Normal speed"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Over speed."
        else:
            return "Normal speed"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


toyota = SportCar(100, 'Red', 'Toyota', False)
mazda = TownCar(30, 'White', 'Mazda', True)
suzuki = WorkCar(70, 'Rose', 'Suzuki', False)
honda = PoliceCar(110, 'Blue',  'honda', True)


print(toyota.turn_left())
print(mazda.turn_right())
print(suzuki.stop())
print(honda.go())
print(suzuki.is_police)
print(honda.is_police)
print(suzuki.show_speed())
print(honda.show_speed())

#вариант 3

""" Показать текущуую скорость """
        print(f'My speed is {self.speed} km/h')

        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Over speed on {self.speed - self._max_granted_speed} km/h')

    @property
    def direction(self):
        """ Показать текущее направление """

class TownCar(Car):
    """ Класс городских автомобилей """

    # максимальная скорость движения
    _max_granted_speed = 60

    def __init__(self, *args):
        """
        :param args: Параметры авто
        """
        super().__init__(*args)

    def show_speed(self):
        """ Показать скорость авто, и если
        превышена так же сообщить об этом """
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class SportCar(Car):
    """ Класс спортивный автомобилей """
    def __init__(self, *args):
        """
        :param args: Параметры авто
        """
        super().__init__(*args)
    pass


class WorkCar(Car):
    """ Класс авто для работы """

    # максимальная скорость движения
    _max_granted_speed = 40

    def __init__(self, *args):
        """
        :param args: Параметры авто
        """
        super().__init__(*args)

    def show_speed(self):
        """ Показать скорость авто, и если
        превышена так же сообщить об этом """
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class PoliceCar(Car):
    """ Класс полицейского авто """
    def __init__(self, *args):
        """
        :param args: Параметры авто
