import re


with open("puzzle-input.txt") as file:
    seeds = []
    unsorted = {}
    section = ""
    for file_line in file:
        line = file_line.strip()
        if not line:
            continue

        if ":" in line:
            section = line.split()[0].replace("-to-", "_")
            if section == "seeds:":
                seed_ranges = [int(i) for i in line.split()[1:]]
                for x in range(0, len(seed_ranges), 2):
                    seeds.append(
                        [seed_ranges[x], seed_ranges[x] + seed_ranges[x + 1] - 1]
                    )
            else:
                unsorted[section] = {}
            continue
        line_split = [int(i) for i in line.split()]
        unsorted[section][line_split[1]] = line_split

# Sort the mapping by source value
maps = {}
for section in unsorted:
    maps[section] = []
    sorted_dict = dict(sorted(unsorted[section].items()))
    for key in sorted_dict:
        maps[section].append(sorted_dict[key])

lowest = None
name = "seed"
entry_vals = seeds
finised = False
while not finised:
    finised = True
    key = ""
    for k in maps:
        if re.match("^" + name, k):
            key = k
            finised = False
            break
    if not finised:
        new_vals = []
        for entry in entry_vals:
            entry_first = entry[0]
            entry_last = entry[1]
            is_outside_range = False
            for mapping in maps[key]:
                is_outside_range = False
                src_start = mapping[1]
                src_end = src_start + mapping[2]
                dst_start = mapping[0]
                dst_end = mapping[0] + mapping[2]

                # Starts in or after range
                if entry_first >= src_start:
                    # Starts in range
                    if entry_first < src_end:
                        entry_offset = entry_first - src_start

                        # Completely in range
                        if entry_last < src_end:
                            entry_range = entry_last - entry_first
                            new_vals.append(
                                [
                                    dst_start + entry_offset,
                                    dst_start + entry_offset + entry_range,
                                ]
                            )
                            break

                        # Finishes after range
                        else:
                            new_vals.append(
                                [
                                    dst_start + entry_offset,
                                    dst_end - 1,
                                ]
                            )
                            entry_first = src_end

                    # Is after range
                    else:
                        is_outside_range = True
                        continue

                # Start before range
                else:
                    # Finishes in or after
                    if entry_last >= src_start:
                        # Process what is before range
                        new_vals.append([entry_first, src_start - 1])

                        # Process what is in or after range
                        entry_first = src_start

                        # Finishes in range
                        if entry_last < src_end:
                            entry_range = entry_last - entry_first
                            new_vals.append(
                                [
                                    dst_start,
                                    dst_start + entry_range,
                                ]
                            )
                            break

                        # Finishes after range
                        else:
                            new_vals.append(
                                [
                                    dst_start,
                                    dst_end - 1,
                                ]
                            )
                            entry_first = src_end

                    # Is before range
                    else:
                        is_outside_range = True
                        break

                # If here, it's because the entry was cut, re-update the entry array for next iteration
                entry[0] = entry_first

            # In the case where the entry is out of range and no more mappings to process, just re-use it as-is
            if is_outside_range:
                new_vals.append(entry)

        entry_vals = new_vals
        name = key.split("_")[1]

# Find the smallest range start
for values in entry_vals:
    if lowest is None:
        lowest = values[0]
    else:
        if values[0] < lowest:
            lowest = values[0]

print(str(lowest))
