# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

with open("task 3.txt", 'r') as f:
    employees = f.read().splitlines()
    salaries = [int(e.split()[1]) for e in employees]
    poor = [e.split()[0] for e in employees if int(e.split()[1]) < 20000]
    print(f"Сотрудники с окладом менее 20 тыс.: {' '.join(poor)}")
    print(f"Средняя величина дохода: {mean(salaries)}")
