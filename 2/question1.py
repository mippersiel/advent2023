import re

constraint = {"red": 12, "green": 13, "blue": 14}

sum = 0
with open("puzzle-input.txt") as file:
    for line in file:
        split = line.split(":")
        game_entry = split[0].strip()
        game_id = int(re.findall("[0-9]+", game_entry)[0])
        draws = split[1].strip().split("; ")
        game_ok = True
        for draw in draws:
            entries = draw.split(", ")
            for entry in entries:
                data = entry.split(" ")
                count = int(data[0])
                color = data[1]
                if count > constraint[color]:
                    game_ok = False
                    break
            if not game_ok:
                break
        if game_ok:
            sum += game_id

print(sum)
