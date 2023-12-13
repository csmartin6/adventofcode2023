from functools import cache
@cache
def handle_dot(line, groups, curr_damaged=0):
    if curr_damaged == 0:
        return count_of(line[1:], groups, curr_damaged=0)
    else:
        # check group is the right size
        if len(groups) > 0 and curr_damaged == groups[0]:
            return count_of(line[1:], groups[1:], curr_damaged=0)
        else:
            return 0


@cache
def handle_hash(line, groups, curr_damaged=0):
    if len(groups) > 0 and curr_damaged > groups[0]:
        return 0
    return count_of(line[1:], groups, curr_damaged=curr_damaged+1)

@cache
def count_of(line, groups, curr_damaged=0):
    # no more characters
    if len(line) == 0:
        if len(groups) > 1:
            # not all groups made
            return 0
        elif len(groups) == 0:
            # all groups
            return 1 if curr_damaged == 0 else 0
        # return 0
        # last # form a valid group
        return 1 if curr_damaged == groups[0] else 0
    else:
        if line[0] == '?':
            count_dot = handle_dot(line, groups, curr_damaged=curr_damaged)
            count_hash = handle_hash(line, groups, curr_damaged=curr_damaged)
            return count_dot + count_hash
        elif line[0] == "#":
            return handle_hash(line, groups, curr_damaged=curr_damaged)
        else: # (line[0] == ".")
            return handle_dot(line, groups, curr_damaged=curr_damaged)


if __name__ == '__main__':

    with open('data/day_12/input.txt') as f:

    # with open('data/day_12/example.txt') as f:
        lines = f.readlines()


    line1 , group_str = lines[0].strip().split()
    groups1 = [int(n) for n in group_str.split(",")]

    combinations = 0
    # count_of("?", [], curr_damaged=0)
    # count_of('??', [1], curr_damaged=1)
    # c = count_of('###.???', [3,1,1], curr_damaged=0)
    # print(c)

    for line in lines:
        dam_string, group_str = line.strip().split()
        groups = [int(n) for n in group_str.split(",")]
        c = count_of(dam_string, tuple(groups), curr_damaged=0)
        combinations += c
        print(f"{c}: {dam_string}")

    print(f"Part 1: combinations: {combinations }")


    combinations = 0
    for line in lines:
        dam_string, group_str = line.strip().split()
        groups = [int(n) for n in group_str.split(",")]


        unfolded_str = (dam_string + "?") * 5
        unfolded_str = unfolded_str[:-1]
        unfolded_groups = groups * 5
        c = count_of(unfolded_str, tuple(unfolded_groups), curr_damaged=0)
        combinations += c
        print(f"{c}: {dam_string}")

    print(f"Part 2: combinations: {combinations}")