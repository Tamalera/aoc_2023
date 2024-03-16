input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0

flipped_lines =  [ [*r][::-1] for r in zip(*all_lines) ]
shifted_rocks = []

changes = True
while changes:
    changes = False
    helper = []
    for line in flipped_lines:
        new_line = line
        for i, l in enumerate(line):
            if i < (len(line) - 1) and l == "O" and line[i + 1] == ".":
                new_line[i] = "."
                new_line[i + 1] = "O"
                line[i] = "."
                line[i + 1] = "O"
                changes = True
        helper.append(new_line)
        shifted_rocks = helper

counter = 0
for rock_column in shifted_rocks:
    for i, rock in enumerate(rock_column):
        if rock == "O":
            counter += 1
            sum = sum + (i + 1)

print(str(counter))
print(str(sum))
