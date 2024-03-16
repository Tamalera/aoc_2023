input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0


def hash_it(l):
    val = 0
    for el in l:
        val = val + ord(el)
        val = val * 17
        val = val % 256
    return val


for line in all_lines:
    line = line.strip().split(",")
    for l in line:
        sum = sum + hash_it(l)

print(str(sum))
