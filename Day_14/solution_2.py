input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

# cycles = 1000000000
cycles = 300

sums = {"north": set(), "east": set(), "south": set(), "west": set()}
shifted_rocks = []
flipped_lines = [[*r][::-1] for r in zip(*all_lines)]


def rotate_once():
    return [[*r][::-1] for r in zip(*shifted_rocks)]


def shift_boulders(input_list):
    global shifted_rocks
    changes = True
    while changes:
        changes = False
        helper = []
        for line in input_list:
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
    return shifted_rocks


def sum_it_up() -> int:
    sum = 0
    for rock_column in shifted_rocks:
        for i, rock in enumerate(rock_column):
            if rock == "O":
                sum = sum + (i + 1)
    return sum


# Initial North:
shift_boulders(flipped_lines)
sums["north"].add(sum_it_up())

# All other cycles:
for i in range(cycles):
    # East
    flipped_lines = rotate_once()
    shift_boulders(flipped_lines)
    sums["east"].add(sum_it_up())
    # South
    flipped_lines = rotate_once()
    shift_boulders(flipped_lines)
    sums["south"].add(sum_it_up())
    # West
    flipped_lines = rotate_once()
    shift_boulders(flipped_lines)
    sums["west"].add(sum_it_up())
    # North
    flipped_lines = rotate_once()
    sums["north"].add(sum_it_up())
    shift_boulders(flipped_lines)

for direction in sums.values():
    print(direction)
    print(str(min(direction)))