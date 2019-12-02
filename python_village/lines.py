file = open('lines.txt')

even_lines = [line for i, line in enumerate(file) if i % 2 == 1]
for line in even_lines:
    print(line.rstrip())
