# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return abs(self.count - other.count) if self.count != other.count else 'Разность равна нулю'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return round(self.count / other.count)

    def make_order(self, cellsinrow):
        rows_count = self.count // cellsinrow
        rest = self.count % cellsinrow
        return ('*' * cellsinrow + '\n') * rows_count + '*' * rest

cell1 = Cell(21)
cell2 = Cell(4)
cell3 = Cell(21)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 - cell3)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(4))
