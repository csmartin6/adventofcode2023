from cachetools import cached, Cache
from cachetools.keys import hashkey
import networkx as nx
import sys
sys.setrecursionlimit(100000)

MAX_STRAIGHT_MOVES = 3


def blockskey(*args, blocks={}, **kwargs):
    key = hashkey(*args, **kwargs)
    key += tuple(sorted(blocks.items()))
    return key

@cached(
    cache=Cache(maxsize=1000000),
    key=blockskey
)
def crucible_step(m, n, state, target,visited, blocks={}, straight_moves=0):
    # move
    position = (state[0]+state[2], state[1]+state[3])
    if position == target:
        return blocks[position]

    if not (0 <= position[0] < m and 0 <= position[1] < n) or position in visited:
        return float("Inf")

    cost = blocks[position]
    new_visit = set(visited)
    new_visit.add(position)
    visited = frozenset(new_visit)

    # turn_left
    left_v = -state[3], state[2]
    left_state = (*position, *left_v)
    if_go_left = crucible_step(m, n, left_state, target, visited, blocks=blocks, straight_moves=0)

    # turn right
    right_v = state[3], -state[2]
    right_state = (*position, *right_v)
    if_go_right = crucible_step(m,n, right_state, target, visited, blocks=blocks, straight_moves=0)

    if_go_straight = float("Inf")
    if straight_moves < MAX_STRAIGHT_MOVES:
        straight_state = (position[0], position[1], state[2], state[3])
        if_go_straight = crucible_step(m, n, straight_state, visited, target, blocks=blocks, straight_moves=straight_moves+1)

    return cost + min(if_go_left, if_go_right, if_go_straight)








if __name__ == '__main__':
    with open('data/day_17/input') as f:
    # with open('data/day_17/example') as f:
        lines = f.readlines()

    m = len(lines)
    n = len(lines[0].strip())
    blocks = {}

    G = nx.DiGraph()

    for i, line in enumerate(lines):
        for j, cost in enumerate(line.strip()):
            blocks[(i,j)] = int(cost)
            G.add_node((i, j, 'vertical'))
            G.add_node((i, j, 'horizontal'))



    for i in range(m):
        for j in range(n):
            # add edges left
            for k in range(j-1, max(j-MAX_STRAIGHT_MOVES-1, -1), -1):

                source = (i, j, 'vertical')
                destination = (i, k, 'horizontal')
                weight = sum([
                               blocks[(i, z)] for z in range(k, j)
                           ])
                G.add_edge(source,
                           destination,
                           weight=weight)

            # add edges up
            for k in range(i-1, max(i-MAX_STRAIGHT_MOVES-1, -1), -1):
                source = (i, j, 'horizontal')
                destination = (k, j, 'vertical')
                weight = sum([
                    blocks[(z, j)] for z in range(k, i)
                ])
                G.add_edge(source,
                           destination,
                           weight=weight)
            # add edges down
            for k in range(i+1, min(i+MAX_STRAIGHT_MOVES + 1, m)):
                source = (i, j, 'horizontal')
                destination = (k, j, 'vertical')
                weight = sum([
                               blocks[(z, j)] for z in range(i+1, k+1)
                           ])
                G.add_edge(source,
                           destination,
                           weight=weight)

            # add edges right
            for k in range(j+1, min(j+MAX_STRAIGHT_MOVES+1, n)):
                source = (i, j, 'vertical')
                destination = (i, k, 'horizontal')
                weight = sum([
                    blocks[(i, z)] for z in range(j+1, k+1)
                ])
                G.add_edge(source,
                           destination,
                           weight=weight)

    G.add_node('start')
    G.add_node('finish')
    G.add_edge('start', (0,0,'vertical'), weight=0)
    G.add_edge('start', (0, 0, 'horizontal'), weight=0)
    G.add_edge((m-1,n-1,'horizontal'),'finish', weight=0)
    G.add_edge((m - 1, n - 1, 'vertical'), 'finish', weight=0)
    shortest_path = nx.shortest_path(G, 'start', 'finish', weight='weight')

    shortest_path_length = nx.path_weight(G, shortest_path, weight='weight')
    print(f"Part 1: ")
    print(f"path length {len(shortest_path)}")
    print(f"path weight: {shortest_path_length}")


    MIN_STRAIGHT = 4
    MAX_STRAIGHT = 10

    G = nx.DiGraph()

    for i, line in enumerate(lines):
        for j, cost in enumerate(line.strip()):
            blocks[(i, j)] = int(cost)
            G.add_node((i, j, 'vertical'))
            G.add_node((i, j, 'horizontal'))

    for i in range(m):
        for j in range(n):
            # add edges left
            for k in range(j - MIN_STRAIGHT, max(j - MAX_STRAIGHT - 1, -1), -1):
                if k >= 0:
                    source = (i, j, 'vertical')
                    destination = (i, k, 'horizontal')
                    weight = sum([
                        blocks[(i, z)] for z in range(k, j)
                    ])
                    G.add_edge(source,
                               destination,
                               weight=weight)

            # add edges up
            for k in range(i- MIN_STRAIGHT, max(i - MAX_STRAIGHT - 1, -1), -1):
                if k >= 0:
                    source = (i, j, 'horizontal')
                    destination = (k, j, 'vertical')
                    weight = sum([
                        blocks[(z, j)] for z in range(k, i)
                    ])
                    G.add_edge(source,
                               destination,
                               weight=weight)
            # add edges down
            for k in range(i + MIN_STRAIGHT, min(i + MAX_STRAIGHT + 1, m)):
                if k < m:
                    source = (i, j, 'horizontal')
                    destination = (k, j, 'vertical')
                    weight = sum([
                        blocks[(z, j)] for z in range(i + 1, k + 1)
                    ])
                    G.add_edge(source,
                               destination,
                               weight=weight)

            # add edges right
            for k in range(j + MIN_STRAIGHT, min(j + MAX_STRAIGHT + 1, n)):
                if k < n:
                    source = (i, j, 'vertical')
                    destination = (i, k, 'horizontal')
                    weight = sum([
                        blocks[(i, z)] for z in range(j + 1, k + 1)
                    ])
                    G.add_edge(source,
                               destination,
                               weight=weight)

    G.add_node('start')
    G.add_node('finish')
    G.add_edge('start', (0, 0, 'vertical'), weight=0)
    G.add_edge('start', (0, 0, 'horizontal'), weight=0)
    G.add_edge((m - 1, n - 1, 'horizontal'), 'finish', weight=0)
    G.add_edge((m - 1, n - 1, 'vertical'), 'finish', weight=0)
    shortest_path = nx.shortest_path(G, 'start', 'finish', weight='weight')

    shortest_path_length = nx.path_weight(G, shortest_path, weight='weight')
    print(f"Part 2: ")
    print(f"path length {len(shortest_path)}")
    print(f"path weight: {shortest_path_length}")