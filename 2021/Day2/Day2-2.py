import sys


def get_number(string):
    return int(''.join(filter(str.isdigit, string)))


with open(sys.argv[1], 'r') as infile:
    horizon = 0
    depth = 0
    aim = 0
    for line in infile:
        if line.startswith("forward"):
            horizon += get_number(line)
            depth += get_number(line) * aim
        if line.startswith("down"):
            aim += get_number(line)
        if line.startswith("up"):
            aim -= get_number(line)
    print(horizon * depth)