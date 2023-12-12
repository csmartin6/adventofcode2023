
def next_number(numbers):
    if all(d == 0 for d in numbers):
        return 0
    diffs = [int(numbers[i+1]) - int(numbers[i]) for i in range(len(numbers)-1)]
    final = next_number(diffs)
    last_number = numbers[-1]

    return final + last_number

def previous_number(numbers):
    if all(d == 0 for d in numbers):
        return 0
    diffs = [int(numbers[i+1]) - int(numbers[i]) for i in range(len(numbers)-1)]
    previous = previous_number(diffs)
    first_number = numbers[0]

    return first_number - previous




if __name__ == '__main__':

    with open('data/day_09_input.txt') as f:
        lines = f.readlines()
    #
    # with open('data/day_09_example.txt') as f:
    #     lines = f.readlines()

    next_numbers = []
    previous_numbers = []
    for line in lines:
        numbers = [int(n) for n in line.strip().split()]
        next_numbers.append(next_number(numbers))
        previous_numbers.append(previous_number(numbers))

    print(f"Part 1: sum next numbers: {sum(next_numbers)}")


    print(f"Part 2: sum previous numbers: {sum(previous_numbers)}")