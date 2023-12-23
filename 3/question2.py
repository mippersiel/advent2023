import re


def get_number(line, idx):
    number = None
    length = len(line)
    start = idx
    end = idx
    if re.match(r"[0-9]", line[idx]):
        prev = idx - 1
        while prev >= 0:
            if re.match(r"[0-9]", line[prev]):
                start = prev
                prev = prev - 1
            else:
                break
        next = idx + 1
        while next < length:
            if re.match(r"[0-9]", line[next]):
                end = next
                next = next + 1
            else:
                break
        number = int(line[start : end + 1])
    return number


def process_gear(line, prev, next, idx):
    numbers = []
    if idx > 0:
        if prev is not None:
            numbers.append(get_number(prev, idx - 1))
        numbers.append(get_number(line, idx - 1))
        if next is not None:
            numbers.append(get_number(next, idx - 1))
    if idx != len(line) - 1:
        if prev is not None:
            numbers.append(get_number(prev, idx + 1))
        numbers.append(get_number(line, idx + 1))
        if next is not None:
            numbers.append(get_number(next, idx + 1))
    if prev is not None:
        numbers.append(get_number(prev, idx))
    if next is not None:
        numbers.append(get_number(next, idx))
    uniques = list(set(numbers))
    if None in uniques:
        uniques.remove(None)
    if len(uniques) == 2:
        return uniques[0] * uniques[1]
    else:
        return 0


def process_line(line, prev, next):
    sum = 0
    for i in range(0, len(line)):
        if line[i] == "*":
            sum += process_gear(line, prev, next, i)
    return sum


with open("puzzle-input.txt") as file:
    sum = 0
    last = None
    previous = None
    current = None
    for line in file:
        last = previous
        previous = current
        current = line.strip()
        if previous is None:
            continue
        sum += process_line(previous, last, current)
    sum += process_line(current, previous, None)

    print(sum)
