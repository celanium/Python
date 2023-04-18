'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''

#вариант 1

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} ton for the building')

road_to_village = Road(20000, 6)
road_to_village.intake()

#вариант 2

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        return self._length * self._width
        # depth, heft


class MassAsphalt(Road):
    pass


i_vars = MassAsphalt(20, 5000).square()
print(i_vars)

#вариант 3

class Road:
    """ Класс дорожного полотна """
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _surface_spec_gravity: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        """
        :param length: Длина дорожного полотна в метрах
        :param width: Ширина дорожного полотна в метрах
        """
        self._length = float(length)
        self._width = float(width)

    def get_surface_gravity(self, thickness: float) -> [float, None]:
        """ Рассчет массы дорожного полотна заданной толщина
        :param thickness: Толщина дорожного покрытия в сантиметрах
        :return: Масса дорожного полотна в тоннах если все ОК, иначе None
        """
        try:
            return (self._length * self._width
                    * thickness * self._surface_spec_gravity)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(5000, 10)
        print(
            'Масса дорожного покрытия составит:',
            road.get_surface_gravity(20),
            'тонн'
        )
    except TypeError:
        print('класс Road требует 2 позиционных аргумента')
