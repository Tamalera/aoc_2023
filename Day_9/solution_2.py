input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0
for line in all_lines:
    line = line.strip().split()
    calc_lines = []
    calc_lines.append(line)
    while set(line) != {0}:
        new_line = []
        for i,l in enumerate(line):
            if i + 1 < len(line):
                new_line.append(int(l) - int(line[i+1]))

        calc_lines.append(new_line)
        line = new_line
    last_elements = []
    calc_lines.reverse()
    for calc_line in calc_lines:
        last_elements.append(calc_line[0])
    for el in last_elements:
        sum = sum + int(el)

print(sum)




