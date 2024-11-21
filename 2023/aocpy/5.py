import os
import re

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day5.txt")) as f:
        almanac = [l for line in f.readlines() if (l := line.strip()) != ""]

    # Part #1
    locations = [int(s) for s in re.findall(r"(\d+)", almanac[0])]
    map_idxs = [i for i, line in enumerate(almanac) if "map" in line]
    num_maps = len(map_idxs)
    for i in range(num_maps):
        map_idx = map_idxs[i]
        next_map_idx = map_idxs[i+1] if (i + 1) < num_maps else len(almanac)
        map_lines = almanac[(map_idx+1):next_map_idx]
        already_checked = []
        for map_line in map_lines:
            d, s, r = map(
                int, re.search(r"(\d+) (\d+) (\d+)", map_line).groups()
            )
            for j in range(len(locations)):
                if j in already_checked:
                    continue
                elif locations[j] in range(s, s+r):
                    locations[j] = locations[j] - s + d
                    already_checked.append(j)
    print(f"Answer #1: {min(locations)}")
    assert min(locations) == 199602917

    # Part #2
    print("Answer #2: STUMPED")
