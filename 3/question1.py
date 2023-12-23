import re


def process_number(line, prev, next, start, end):
    max_idx = len(line) - 1
    number = int(line[start:end])
    start_idx = 0 if start - 1 < 0 else start - 1
    end_idx = max_idx if end > max_idx else end
    partial_lines = []
    partial_lines.append(line[start_idx] + line[end_idx])
    if prev is not None:
        partial_lines.append(prev[start_idx : end_idx + 1])
    if next is not None:
        partial_lines.append(next[start_idx : end_idx + 1])
    for partial_line in partial_lines:
        if re.findall(r"[^\.0-9]", partial_line):
            return number
    return 0


def process_line(line, prev, next):
    sum = 0
    line_length = len(line)
    start_idx = -1
    for i in range(0, line_length):
        if re.match(r"[0-9]", line[i]):
            if start_idx == -1:
                start_idx = i
            else:
                continue
        else:
            if start_idx == -1:
                continue
            else:
                sum += process_number(line, prev, next, start_idx, i)
                start_idx = -1
    if start_idx != -1:
        sum += process_number(line, prev, next, start_idx, line_length)
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
