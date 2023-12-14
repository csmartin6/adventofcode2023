from utils import transpose_array, print_array, array_to_string, flip_array_horizontally


def roll_west(array):
    adj_array = []
    for row in array:
        next_idx = 0
        new_row = []
        for i, el in enumerate(row):
            if el == "#":
                next_idx = i + 1
                new_row.append("#")
            elif el == "O":
                new_row.append(".")
                new_row[next_idx] = "O"
                next_idx += 1
            elif el == ".":
                new_row.append(".")

        adj_array.append(new_row)
    return adj_array

def roll_north(array):
    tr_array = transpose_array(array)
    adj_array = roll_west(tr_array)
    return transpose_array(adj_array)

def roll_south(array):
    rev_array = array[::-1]
    rev_tr = transpose_array(rev_array)
    adj_array = roll_west(rev_tr)
    adj_array_tr = transpose_array(adj_array)
    return adj_array_tr[::-1]

def roll_east(array):
    flipped_array = flip_array_horizontally(array)
    rolled_array = roll_west(flipped_array)
    return flip_array_horizontally(rolled_array)

def score_array(array):
    score = 0
    for i, row in enumerate(reversed(array)):
        for el in row:
            if el == "O":
                score += (i+1)
    return score


if __name__ == '__main__':
    with open('data/day_14/input') as f:
    # with open('data/day_14/example') as f:
        lines = f.readlines()


    array = lines

    # adj_array = roll_north(array)
    # score = score_array(adj_array)
    # print_array(adj_array)
    # print(f"Part 1: {score}")

    found_configurations = {}
    cycles_found = {}
    init_array_atr = array_to_string(array)
    curr_array = array
    # found_configurations[array_to_string(array)] = 0
    scores = {}
    scores[0] = score_array(array)
    cycle_length = 0
    i = 0
    N = 1000000000
    while i < N-1:
        # print(f"{i}", end="\r")
        curr_array = roll_north(curr_array)
        # print("\nRoll North")
        # print_array(curr_array)
        curr_array = roll_west(curr_array)
        # print("\nRoll West")
        # print_array(curr_array)
        curr_array = roll_south(curr_array)
        # print("\nRoll South")
        # print_array(curr_array)
        curr_array = roll_east(curr_array)
        # print("\nRoll East")
        # print_array(curr_array)

        # print(f"\nAfter {i+1} cycles")
        # print_array(curr_array)
        scores[i] = score_array(curr_array)
        array_str = array_to_string(curr_array)

        if array_str in cycles_found:
            # move forward number of cycles
            cycle_length = cycles_found[array_str]
            num_cycles = (N-1-i) // cycle_length
            i += num_cycles*cycle_length if num_cycles > 0 else 1
        elif array_str in found_configurations:
            cycles_found[array_str] = i - found_configurations[array_str]
            i += 1
        else:
            found_configurations[array_str] = i
            i += 1


    score = score_array(curr_array)
    print(f"Part 2: {score}")
    # N = 1000000000
    #
    # score = scores[(N-1) % (cycle_length)]


    # print(f"Part 2: {score}")

