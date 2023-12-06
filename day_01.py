digit_strings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_first_digit(line):
    return next(int(d) for d in line if d.isdigit())

def get_first_number(line):
    # get first digit
    try:
        first_idx, first_digit = next((i, int(d)) for i, d in enumerate(line) if d.isdigit())
    except StopIteration:
        first_idx = len(line)
        first_digit = None

    for k,v in digit_strings.items():
        idx = line.find(k)
        if idx != -1 and idx <= first_idx:
            first_digit = v
            first_idx = idx
    return first_digit




def get_last_digit(line):
    return get_first_digit(reversed(line))

def get_last_number(line):
    # get last digit
    try:
        last_idx, last_digit = next((i, int(d)) for i, d in enumerate(reversed(line)) if d.isdigit())
        last_idx = len(line) - last_idx - 1
    except StopIteration:
        last_idx = 0

    for k, v in digit_strings.items():
        idx = line.rfind(k)
        if idx != -1 and idx >= last_idx:
            last_digit = v
            last_idx = idx
    return last_digit

def part_1(lines):
    calibration_sum = 0
    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        calibration_sum += first_digit * 10 + last_digit

    return calibration_sum

def part_2(lines):
    calibration_sum = 0
    for line in lines:
        first_digit = get_first_number(line)
        last_digit = get_last_number(line)

        calibration_sum += first_digit * 10 + last_digit

    return calibration_sum

if __name__ == '__main__':

    with open('data/day_1_input.txt') as f:
        lines = f.readlines()
        
    part_1_calibration_sum = part_1(lines)
    print("Part 1")
    print(f"Calibration values sum: {part_1_calibration_sum}")

    part_2_calibration_sum = part_2(lines)
    print("Part 2")
    print(f"Calibration values sum: {part_2_calibration_sum}")

