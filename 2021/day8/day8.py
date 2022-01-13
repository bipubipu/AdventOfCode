import sys

with open(sys.argv[1], 'r') as f:
    entries = f.readlines()

# Get four digit output values
outputs = [entry.split('|')[1].split() for entry in entries]

# Mapping for number of segments needed for digits
segment_mapping = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
count_digits = 0
for output in outputs:
    for digit in output:
        if len(digit) in {
                len(segment_mapping[1]),
                len(segment_mapping[4]),
                len(segment_mapping[7]),
                len(segment_mapping[8])
        }:
            count_digits += 1

print(count_digits)