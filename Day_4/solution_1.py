input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0

for line in all_lines:
    line = line.strip().split(":")[1].strip().split(" | ")
    scratch_card = line[0].strip().split()
    solution_card = line[1].strip().split()
    count = len(set(scratch_card).intersection(solution_card))
    if count > 0:
        final_count = pow(2, count - 1)
        sum = sum + final_count

print(str(sum))