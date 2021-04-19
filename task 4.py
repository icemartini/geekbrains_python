# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("task 4.txt", 'r') as f:
    lines = f.read().splitlines()
    rus = ['Один', 'Два', 'Три', 'Четыре']
    with open("russian.txt", 'w') as russian:
        for index, line in enumerate(lines):
            line = line.split()
            line[0] = rus[index]
            russian.write(' '.join(line) + '\n')
