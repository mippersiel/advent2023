import re


with open("puzzle-input.txt") as file:
    seeds = []
    maps = {}
    section = ""
    for file_line in file:
        line = file_line.strip()
        if not line:
            continue

        if ":" in line:
            section = line.split()[0].replace("-to-", "_")
            if section == "seeds:":
                seeds = [int(i) for i in line.split()[1:]]
            else:
                maps[section] = []
            continue

        maps[section].append([int(i) for i in line.split()])

lowest = None
for seed in seeds:
    entry = "seed"
    entry_val = seed
    finised = False
    while not finised:
        finised = True
        key = ""
        for k in maps:
            if re.match("^" + entry, k):
                key = k
                finised = False
                break
        if not finised:
            for mapping in maps[key]:
                src_start = mapping[1]
                src_end = src_start + mapping[2]
                if entry_val >= src_start and entry_val < src_end:
                    entry_val = mapping[0] + (entry_val - src_start)
                    break
            entry = key.split("_")[1]

    if lowest is None:
        lowest = entry_val
    else:
        if entry_val < lowest:
            lowest = entry_val

print(str(lowest))
