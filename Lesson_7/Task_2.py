'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod

from typing import Any


class AbstractClothes(ABC):
    #  Интерфейс одежды

    @property
    @abstractmethod
    def fabric_required(self):
        pass

    @property
    @abstractmethod
    def size(self):
    #  Общая размерность одежды
        pass

    @abstractmethod
    def _calculate_fabric(self):
    #  подсчет количества ткани
        pass


class Clothes(AbstractClothes):
    _clothes = []

    #  Одежда

    def __init__(self, name: str, size: Any):
        self.name = name
        self._size = size
        self._fabric_required = None

        self._clothes.append(self)

    def _calculate_fabric(self):
        raise NotImplemented

    @property
    def fabric_required(self) -> float:
    #  Расход ткани
        if not self._fabric_required:
            self._calculate_fabric()

        return self._fabric_required

    @property
    def size(self) -> Any:
    #  Узнать размер
        return self._size

    @size.setter
    def size(self, size: Any):
    # Задать размер пальто
        self._size = size
        self._fabric_required = None

    @property
    def total_fabric_required(self):
    # Определить количество ткани на всю одежду
        return sum([item.fabric_required for item in self._clothes])


class Coat(Clothes):
    # Пальто

    def _calculate_fabric(self):
    # посчитать расход ткани На пальто
        self._fabric_required = round(self.size / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
    # Узнать размер пальто
        return self.size

    @V.setter
    def V(self, size: Any):
    # Задать новый размер пальто
        self.size = size

    def __str__(self):
        return f"Для пошива пальто {self.size} размера " \
               f"требуется {self.fabric_required} кв. метров ткани"


class Suit(Clothes):
    # Костюм

    def _calculate_fabric(self):
    # посчитать расход ткани для костюма
        self._fabric_required = round(2 * self.size * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
    # Узнать размер костюма
        return self.size

    @H.setter
    def H(self, height: Any):
    # Задать новый размер костюма
        self.size = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.size} см. " \
               f"требуется {self.fabric_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('Пальто ультрасовременное', 10)
    print(coat)
    coat.V = 12
    print(coat)

    suit = Suit('Костюм изысканный', 164)
    print(suit)
    suit.H = 192
    print(suit)

    print(coat.total_fabric_required)
    print(suit.total_fabric_required)

