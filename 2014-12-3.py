import random
from itertools import product


def map_gen(N):
    tiles = ['A'] * 6 + ['G'] + ['.'] * 12
    tilemap = [[random.choice(tiles) for i in range(N)] for j in range(N)]
    return tilemap


def expand_map(tilemap):
    expanded_map = tilemap
    for i, j in product(range(len(tilemap)), range(len(tilemap))):
        if tilemap[i][j] == '.':
            for k, l in product(range(-1, 2), range(-1, 2)):
                try:
                    if tilemap[i + k][j + l] == 'G' and (k, l) != (0, 0):
                        expanded_map[i][j] = 'X'
                except IndexError:
                    pass
    return expanded_map


map = map_gen(20)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in map]))
print('\n')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in expand_map(map)]))