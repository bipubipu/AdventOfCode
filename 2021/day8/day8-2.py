import sys

# Count the occurences of each letter appears in a given signal pattern.
def count_letters(pattern_string):
    letter_counts = {}
    for letter in 'abcdefg':
        letter_counts[letter] = pattern_string.count(letter)
    return letter_counts

# From 10 unique digital patterns to induct what letters correspond to 'abcdefg' 
def get_new_mapping(entry):
    signal_patterns = entry.split('|')[0]
    signal_patterns_list = signal_patterns.split()
    entry_letter_count = count_letters(signal_patterns)
    new_mapping = {}

    # We find that only 'b', 'e', 'f' appear unique times, 6, 4, 9 repectively.
    # In new pattens, we can induct which letters represent 'b' 'e' 'f' based on letter occurences.
    new_mapping['b'] = list(entry_letter_count.keys())[list(
        entry_letter_count.values()).index(original_letter_count['b'])]
    new_mapping['e'] = list(entry_letter_count.keys())[list(
        entry_letter_count.values()).index(original_letter_count['e'])]
    new_mapping['f'] = list(entry_letter_count.keys())[list(
        entry_letter_count.values()).index(original_letter_count['f'])]

    # Because 1 uses 2 segments 'cf', and 1 is the only number that uses 2 segments, we know what is 'c'
    # Digit 7 uses 3 segments 'acf', we can know how 'a' is represented by
    # Number 4 uses 4 segments 'bcdf', as we already know 'bcf', so we can know which is 'd'
    for signal in signal_patterns_list:
        if len(signal) == 2:
            digit_two_signal = signal
        if len(signal) == 3:
            digit_seven_signal = signal
        if len(signal) == 4:
            digit_four_signal = signal

    new_mapping['c'] = digit_two_signal.replace(new_mapping['f'], '')
    new_mapping['a'] = digit_seven_signal.replace(new_mapping['f'],'').replace(new_mapping['c'], '')
    new_mapping['d'] = digit_four_signal.replace(new_mapping['b'], '').replace(
        new_mapping['c'], '').replace(new_mapping['f'], '')

    # 'g' is the last letter unmatched
    new_mapping['g'] = ''.join(
        set('abcdefg') - set(list(new_mapping.values())))
    return new_mapping

def get_number(mapping, raw_output):
    # Switch key and value, easier to convert output
    converted_mapping = { y:x for x,y in mapping.items()}
    converted_output = ''
    for letter in raw_output:
        converted_output += converted_mapping[letter]

    result = ''.join(sorted(converted_output))
    number = list(segment_mapping.keys())[list(
        segment_mapping.values()).index(result)]
    return number

def convert_output(entry):
    mapping = get_new_mapping(entry)
    raw_outputs = entry.split('|')[1].split()
    final_output = ''
    for output in raw_outputs:
        if len(output) == 2:
            final_output += '1'
        elif len(output) == 4:
            final_output += '4'
        elif len(output) == 3:
            final_output += '7'
        elif len(output) == 7:
            final_output += '8'
        else:
            final_output += str(get_number(mapping, output))
    return int(final_output)

with open(sys.argv[1], 'r') as f:
    entries = f.readlines()

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

# original_letter_count should be {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}
original_letter_count = count_letters(''.join(list(segment_mapping.values())))

output_values = sum(convert_output(entry) for entry in entries)

print(output_values)