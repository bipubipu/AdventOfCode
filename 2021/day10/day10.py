import sys

chunk_pair = {'(': ')', '{': '}', '[': ']', '<': '>'}
chunk_open = ['(', '{', '[', '<']
chunk_close = [')', '}', ']', '>']
error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}


# Iterate every character, if the current one is in open list, and the next one in close list
# Remove them if they are a pair
# But if they don't match, that means this line is corrupted
def find_incorrect_closing_character(line):
    line_copy = line
    i = 0
    while i < len(line_copy) - 1:
        if line_copy[i] in chunk_open and line_copy[i + 1] in chunk_close:
            if chunk_pair[line_copy[i]] == line_copy[i + 1]:
                line_copy = line_copy[:i] + line_copy[i + 2:]
                # Reset the index, move it back to previous character
                i = i - 1 if i > 1 else 0
                continue
            else:
                return line_copy[i + 1]
        i += 1
    return None


with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

total_score = 0
for line in lines:
    result = find_incorrect_closing_character(line)
    if result:
        total_score += error_score[result]

print(total_score)