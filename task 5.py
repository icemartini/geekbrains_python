# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

with open("task 5.txt", 'w+') as f:
    user_input = input('Введите через пробел набор чисел: ')
    f.write(user_input)
    f.seek(0)
    print(f"Сумма чисел в файле: {reduce(lambda a, b: int(a) + int(b), f.read().split())}")
