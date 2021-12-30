with open('Day1.csv', 'r') as infile:
    count = 0
    lines = infile.readlines()
    length = len(lines)

    for i in range(length):
        if i < length - 3:
            first_sum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
            second_sum = int(lines[i + 1]) + int(lines[i + 2]) + int(
                lines[i + 3])
            if second_sum > first_sum:
                count += 1
        else:
            break
    print(count)