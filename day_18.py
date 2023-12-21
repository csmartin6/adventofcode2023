from queue import Queue
import numpy as np

def dig_trench(lines):
    pos = (0,0)
    trench = set([pos])
    for line in lines:
        direction, distance, color = line.strip().split()
        distance=int(distance)
        di = 0
        if direction == "D":
            di = 1
        elif direction == "U":
            di = -1

        dj = 0
        if direction == "L":
            dj = -1
        elif direction == "R":
            dj = 1

        for i in range(distance):
            pos = pos[0] + di , pos[1] + dj
            trench.add(pos)


    return trench

def get_corners(lines):
    pos = (0.5,0.5)
    trench = [pos]
    total_length = 0
    for i, line in enumerate(lines):
        next_line = lines[i+1] if i < len(lines)-1 else lines[0]
        next_direction, next_distance, _ = next_line.strip().split()
        direction, distance, color = line.strip().split()
        distance = int(distance)
        total_length+=distance
        di = 0
        if direction == "D":
            di = distance # + 1 if next_direction == "R" else 0
        elif direction == "U":
            di = -distance # - 1 if next_direction == "R" else 0

        dj = 0
        if direction == "L":
            dj = -distance # -1 if next_direction == "D" else 0
        elif direction == "R":
            dj = distance # + 1 if next_direction == "D" else 0
        pos = pos[0] + di, pos[1] + dj
        trench.append(pos)

    # shift cornors
    corners = [(0,0)]

    for i in range(1, len(trench)-1):
        previous_edge = (trench[i][0] - trench[i-1][0], trench[i][1] - trench[i-1][1])
        next_edge = (trench[i+1][0] - trench[i][0], trench[i+1][1] - trench[i][1])

        angle = ((np.arctan2(next_edge[0], next_edge[1]) - np.arctan2(previous_edge[0], previous_edge[1]) + np.pi * 2) % (
                    np.pi * 2)) - np.pi
        # if angle > 0:
        #     print(f"{i}: {trench[i]} {previous_edge} => {next_edge} convex")
        # else:
        #     print(f"{i}: {trench[i]} {previous_edge} => {next_edge} concave")




    return trench, total_length



def get_corners2(lines):

    directions = ["R", "D", "L", "U"]

    pos = (0, 0)
    trench = [pos]
    total_length = 0
    for i, line in enumerate(lines):
        _, _, hex = line.strip().split()
        hex = hex.replace("(", "").replace(")", "").replace("#","")
        direction = directions[int(hex[-1])]
        distance = int(hex[:-1], 16)
        total_length+=distance
        di = 0
        if direction == "D":
            di = distance # + 1 if next_direction == "R" else 0
        elif direction == "U":
            di = -distance # - 1 if next_direction == "R" else 0

        dj = 0
        if direction == "L":
            dj = -distance # -1 if next_direction == "D" else 0
        elif direction == "R":
            dj = distance # + 1 if next_direction == "D" else 0
        pos = pos[0] + di, pos[1] + dj
        trench.append(pos)

    return trench, total_length

def fill_trench(trench_boundary):
    i_min = min([p[0] for p in trench_boundary])
    i_max = max([p[0] for p in trench_boundary])
    j_min = min([p[1] for p in trench_boundary])
    j_max = max([p[1] for p in trench_boundary])

    filled = set(trench_boundary)

    for i in range(i_min, i_max + 1):
        for j in range(j_min, j_max+1):
            if (i,j) not in trench_boundary:
                # check left
                crossings_left = 0
                for k in range(j - 1, j_min-1, -1):
                    if (i, k) in trench_boundary:
                        crossings_left += 1

                # check right
                crossings_right = 0
                for k in range(j + 1, j_max+1):
                    if (i, k) in trench_boundary:
                        crossings_right += 1

                # check up
                crossings_up = 0
                for k in range(i - 1, i_min-1, -1):
                    if (k, j) in trench_boundary:
                        crossings_up += 1

                # check down
                crossings_down = 0
                for k in range(i + 1, i_max+1):
                    if (k, j) in trench_boundary:
                        crossings_down += 1

                if all([
                    crossings_left != 0,
                    crossings_right != 0,
                    crossings_up != 0,
                    crossings_down != 0,
                ]):
                    filled.add((i,j))

    return filled

def fill_trench2(trench_boundary):
    filled = set(trench_boundary)
    q = Queue()
    q.put((1,1))

    while not q.empty():
        i, j = q.get()
        for p in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if p not in filled:
                filled.add(p)
                q.put(p)
    return filled


def print_trench(trench):
    i_min = min([p[0] for p in trench])
    i_max = max([p[0] for p in trench])
    j_min = min([p[1] for p in trench])
    j_max = max([p[1] for p in trench])

    for i in range(i_min, i_max+1):
        str = ""
        for j in range(j_min, j_max+1):
            str += "#" if (i,j) in trench else "."

        print(str)

def print_both(boundary, interior):
    i_min = min([p[0] for p in boundary])
    i_max = max([p[0] for p in boundary])
    j_min = min([p[1] for p in boundary])
    j_max = max([p[1] for p in boundary])

    for i in range(i_min, i_max+1):
        str = ""
        for j in range(j_min, j_max+1):
            str_ij = "."
            if (i,j) in interior:
                str_ij = "@"
            if (i,j) in boundary:
                str_ij = "#"
            str += str_ij

        print(str)

def shoelace_area(trench):
    x = np.array([p[0] for p in trench])
    y = np.array([p[1] for p in trench])
    i = np.arange(len(x))
    area = np.sum(x[i - 1] * y[i] - x[i] * y[i - 1]) / 2
    return area

def polygon_area(vertices):
    """
    Return the area of the polygon enclosed by vertices using the shoelace
    algorithm.

    """

    a = np.vstack((vertices, vertices[0]))
    S1 = sum(a[:-1,0] * a[1:,1])
    S2 = sum(a[:-1,1] * a[1:,0])
    return abs(S1-S2)/2







if __name__ == '__main__':
    with open('data/day_18/input') as f:
    # with open('data/day_18/example') as f:
        lines = f.readlines()

    trench = dig_trench(lines)
    # print("\nBoundary:")
    # print_trench(trench)
    filled = fill_trench2(trench)
    # print("\nFilled:")
    # print_trench(filled)
    # print("\nBoth:")
    # print_both(trench, filled)
    print(f"Part 1: {len(filled)}")

    corners, length = get_corners(lines)
    print(f"total_length: {length}")
    area = polygon_area(corners) + length*0.5 +1
    print(f"Shoelace Area: {area}")


    corners, length = get_corners2(lines)
    print(f"total_length: {length}")
    area = polygon_area(corners) + length*0.5 +1
    print(f"Part 2: Shoelace Area: {int(area)}")
