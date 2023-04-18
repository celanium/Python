'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет), метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать running переключение светофора в режимы: красный, желтый, зеленый
- печать на экран текущего цвета сфетофора. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Алгоритм:
- Подумайте должен ли атрибут color быть атрибутом класса или атрибутом экземпляра.
- Используйте функцию sleep пакета time для формирования задержки
- ВЫ можете использовать итератор по цветам или метод running может принимать аргумент - цвет, на который надо переключиться, тогда задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
- Попробуйте связать в одну структуру данных цвета и время задержек'''

#вариант1

from time import sleep
from datetime import datetime as dt


class TrafficLight:
    """ Класс светофора, реализующий свое переключение при запуске running( """
    _states = {'red': 7, 'yellow': 2, 'green': 10}
    _color = ''

    def running(self):
        """ Метод запусключения светофора """
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self._color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self._color}' after" 
                  f"{(dt.now() - start_state_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()

#вариант 2

from time import sleep
class TrafficLight:
    # 7 + 2 + 6
    try:
        i_rate = int(input("How many reps? (One cycle - 15 sec. Cycle can't be more than 30 ): ->>> "))
        if i_rate > 30:
            raise BaseException
    except BaseException:
        print("Error. Please, enter to int number.")
        exit(-1)

    __color = ('red', 'yellow', 'green')

    def running(self):
        i_cycle = 0

        while i_cycle < self.i_rate:
            i_cycle += 1
            i_text = "The traffic light is now on:"

            for i_color in TrafficLight.__color:
                if i_color == 'red':
                    print(i_text, i_color)
                    sleep(7)
                elif i_color == 'yellow':
                    print(i_text, i_color)
                    sleep(2)
                elif i_color == 'green':
                    print(i_text, i_color)
                    sleep(6)
                else:
                    print("Error. Please restart program.")
                    exit(-1)

TrafficLight().running()

#вариант 3

import time
class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i=0
        while i<5:
            for el in TrafficLight._colors :
                print(el)
                i+=1
                time.sleep(1)

traffic = TrafficLight()
traffic.running()