
def find_vertical_reflections(arr):
    m = len(arr)
    if m ==0:
        return []
    n = len(arr[0])
    candidates = list(range(1, n))
    for row in arr:
        rem_candidates = []
        for candidate in candidates:
            still_candidate = True
            for i in range(1, min(n-candidate+1, candidate+1)):
                if row[candidate-i] != row[candidate - 1 + i]:
                    still_candidate = False
                    break

            if still_candidate:
                rem_candidates.append(candidate)

        candidates = rem_candidates
    return candidates

def find_potential_vertical_reflections(arr):
    m = len(arr)
    if m ==0:
        return []
    n = len(arr[0])
    candidates = list(range(1, n))

    one_strike = set()

    for row in arr:
        rem_candidates = []
        for candidate in candidates:
            still_candidate = True
            for i in range(1, min(n-candidate+1, candidate+1)):
                if row[candidate-i] != row[candidate - 1 + i]:
                    if candidate not in one_strike:
                        one_strike.add(candidate)
                    else:
                        still_candidate = False

            if still_candidate:
                rem_candidates.append(candidate)

        candidates = rem_candidates
    return candidates



def transpose_array(array):
    return [r for r in zip(*array)]


if __name__ == '__main__':
    with open('data/day_13/input') as f:
    # with open('data/day_13/example') as f:
        lines = f.readlines()
    arrays = []
    current_array = []
    for line in lines:
        if len(line.strip()) == 0:
            arrays.append(current_array)
            current_array = []
        else:
            current_array.append(line.strip())
    if len(current_array) > 0:
        arrays.append(current_array)

    print(len(arrays))
    score = 0
    for i, array in enumerate(arrays):

        vert_reflections = find_vertical_reflections(array)
        horiz_reflections = []
        if len(vert_reflections) == 0:
            horiz_reflections = find_vertical_reflections(transpose_array(array))

        print(f"i: {i}\tvert: {vert_reflections}\t horiz: {horiz_reflections}")

        for v in vert_reflections:
            score += v

        for h in horiz_reflections:
            score += 100 * h

    print(f"Part 1: score: {score}")

    print("\nPart 2")

    score = 0
    for i, array in enumerate(arrays):
        vert_reflections = find_vertical_reflections(array)
        potential_vert_reflections = find_potential_vertical_reflections(array)
        horiz_reflections = find_vertical_reflections(transpose_array(array))
        potential_horiz_reflections = find_potential_vertical_reflections(transpose_array(array))

        new_vert = [v for v in potential_vert_reflections if v not in vert_reflections]
        new_horiz = [v for v in potential_horiz_reflections if v not in horiz_reflections]

        print(f"i: {i}\tvert: {new_vert}\t horiz: {new_horiz}")

        for v in new_vert:
            score += v

        for h in new_horiz:
            score += 100 * h

    print(f"Part 2: score: {score}")