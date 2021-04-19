# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("task 2.txt", 'r') as f:
    lines = f.read().splitlines()
    for line_index, line in enumerate(lines):
        lines_count = line_index + 1
        words_count = len(line.split())
        print(f'количество слов в {lines_count} строке: {words_count}')
    print(f'количество строк в файле: {lines_count}')
