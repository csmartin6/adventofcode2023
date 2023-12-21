from collections import defaultdict


def project_beam(contraption, state):
    visited = set()
    visited.add((0,0))
    particles = [
        state  # position i, position j, velocity i, velocity j
    ]
    times_seen = defaultdict(int)
    steps = 0
    while len(particles) > 0:
        steps += 1
        rem_particles = []
        for p in particles:
            p_i, p_j = (p[0] + p[2], p[1] + p[3])
            v_i, v_j = p[2], p[3]
            times_seen[(p_i, p_j, v_i, v_j)] += 1
            if 0 <= p_i < m and 0 <= p_j < n and times_seen[(p_i, p_j, v_i, v_j)] < 2:
                visited.add((p_i, p_j))
                el = contraption[(p_i, p_j)]
                if el == "\\":
                    new_particle_state = (p_i, p_j, v_j, v_i)
                    rem_particles.append(new_particle_state)
                elif el == "/":
                    new_particle_state = (p_i, p_j, -v_j, -v_i)
                    rem_particles.append(new_particle_state)
                elif el == "|":
                    if v_i == 0 and v_j != 0:
                        # down
                        new_particle_state = (p_i, p_j, 1, 0)
                        rem_particles.append(new_particle_state)
                        # up
                        new_particle_state = (p_i, p_j, -1, 0)
                        rem_particles.append(new_particle_state)
                    else:
                        new_particle_state = (p_i, p_j, v_i, v_j)
                        rem_particles.append(new_particle_state)
                elif el == "-":
                    if v_i != 0 and v_j == 0:
                        # left
                        new_particle_state = (p_i, p_j, 0, -1)
                        rem_particles.append(new_particle_state)
                        # right
                        new_particle_state = (p_i, p_j, 0, 1)
                        rem_particles.append(new_particle_state)
                    else:
                        new_particle_state = (p_i, p_j, v_i, v_j)
                        rem_particles.append(new_particle_state)
                else:
                    new_particle_state = (p_i, p_j, v_i, v_j)
                    rem_particles.append(new_particle_state)
        particles = rem_particles

    return visited


if __name__ == '__main__':
    with open('data/day_16/input') as f:
    # with open('data/day_16/example') as f:
        lines = f.readlines()

    contraption = {}
    for i, line in enumerate(lines):
        for j, el in enumerate(line.strip("\n")):
            contraption[(i,j)] = el

    m = len(lines)
    n = len(lines[0].strip("\n"))

    visited = set()
    visited.add((0,0))

    visited = project_beam(contraption, (0, -1, 0, 1) )

    print(f"Part 1: {len(visited)}")

    # from top
    print("Part 2")

    most_visited = 0
    most_visited_starting_state= None

    for i in range(n):
        # top
        starting_state = (-1, i, 1, 0)
        visited = project_beam(contraption, starting_state)
        num_visited = len(visited)
        if num_visited > most_visited:
            most_visited = num_visited
            most_visited_starting_state = starting_state

        # bottom
        starting_state = (m, i, -1, 0)
        visited = project_beam(contraption, starting_state)
        num_visited = len(visited)
        if num_visited > most_visited:
            most_visited = num_visited
            most_visited_starting_state = starting_state

    for j in range(m):
        # left
        starting_state = (j, -1, 0, 1)
        visited = project_beam(contraption, starting_state)
        num_visited = len(visited)
        if num_visited > most_visited:
            most_visited = num_visited
            most_visited_starting_state = starting_state

        # right
        starting_state = (j, n, 0, -1)
        visited = project_beam(contraption, starting_state)
        num_visited = len(visited)
        if num_visited > most_visited:
            most_visited = num_visited
            most_visited_starting_state = starting_state


    print(f"Most Visited: {most_visited}")





