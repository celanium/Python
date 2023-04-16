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