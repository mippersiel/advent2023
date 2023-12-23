def extrapolate(array):
    next_array = []
    all_zeros = True
    for i in range(1, len(array)):
        new_entry = array[i] - array[i - 1]
        all_zeros &= new_entry == 0
        next_array.append(new_entry)
    if all_zeros:
        return array[0]
    else:
        first_val = extrapolate(next_array)
        return array[0] - first_val


entries = []
with open("puzzle-input.txt") as file:
    for line in file:
        entries.append([int(i) for i in line.strip().split()])

sum = 0
for entry in entries:
    sum += extrapolate(entry)
print(sum)
