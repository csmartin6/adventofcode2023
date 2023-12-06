import re
def parse_game(line):

    game_details, games_raw = line.split(':')
    game_id = None

    if matches := re.match(r"Game (\d*)", game_details):
        game_id = int(matches.groups()[0])


    games = games_raw.split(";")

    max_red = 0
    max_green = 0
    max_blue = 0

    for game in games:
        # parse
        if matches := re.search(r"(\d*) blue", game):
            blue = int(matches.groups()[0])
            max_blue = max(max_blue, blue)

        if matches := re.search(r"(\d*) red", game):
            red = int(matches.groups()[0])
            max_red = max(max_red, red)


        if matches := re.search(r"(\d*) green", game):
            green = int(matches.groups()[0])
            max_green = max(max_green, green)

    return game_id, (max_red, max_green, max_blue)

if __name__ == '__main__':
    with open('data/day_2_input.txt') as f:
        lines = f.readlines()

    num_red = 12
    num_green = 13
    num_blue = 14

    sum_ids = 0
    sum_of_powers = 0
    for line in lines:
        game_id, (r, g, b) = parse_game(line)
        if r <= num_red and g <= num_green and b <= num_blue:
            sum_ids += game_id

        game_power = r*g*b
        sum_of_powers += game_power

    print(f"part_1: sum_ids: {sum_ids}")
    print(f"part_2: sum_of_powers: {sum_of_powers}")


