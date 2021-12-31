def getPoints(x1, y1, x2, y2, dict):
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                countPoints(x1, i, dict)
        else:
            for i in range(y2, y1 + 1):
                countPoints(x1, i, dict)
    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                countPoints(i, y1, dict)
        else:
            for i in range(x2, x1 + 1):
                countPoints(i, y1, dict)


def countPoints(x, y, dict):
    if (x, y) in dict:
        dict[(x, y)] += 1
    else:
        dict[(x, y)] = 1


with open('vents.csv', 'r') as infile:
    lines = [line.strip().split('->') for line in infile.readlines()]
    # Innitialise a dictionary to store coords
    coords = {}

    # Line will be in this form: ['0,9 ', ' 5,9']
    for line in lines:
        # Set coords of starting and ending point of the line
        (x1, y1) = tuple(map(int, line[0].split(',')))
        (x2, y2) = tuple(map(int, line[1].split(',')))

        # If a line is vertical or horizontal
        if x1 == x2 or y1 == y2:
            getPoints(x1, y1, x2, y2, coords)

    print(sum(v >= 2 for v in coords.values()))