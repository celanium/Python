'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

import enum


class Warehouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def __str__(self):
        return f"{self.name} {self.address} {','.join([str(i) for i in self.inventory])}"


class OfficeEquipment:
    def __init__(
            self,
            device_type: str,
            vendor: str,
            model: str,
            color: str,
            price: float,
    ):
        self.type = device_type
        self.vendor = vendor
        self.model = model
        self.color = color
        self.purchase_price = price
        self.canPrint = True if self.type in ("printer", "copier") else False
        self.canScan = True if self.type in ("scanner", "copier") else False

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    canPrint = True
    canScan = False
    cartridge_type = ""

    def __init__(self,
                 vendor: str,
                 model: str,
                 color: str,
                 price: float,
                 cartridge_type: str):
        super().__init__('printer',
                         vendor,
                         model,
                         color,
                         price)
        self.cartridge_type = cartridge_type

    def __str__(self):
        return f"{super().__str__()} {self.cartridge_type})"


class Scanner(OfficeEquipment):
    canPrint = False
    canScan = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Copier(OfficeEquipment):
    canPrint = True
    canScan = True

    def __init__(self, *args):
        super().__init__('copier', *args)


if __name__ == '__main__':
    warehouse = Warehouse("Главный", "Медиков, 3")
    printer1 = Printer("Canon", "MF-3010", "black", 1000, "laser")
    printer2 = Printer("HP", "M111w", "white", 4000, "laser")
    print(printer1)
    warehouse.add_item(printer1)
    warehouse.add_item(printer2)
    print(warehouse)
