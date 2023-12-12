
def expand_rows(galaxy, factor=2):
    rows = []
    for row in galaxy:
        rows.append(row)
        if all(r == "." for r in row):
            for j in range(factor-1):
                rows.append(row)
    return rows

def get_rows_to_expand(galaxy):
    rows = []
    for i, row in enumerate(galaxy):
        if all(r == "." for r in row):
            rows.append(i)
    return rows

def get_cols_to_expand(galaxy):
    galaxy_T = transpose_galaxy(galaxy)
    cols = []
    for j, col in enumerate(galaxy_T):
        if all(c == "." for c in col):
            cols.append(j)
    return cols


def transpose_galaxy(galaxy):
    return [r for r in zip(*galaxy)]

def expand_columns(galaxy, factor=2):
    transposed = transpose_galaxy(galaxy)
    expanded = expand_rows(transposed, factor=factor)
    return transpose_galaxy(expanded)

def expand_galaxy(galaxy, factor=2):
    g = expand_rows(galaxy, factor)
    g = expand_columns(g, factor)
    return g


if __name__ == '__main__':

    with open('data/day_11/input.txt') as f:
    # with open('data/day_11/example.txt') as f:
        lines = f.readlines()

    galaxy = [line.strip() for line in lines]

    expanded_galaxy = expand_galaxy(galaxy)

    positions = []
    for i, row in enumerate(expanded_galaxy):
        for j, x in enumerate(row):
            if x == "#":
                positions.append((i, j))

    shortest_paths = []
    for k, position_a in enumerate(positions):
        for position_b in positions[(k+1):]:
            path = abs(position_a[0]-position_b[0]) + abs(position_a[1]-position_b[1])
            shortest_paths.append(path)


    print("Part 1: Sum of shortest paths:", sum(shortest_paths))


    rows_ex = sorted(get_rows_to_expand(galaxy))
    cols_ex = sorted(get_cols_to_expand(galaxy))

    factor = 1000000
    positions = []
    for i, row in enumerate(galaxy):
        for j, x in enumerate(row):
            if x == "#":
                i_ex = i + len([r for r in rows_ex if r <= i]) * (factor - 1)
                j_ex = j + len([c for c in cols_ex if c <= j]) * (factor - 1)
                positions.append((i_ex, j_ex))

    shortest_paths = []
    for k, position_a in enumerate(positions):
        for position_b in positions[(k + 1):]:
            path = abs(position_a[0] - position_b[0]) + abs(position_a[1] - position_b[1])
            shortest_paths.append(path)

    print(f"Part 2: Expansion Factor: {factor} Sum of shortest paths:", sum(shortest_paths))

