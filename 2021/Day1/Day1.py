import sys

with open(sys.argv[1], 'r') as infile:
    count = 0
    lines = infile.readlines()
    length = len(lines)

    for i in range(length):
        if i < length - 1:
            if int(lines[i + 1]) > int(lines[i]):
                count += 1
        else:
            break
    print(count)