from itertools import combinations

inp = '''A -2.5 .5 3.5 .5
B -2.23 99.99 -2.10 -56.23
C -1.23 99.99 -1.10 -56.23
D 100.1 1000.34 2000.23 2100.23
E 1.5 -1 1.5 1.0
F 2.0 2.0 3.0 2.0
G 2.5 .5 2.5 2.0'''


def intersect(a, b):
    try:
        u = ((b[3] - b[1]) * (a[0] - b[0]) - (b[2] - b[0]) * (a[1] - b[1]))/((b[2] - b[1]) * (a[3] - a[1]) - (b[3] - b[1]) * (a[2] - a[0]))
        try:
            t = ((u - 1) * a[0] - u * a[2] + b[0])/(b[0] - b[2])
        except ZeroDivisionError:
            t = ((u - 1) * a[1] - u * a[3] + b[1])/(b[1] - b[3])
        if 0 <= u <= 1 and 0 <= t <= 1:
            return u, t
        else:
            return None
    except ZeroDivisionError:
        return None

intersects = set()
line_segments = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
pairs = []
lines = {j[0]: list(map(float, j[1:])) for j in [i.split(' ') for i in inp.split('\n')]}
for combination in combinations(lines, 2):
    if intersect(lines[combination[0]], lines[combination[1]]):
        intersects.add(combination[0])
        intersects.add(combination[1])
        pairs.append([combination[0], combination[1]])
no_intersects = line_segments - intersects
print('Intersecting Lines:')
for pair in pairs:
    print(str(pair[0]) + ' ' + str(pair[1]))
print('No intersections:')
for no_intersect in no_intersects:
    print(str(no_intersect))