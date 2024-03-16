input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0
for line in all_lines:
    the_digit = ""
    for char in line:
        if char.isdigit():
            the_digit = char
            break
    for c in line[::-1]:
        if c.isdigit():
            the_digit = the_digit + c
            break
    sum = sum + int(the_digit)

print(str(sum))
