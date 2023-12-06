import re
from collections import defaultdict
def parse_numbers(line):
    matches = re.finditer(r"\.*(\d+)\.*", line)
    return [(m.span(1), int(m.group(1))) for m in matches]

def parse_symbols(line):
    matches = re.finditer(r"([^\d\.\n])", line)
    return [m.start() for m in matches]

def find_gears(line):
    return [i for i, c in enumerate(line) if c == "*"]


if __name__ == '__main__':
    with open('data/day_3_input.txt') as f:
        lines = f.readlines()
    # with open('data/day_3_part_2_example.txt') as f:
    #     lines = f.readlines()
    symbol_positions = []
    number_positions = []
    gears = {}
    for i, line in enumerate(lines):
        symbols = parse_symbols(line)
        for j in symbols:
            symbol_positions += [(i,j)]

        gears_on_line = find_gears(line)
        for j in symbols:
            gears[(i,j)] = []

    sum_part_numbers = 0
    positions_covered_by_symbols = set()

    for (i,j) in symbol_positions:
        positions_covered_by_symbols.add((i-1, j-1))
        positions_covered_by_symbols.add((i, j - 1))
        positions_covered_by_symbols.add((i + 1, j - 1))
        positions_covered_by_symbols.add((i - 1, j))
        positions_covered_by_symbols.add((i, j))
        positions_covered_by_symbols.add((i + 1, j))
        positions_covered_by_symbols.add((i - 1, j+1))
        positions_covered_by_symbols.add((i, j+1))
        positions_covered_by_symbols.add((i + 1, j+1))

    for i, line in enumerate(lines):
        numbers = parse_numbers(line)
        for ((s,e), v) in numbers:
            number_positions += [((s,e),v)]
            for j in range(s,e):
                if (i, j) in positions_covered_by_symbols:
                    sum_part_numbers += v
                    break

            for j in range(s-1,e+1):
                for k in [-1, 0 , 1]:
                    if (i+k, j) in gears:
                        gears[(i+k, j)].append(v)

    sum_gear_ratios = 0
    for k, v in gears.items():
        if len(v) == 2:
            sum_gear_ratios += v[0]*v[1]

    print(f"part 1: sum of part numbers = {sum_part_numbers}")
    print(f"part 1: sum of gear ratios = {sum_gear_ratios}")
