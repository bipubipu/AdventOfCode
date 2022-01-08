import sys


def binary_list2int(binary_list):
    return int(''.join(binary_list), 2)


with open(sys.argv[1], 'r') as infile:
    lines = infile.readlines()
    length_number = len(lines[0].strip())
    lines_copy1 = lines.copy()
    lines_copy2 = lines.copy()

    for i in range(length_number):
        total = 0
        for j in range(len(lines_copy1)):
            total += int(lines_copy1[j][i])
        # 1 is the most common digit or 0 & 1 are equally common, keep 1
        if total >= len(lines_copy1) / 2:
            lines_copy1 = [x for x in lines_copy1 if x[i] == '1']
        else:
            lines_copy1 = [x for x in lines_copy1 if x[i] == '0']
        if len(lines_copy1) == 1:
            break
    for i in range(length_number):
        total = 0
        for j in range(len(lines_copy2)):
            total += int(lines_copy2[j][i])
        # 0 is the least common digit or 0 & 1 are equally common, keep 0
        if total >= len(lines_copy2) / 2:
            lines_copy2 = [x for x in lines_copy2 if x[i] == '0']
        else:
            lines_copy2 = [x for x in lines_copy2 if x[i] == '1']
        if len(lines_copy2) == 1:
            break

    oxygen = binary_list2int(lines_copy1)
    co2 = binary_list2int(lines_copy2)

    print(oxygen * co2)