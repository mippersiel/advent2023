def extrapolate(array):
    next_array = []
    all_zeros = True
    for i in range(1, len(array)):
        new_entry = array[i] - array[i - 1]
        all_zeros &= new_entry == 0
        next_array.append(new_entry)
    if all_zeros:
        return array[-1]
    else:
        last_val = extrapolate(next_array)
        return last_val + array[-1]


entries = []
with open("puzzle-input.txt") as file:
    for line in file:
        entries.append([int(i) for i in line.strip().split()])

sum = 0
for entry in entries:
    sum += extrapolate(entry)
print(sum)
