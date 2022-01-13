import sys


def check_low_point_vertical(x, y, data):

    # If the point is on the first line
    if x == 0:
        return True if data[x][y] < data[x + 1][y] else False

    # If the point is on the last line
    elif x == len(data) - 1:
        return True if data[x][y] < data[x - 1][y] else False

    return True if data[x][y] < data[x + 1][y] and data[x][y] < data[
        x - 1][y] else False


def check_low_point_horizontal(y, list):
    if y == 0:
        return True if list[y] < list[y + 1] else False
    elif y == len(list) - 1:
        return True if list[y] < list[y - 1] else False
    return True if list[y] < list[y + 1] and list[y] < list[y - 1] else False


def find_low_points(data):
    low_points = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            if check_low_point_vertical(
                    x, y, data) and check_low_point_horizontal(y, data[x]):
                low_points.append((x, y))
    return low_points


with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

low_points = find_low_points(lines)
print(sum(low_points) + len(low_points))