import functools
import math


def win(time, distance, hold_time):
    return hold_time * (time - hold_time) > distance


def winning_range(time, distance):
    a = -1
    b = time
    c = -distance

    zero_1 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    zero_2 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    lower_zero, upper_zero = sorted([zero_1, zero_2])
    return math.ceil(lower_zero), math.floor(upper_zero)


if __name__ == '__main__':

    with open('data/day_06_input.txt') as f:
        lines = f.readlines()

    # with open('data/day_06_example.txt') as f:
    #     lines = f.readlines()

    times = [int(x) for x in lines[0].strip("Time:").split()]
    distances = [int(x) for x in lines[1].strip("Distance:").split()]

    ways_to_win = []
    for time, distance in zip(times, distances):
        wins = 0
        for h in range(time):
            if win(time, distance, h):
                wins += 1
        ways_to_win.append(wins)

    prod = functools.reduce(lambda x, y: x * y, ways_to_win, 1)

    print(f"Part 1: Product of ways to win {prod}")

    ways_to_win2 = []
    for time, distance in zip(times, distances):
        lb, ub = winning_range(time, distance)
        ways_to_win2.append(ub - lb + 1)
    prod2 = functools.reduce(lambda x, y: x * y, ways_to_win2, 1)
    print(f"Part 1: Product of ways to win alt {prod2}")

    time = int(lines[0].strip("Time:").replace(" ", ""))
    distance = int(lines[1].strip("Distance:").replace(" ", ""))

    lb, ub = winning_range(time, distance)
    print(f"Part 2: Winning range {lb}, {ub}: ways to win {ub - lb + 1}")
