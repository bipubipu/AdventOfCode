import sys

with open(sys.argv[1], 'r') as f:
    list = f.read().split(',')
    list = list(map(int, list))

num_of_days = int(sys.argv[2])
for i in range(num_of_days):
    for j in range(len(list)):
        if list[j] == 0:
            list[j] = 6
            list.append(8)
        else:
            list[j] -= 1

print(len(list))
