times = []
distances = []
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        if "Time:" in line:
            times.extend(line.split()[1:])
        elif "Distance:" in line:
            distances.extend(line.split()[1:])

times = [int(i) for i in times]
distances = [int(i) for i in distances]

winning_counts = []
for idx in range(0, len(times)):
    time = times[idx]
    max_distance = distances[idx]
    winning_count = 0
    for i in range(0, time + 1):
        speed = i
        travel_time = time - i
        distance = speed * travel_time
        if distance > max_distance:
            winning_count += 1
    winning_counts.append(winning_count)

result = 1
for count in winning_counts:
    result = result * count
print(result)
