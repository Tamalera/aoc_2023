input_file = open('input3.txt', 'r')
all_lines = input_file.readlines()

sum = 0
for line in all_lines:
    l = line.strip().split()
    for num in l:
        sum = sum + int(num)

print(str(sum))