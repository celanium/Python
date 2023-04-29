'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру,
например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
 вводимых пользователем данных. Например, для указания количества принтеров,
 отправленных на склад, нельзя использовать строковый тип данных.
 Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
 максимум возможностей, изученных на уроках по ООП.'''

BLACK = "black"
WHITE = "white"
LASER = "laser"
SCANNER = "scanner"
COPIER = "copier"
PRINTER = "printer"


class Warehouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = {}

    def receive(self, item: "OfficeEquipment", quantity_str: str):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} не оргтехника")
        if not quantity_str.isdigit():
            raise AddStorageError(f"{quantity_str} не число")
        quantity = int(quantity_str)
        if not item.model:
            raise AddStorageError(f"Пустое наименование модели")
        else:
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity

    def transfer(self, item: "OfficeEquipment", quantity, department):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            print(
                f"{quantity} единиц {item.model} переведено в {department}")
        else:
            raise TransferStorageError(
                f"Недостаточно {item.model} на складе {self.inventory[item]}")

    def __str__(self):
        res = f"{self.name} {self.address} \n"
        for equipment, amount in self.inventory.items():
            res += f"{equipment.model} : {amount} \n"
        return res


class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Ошибка передачи оборудования:\n {text}"


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
        self.canPrint = True if self.type in (PRINTER, COPIER) else False
        self.canScan = True if self.type in (SCANNER, COPIER) else False

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
        super().__init__(PRINTER,
                         vendor,
                         model,
                         color,
                         price)
        self.cartridge_type = cartridge_type

    def __str__(self):
        return f"{super().__str__()} {self.cartridge_type}"


class Scanner(OfficeEquipment):
    canPrint = False
    canScan = True
    dpi = None

    def __init__(self, vendor: str,
                 model: str,
                 color: str,
                 price: float,
                 dpi: int):
        super().__init__(SCANNER, vendor,
                         model,
                         color,
                         price)
        self.dpi = dpi

    def __str__(self):
        return f"{super().__str__()} {self.dpi}"


class Copier(OfficeEquipment):
    canPrint = True
    canScan = True
    speed = None

    def __init__(self, vendor: str,
                 model: str,
                 color: str,
                 price: float,
                 speed):
        super().__init__(COPIER, vendor,
                         model,
                         color,
                         price)
        self.speed = speed

    def __str__(self):
        return f"{super().__str__()} {self.speed}"


if __name__ == '__main__':
    warehouse = Warehouse("Главный", "Медиков, 3")
    printer1 = Printer("Canon", "MF-3010", BLACK, 1000, LASER)
    printer2 = Printer("HP", "M111w", WHITE, 4000, LASER)
    scanner = Scanner("Epson", "DS-30000", WHITE, 2499.00, 600)
    copier1 = Copier("Xerox", "DF-2311", BLACK, 1333.44, 33)
    print(printer1)
    warehouse.receive(printer1, "2")
    warehouse.receive(printer2, "1")
    warehouse.receive(scanner, "2")
    warehouse.receive(copier1, "2")
    print(warehouse)
    try:
        warehouse.transfer(printer1, 5, "Бухгалтерия")
    except TransferStorageError:
        print("не получилось передать")
    warehouse.transfer(printer1, 1, "Бухгалтерия")
    print(warehouse)
