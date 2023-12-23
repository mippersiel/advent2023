import re

sum = 0
with open("puzzle-input.txt") as file:
    for line in file:
        matches = re.findall("[0-9]", line)
        number = int(matches[0] + matches[-1])
        sum += number

print(sum)
