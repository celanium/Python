'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

#вариант 1

class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{self.title} чертит")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{self.title} рисует")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()

#вариант 2

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering.")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Pen"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Pencil"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Handle"


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

#вариант 3

class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()