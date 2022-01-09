import sys


def get_points(x1, y1, x2, y2, dict):
    if x1 == x2:
        ymin = y1 if y1 < y2 else y2
        ymax = y2 if y1 < y2 else y1
        for i in range(ymin, ymax + 1):
            count_points(x1, i, dict)

    if y1 == y2:
        xmin = x1 if x1 < x2 else x2
        xmax = x2 if x1 < x2 else x1
        for i in range(xmin, xmax + 1):
            count_points(i, y1, dict)


def count_points(x, y, dict):
    if (x, y) in dict:
        dict[(x, y)] += 1
    else:
        dict[(x, y)] = 1


with open(sys.argv[1], 'r') as infile:
    lines = [line.strip().split('->') for line in infile.readlines()]
# Initialise a dictionary to store coords
coords = {}

# Line will be in this form: ['0,9 ', ' 5,9']
for line in lines:
    # Set coords of starting and ending point of the line
    (x1, y1) = tuple(map(int, line[0].split(',')))
    (x2, y2) = tuple(map(int, line[1].split(',')))

    # If a line is vertical or horizontal
    if x1 == x2 or y1 == y2:
        get_points(x1, y1, x2, y2, coords)

print(sum(v >= 2 for v in coords.values()))
