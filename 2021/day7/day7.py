import sys, math

with open(sys.argv[1], 'r') as f:
    list = f.read().split(',')

list = [int(i) for i in list]
list.sort()

# The minimal fuel consumption is near the mean and median value of crabs' positions
mean = sum(list) / len(list)
mid = len(list) // 2
median = (list[mid] + list[~mid]) / 2
range_min = min(math.floor(mean), math.floor(median))
range_max = max(math.ceil(mean), math.ceil(median))

fuel = []
for i in range(range_min, range_max + 1):
    fuel.append(sum(abs(j - i) for j in list))
print(min(fuel))