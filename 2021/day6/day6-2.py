# This solution also works in the first challenge
import sys

with open(sys.argv[1], 'r') as f:
    list = f.read().split(',')

# Initiate the dictionary to store occurences of timer intervals
dict = dict.fromkeys(range(9), 0)
for i in list:
    dict[int(i)] += 1

num_of_days = int(sys.argv[2])
for i in range(num_of_days):
    new_fish = dict[0]
    for j in range(8):
        dict[j] = dict[j + 1]
    dict[6] += new_fish
    dict[8] = new_fish

print(sum(dict.values()))