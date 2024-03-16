import re

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

sum = 0
all_possible_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2",
                        "3", "4", "5", "6", "7", "8", "9"]
num_words = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}


def translate(digit_name: str) -> str:
    return num_words[digit_name]


for line in all_lines:
    res = re.findall(r"(?=(" + '|'.join(all_possible_numbers) + r"))", line)
    the_digit = translate(res[0]) + translate(res[-1])
    sum = sum + int(the_digit)

print(str(sum))
