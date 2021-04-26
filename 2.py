# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt

first = input("Введите числитель: ")
second = input("Введите знаменатель: ")

try:
    if float(second) == 0:
        raise ZeroException("На ноль делить нельзя")
except ZeroException as err:
    print(err)
else:
    print(f"Результат деления: {float(first) / float(second)}")
