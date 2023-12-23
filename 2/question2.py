import re

sum = 0
with open("puzzle-input.txt") as file:
    for line in file:
        split = line.split(":")
        game_entry = split[0].strip()
        game_id = int(re.findall("[0-9]+", game_entry)[0])
        draws = split[1].strip().split("; ")
        colors = {"red": 0, "green": 0, "blue": 0}
        for draw in draws:
            entries = draw.split(", ")
            for entry in entries:
                data = entry.split(" ")
                count = int(data[0])
                color = data[1]
                if colors[color] < count:
                    colors[color] = count
        sum += colors["red"] * colors["blue"] * colors["green"]

print(sum)
