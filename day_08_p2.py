from itertools import cycle
if __name__ == '__main__':
    #
    with open('data/day_08_input.txt') as f:
        lines = f.readlines()
    #
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

    aaas = [k for k in nodes.keys() if k.endswith("A")]
    zzzs = [k for k in nodes.keys() if k.endswith("Z")]

    starting_node = "11A"
    time_to_z = {}
    next_z = {}
    cycle_time = {}

    for starting_node in aaas:
        # get all z nodes
    # step backwards from each z node
        current_node = starting_node
        found_z = False
        found_cycle = False
        for i, direction in enumerate(cycle(directions)):
            if direction == "L":
                current_node = nodes[current_node][0]
            elif direction == "R":
                current_node = nodes[current_node][1]

            if current_node.endswith("Z"):
                if starting_node not in time_to_z:
                    time_to_z[starting_node] = []
                time_to_z[starting_node] += [i+1]
                if starting_node not in next_z:
                    next_z[starting_node] = []
                next_z[starting_node] += [current_node]
                if starting_node in time_to_z and len(time_to_z[starting_node]) > 5:
                    break

        print(f"{starting_node}: Time to a Z = {time_to_z[starting_node]} next z: {next_z[starting_node]}" )


    cycle_times = []
    for node in aaas:
        remainder = time_to_z[node][0]
        cycle_time = time_to_z[node][1] - time_to_z[node][0]
        cycle_time2 = time_to_z[node][2] - time_to_z[node][1]
        print("remainder: ", remainder, "cycle_time: ", cycle_time, "cycle_time2: ", cycle_time2)
        cycle_times += [cycle_time]

    from math import lcm
    steps = lcm(*cycle_times)
    print(f"steps: {steps}")




