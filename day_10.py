
if __name__ == '__main__':
    pipe_matrix = {}


    # with open('data/day_10_example_2.txt') as f:
    with open('data/day_10_input.txt') as f:
        lines = f.readlines()
        m = len(lines)
        n = len(lines[0])
        for i, line in enumerate(lines):
            for j, char in enumerate(line.strip("\n")):
                pipe_matrix[(i, j)] = char




    # find S
    start = None
    for k, v in pipe_matrix.items():
        if v == "S":
            start = k
    print(f"start: {start}")
    i_s, j_s = start
    first_steps = []
    for (i,j) in [(i_s-1,j_s), (i_s+1,j_s), (i_s,j_s-1), (i_s,j_s+1)]:
        if (i,j) in pipe_matrix and pipe_matrix[(i,j)] not in [".", "S"]:
            first_steps.append((i,j))



    steps_from_start = {}
    steps_from_start[start] = 0
    for first_direction in first_steps:
        position = first_direction
        velocity = (position[0]-start[0], position[1]-start[1])
        i = 0
        while position != start:
            i+=1
            steps_from_start[position] = i if position not in steps_from_start else min(i, steps_from_start[position])
            if pipe_matrix[position] == "L":
                if velocity == (1, 0):
                    velocity = (0, 1)
                elif velocity == (0, -1):
                    velocity = (-1, 0)
            elif pipe_matrix[position] == "J":
                if velocity == (1, 0):
                    velocity = (0, -1)
                elif velocity == (0, 1):
                    velocity = (-1, 0)
            elif pipe_matrix[position] == "7":
                if velocity == (-1, 0):
                    velocity = (0, -1)
                elif velocity == (0, 1):
                    velocity = (1, 0)
            elif pipe_matrix[position] == "F":
                if velocity == (-1, 0):
                    velocity = (0, 1)
                elif velocity == (0, -1):
                    velocity = (1, 0)

            position = position[0] + velocity[0], position[1] + velocity[1]


    print(f"Part 1: Furthest from start: {max(steps_from_start.values())}")


    points_inside = 0
    inside = {}

    for (i,j), v in pipe_matrix.items():
        if (i,j) not in steps_from_start:
            # go to -1 counting pipe crossings (odd=>inside, even => outside)
            crossings = 0
            for a in range(j, -1, -1):
                if (i, a) in steps_from_start and pipe_matrix[(i, a)] in ["|", "J", "L"]:
                    crossings += 1
            inside[(i,j)] = crossings % 2 == 1


    points_inside = 0
    for k, v in inside.items():
        if v:
            points_inside+=1



    print(f"Part 2: Number of points inside: {points_inside}")



