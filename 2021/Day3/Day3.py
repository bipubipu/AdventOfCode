import sys


def binary_list2int(binary_list):
    return int(''.join(binary_list), 2)


with open(sys.argv[1], 'r') as infile:
    lines = infile.readlines()
    length_lines = len(lines)
    length_number = len(lines[0].strip())
    gamma_binary = []
    epsilon_binary = []
    for i in range(length_number):
        total = 0
        for j in range(length_lines):
            total += int(lines[j][i])
        if length_lines / 2 > total:
            gamma_binary.append('0')
            epsilon_binary.append('1')
        else:
            gamma_binary.append('1')
            epsilon_binary.append('0')

    gamma = binary_list2int(gamma_binary)
    epsilon = binary_list2int(epsilon_binary)
    print(gamma * epsilon)
