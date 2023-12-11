from itertools import cycle
if __name__ == '__main__':
    #
    with open('data/day_08_input.txt') as f:
        lines = f.readlines()

    # with open('data/day_08_example_3.txt') as f:
    #     lines = f.readlines()


    directions = []
    for line in lines:
        if line == "\n":
            break
        else:
            directions.extend(line.strip("\n"))


    nodes = {}
    for line in lines[2:]:
        node_id = line[0:3]
        left = line[7:10]
        right = line[12:15]
        nodes[node_id] = (left, right)


    # current_node = "AAA"
    # steps = 0
    #
    # for direction in cycle(directions):
    #     if direction == "L":
    #         current_node = nodes[current_node][0]
    #     elif direction == "R":
    #         current_node = nodes[current_node][1]
    #
    #     steps += 1
    #
    #     if current_node == "ZZZ":
    #         break

    # print(f"Part 1: {steps} steps")

    starting_nodes = list(n for n in nodes.keys() if n.endswith("A"))

    current_nodes = {s:s for s in starting_nodes}
    steps = 0
    for direction in cycle(directions):
        print(f"steps: {steps}", end = "\r")
        for k, v in current_nodes.items():
            if direction == "L":
                current_nodes[k] = nodes[v][0]
            elif direction == "R":
                current_nodes[k] = nodes[v][1]

        steps += 1

        if all([v.endswith("Z") for v in current_nodes.values()]):
            break

    print(f"Part 2: {steps} steps")

