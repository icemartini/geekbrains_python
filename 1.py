# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, rate, bonus = argv

def salary(hours, rate, bonus):
    # (выработка в часах * ставка в час) + премия
    salary = int(hours) * int(rate) + int(bonus)
    print(salary)
    return

salary(hours, rate, bonus)
