def get_number(string):
    return int(''.join(filter(str.isdigit, string)))


with open('Day2.csv', 'r') as infile:
    horizon = 0
    depth = 0
    for line in infile:
        if line.startswith("forward"):
            horizon += get_number(line)
        if line.startswith("down"):
            depth += get_number(line)
        if line.startswith("up"):
            depth -= get_number(line)
    print(horizon * depth)