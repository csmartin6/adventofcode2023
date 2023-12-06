def play_game(line):
    card, rest = line.split(":")
    game_numbers_str, my_numbers_str = rest.split("|")

    game_numbers = set(int(i.strip()) for i in game_numbers_str.split())
    my_numbers = [int(i.strip()) for i in my_numbers_str.split()]

    count = 0
    for m in my_numbers:
        if m in game_numbers:
            count += 1

    score = 2 ** (count - 1) if count > 0 else 0
    return score


def get_count_winning_numbers(line):
    card, rest = line.split(":")
    game_numbers_str, my_numbers_str = rest.split("|")

    game_numbers = set(int(i.strip()) for i in game_numbers_str.split())
    my_numbers = [int(i.strip()) for i in my_numbers_str.split()]

    count = 0
    for m in my_numbers:
        if m in game_numbers:
            count += 1

    return count


if __name__ == '__main__':

    with open('data/day_4_input.txt') as f:
        lines = f.readlines()
    # with open('data/day_04_part_1_example.txt') as f:
    #     lines = f.readlines()

    score = sum([play_game(line) for line in lines])
    print(f"part 1: score: {score}")
    cards = {}
    for i in range(len(lines)):
        cards[i] = 1

    for i, line in enumerate(lines):
        num_cards = cards[i]
        count = get_count_winning_numbers(line)
        for j in range(count):
            if i + j + 1 < len(lines):
                cards[i + j + 1] += num_cards

    print(f"part 2: # cards: {sum(cards.values())}")
