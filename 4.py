# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    __storage = {'printer': [], 'scanner': [], 'xerox': []}

    def __init__(self, size, freespace, paid=True):
        self.size = size
        self.freespace = freespace
        self.paid = paid

    def __str__(self):
        return f"на складе {len(Warehouse.__storage['printer'])} принтеров, {len(Warehouse.__storage['scanner'])} " \
               f"сканеров и {len(Warehouse.__storage['xerox'])} копиров"

    @staticmethod
    def get_warehouse():
        return Warehouse.__storage

class OfficeEquipment:
    def __init__(self, model, paper, dimension):
        self.name = 'equipment'
        self.model = model
        self.paper = paper
        self.dimension = dimension

    def to_warehouse(self, Warehouse):
        if Warehouse.paid:
            Warehouse.get_warehouse()[self.name].append(self.model)
            print(f'{self.name} успешно перемещен из офиса на склад')
        else:
            print('склад не оплачен, выберите другой склад')

    def to_office(self):
        try:
            Warehouse.get_warehouse()[self.name].remove(self.model)
            print(f'{self.name} успешно перемещен со склада в офис')
        except ValueError:
            print('такой техники нет на складе')

    def is_in_warehouse(self):
        return self.model in Warehouse.get_warehouse()[self.name]

class Printer(OfficeEquipment):
    def __init__(self, model, paper, dimension, colors, speed):
        super().__init__(model, paper, dimension)
        self.name = 'printer'
        self.speed = speed
        try:
            self.colors = int(colors)
        except ValueError:
            print('Количество цветов должно быть целым числом')
            self.colors = None

class Scanner(OfficeEquipment):
    def __init__(self, model, paper, dimension, type, sensor, greycolors):
        super().__init__(model, paper, dimension)
        self.name = 'scanner'
        self.type = type
        self.sensor = sensor
        try:
            self.greycolors = int(greycolors)
        except ValueError:
            print('Количество цветов должно быть целым числом')
            self.greycolors = None

class Xerox(OfficeEquipment):
    def __init__(self, model, paper, dimension, speed):
        super().__init__(model, paper, dimension)
        self.name = 'xerox'
        self.speed = speed

canon = Printer('canon 5d', 'A4', '4800x600', 'sdf', '8p/min')
hp = Scanner('hp laserjet', 'A4', '4800x600', 'tablet', 'CIS', 256)
xerox = Xerox('xerox workcentre', 'A4', '600x600', '20p/min')
warehouse1 = Warehouse('10x10', '5')
warehouse2 = Warehouse('20x20', '10', False)

print(canon.model, canon.colors)
print(hp.type, hp.sensor, hp.greycolors)
print(xerox.dimension)
print(Warehouse.get_warehouse())
canon.to_warehouse(warehouse1)
print(canon.is_in_warehouse())
print(warehouse1)
hp.to_warehouse(warehouse2)
xerox.to_office()
canon.to_office()
