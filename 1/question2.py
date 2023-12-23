import re

number_strings = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def get_numbers_in_line(line):
    number_array = {}
    for number, number_string in number_strings.items():
        indexes = [m.start() for m in re.finditer(number_string, line)]
        for idx in indexes:
            number_array[idx] = number
    indexes = [m.start() for m in re.finditer("[0-9]", line)]
    for idx in indexes:
        number_array[idx] = line[idx]
    return dict(sorted(number_array.items()))


sum = 0
with open("puzzle-input.txt") as file:
    for line in file:
        numbers = get_numbers_in_line(line)
        keys = list(numbers.keys())
        number = int(numbers[keys[0]] + numbers[keys[-1]])
        sum += number

print(sum)
