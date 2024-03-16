input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0
card_tracker = dict()

for i, line in enumerate(all_lines):
    card_tracker[i] = 1

for i, line in enumerate(all_lines):
    line = line.strip().split(":")[1].strip().split(" | ")
    scratch_card = line[0].strip().split()
    solution_card = line[1].strip().split()
    count = len(set(scratch_card).intersection(solution_card))

    for c in range(1, count + 1):
        card_tracker[i + c] = card_tracker[i + c] + 1
        for copy in range(1, card_tracker[i]):
            card_tracker[i + c] = card_tracker[i + c] + 1

for el in card_tracker:
    sum = sum + card_tracker[el]

print(str(sum))
