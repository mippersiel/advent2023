times = []
distances = []
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        if "Time:" in line:
            times.extend(line.split()[1:])
        elif "Distance:" in line:
            distances.extend(line.split()[1:])

time = int("".join(times))
max_distance = int("".join(distances))

loosing_count = 0
for i in range(0, time):
    speed = i
    travel_time = time - i
    distance = speed * travel_time
    if distance > max_distance:
        break
    else:
        loosing_count += 1
for i in range(time, 0, -1):
    speed = i
    travel_time = time - i
    distance = speed * travel_time
    if distance > max_distance:
        break
    else:
        loosing_count += 1
print(time + 1 - loosing_count)
