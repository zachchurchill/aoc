import itertools
import os
import re
from typing import List, Tuple

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day3.txt")) as f:
        schematic_lines = [line.strip() for line in f.readlines()]
    regex = re.compile(r"[^\.^\d]")
    symbol_mask = [
        [re.search(regex, entry) is not None for entry in schematic_line]
        for schematic_line in schematic_lines
    ]

    def _near_symbol(i: int, j: int, mask=symbol_mask) -> bool:
        value_in_question = schematic_lines[i][j]
        length_of_line = len(mask[i])
        number_of_lines = len(mask)

        if value_in_question not in "0123456789" or value_in_question == '.':
            return False

        is_near = any(
            mask[m][n]
            for m, n in itertools.product([i-1, i, i+1], [j-1, j, j+1])
            if (m >= 0 and m < number_of_lines)
            and (n >= 0 and n < length_of_line)
            and ([m, n] != [i, j])
        )
        return is_near
    near_symbol_indexes = [
        {j for j, entry in enumerate(schematic_line) if _near_symbol(i, j)}
        for i, schematic_line in enumerate(schematic_lines)
    ]

    part_numbers = [
        int(m.group(0))
        for near_indexes, schematic_line in zip(near_symbol_indexes, schematic_lines)
        for m in re.finditer(r"(\d+)", schematic_line)
        if len(near_indexes) > 0
        and len(near_indexes.intersection(range(m.start(0), m.end(0)))) > 0
    ]
    print(f"Answer #1: {sum(part_numbers)}")
    assert sum(part_numbers) == 544664

    # Part #2
    potential_gears = {
        i: list(re.finditer(r"\*", schematic_line))
        for i, schematic_line in enumerate(schematic_lines)
        if re.search(r"\*", schematic_line) is not None
    }
    digits = {
        i: list(re.finditer(r"(\d+)", schematic_line))
        for i, schematic_line in enumerate(schematic_lines)
        if re.search(r"(\d+)", schematic_line) is not None
    }

    gear_ratios = []
    for k, astericks in potential_gears.items():
        for ast in astericks:
            adjacent = []
            r = set(range(ast.start(0) - 1, ast.end(0) + 1))
            possible_digits = [
                *digits.get(k - 1, []),
                *digits.get(k, []),
                *digits.get(k + 1, []),
            ]
            for digit in possible_digits:
                if r.intersection(range(*digit.span())) != set():
                    adjacent.append(int(digit.group()))
            if len(adjacent) == 2:
                gear_ratios.append(adjacent[0] * adjacent[1])

    print(f"Answer #2: {sum(gear_ratios)}")
    assert sum(gear_ratios) == 84495585

    # Part #1, refactor
    potential_part_numbers = {
        i: list(re.finditer(r"(\d+)", schematic_line))
        for i, schematic_line in enumerate(schematic_lines)
        if re.search(r"(\d+)", schematic_line) is not None
    }
    symbols = {
        i: list(re.finditer(r"[^\.^\d]", schematic_line))
        for i, schematic_line in enumerate(schematic_lines)
        if re.search(r"[^\.^\d]", schematic_line) is not None
    }
    part_numbers = []
    for k, digits in potential_part_numbers.items():
        for d in digits:
            adjacent = []
            r = set(range(d.start(0) - 1, d.end(0) + 1))
            possible_symbols = [
                *symbols.get(k - 1, []),
                *symbols.get(k, []),
                *symbols.get(k + 1, []),
            ]
            for symbol in possible_symbols:
                if r.intersection(range(*symbol.span())) != set():
                    adjacent.append(symbol)
            if len(adjacent) > 0:
                part_numbers.append(int(d.group()))
    print(f"Answer #1 (refactor): {sum(part_numbers)}")
    assert sum(part_numbers) == 544664
