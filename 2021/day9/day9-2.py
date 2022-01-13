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

# Starting from a given point, expand in left, right, up and down four directions if they exist
# Stop if it is 9, otherwise add those points to a list if they are not in it.
def find_basin_points(point, basin_points, data):
    x, y = point
    if point not in basin_points: 
        basin_points.append(point) 
    j = y
    while j > 0:
        j -= 1
        if (x, j) in basin_points:
            break
        elif data[x][j] == '9':
            break
        else:
            basin_points.append((x, j))
    j = y
    while j < len(data[0]) - 1:
        j += 1
        if (x, j) in basin_points:
            break
        elif data[x][j] == '9':
            break
        else:
            basin_points.append((x, j))
    i = x
    while i > 0:
        i -= 1
        if (i, y) in basin_points:
            break
        elif data[i][y] == '9':
            break
        else:
            basin_points.append((i, y))
    i = x
    while i < len(data) - 1:
        i += 1
        if (i, y) in basin_points:
            break
        elif data[i][y] == '9':
            break
        else:
            basin_points.append((i, y))
    return basin_points

def get_all_basin_points(point, initial_points, data):
    basin_points = find_basin_points(point, initial_points, data)
    for p in basin_points:
        new_basin_point = find_basin_points(p,basin_points,data)    
        if set(new_basin_point) == set(basin_points):
            continue
        else:
            basin_points.extend(new_basin_point)
    return basin_points

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

low_points = find_low_points(lines)
size_basins = []

for point in low_points:
    all_basin_points = get_all_basin_points(point, [], lines)
    size_basins.append(len(all_basin_points))
size_basins.sort()

# Print multiplied value of largest three
print(size_basins[-1]*size_basins[-2]*size_basins[-3])