import sys

chunk_pair = {'(': ')', '{': '}', '[': ']', '<': '>'}
chunk_open = ['(', '{', '[', '<']
chunk_close = [')', '}', ']', '>']
completion_score = {')': 1, ']': 2, '}': 3, '>': 4}


# Iterate every character, if the current one is in open list, and the next one in close list
# Remove them if they are a pair
# But if they don't match, that means this line is corrupted
# Finally return the line if it's incomplete and None if it's corrupted
def find_incomplete_line(line):
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
                return None
        i += 1
    return line_copy


def get_matching_string(incomplete_string):
    matched_string = ''
    for char in incomplete_string:
        matched_string = chunk_pair[char] + matched_string
    return matched_string


def get_completion_score(string):
    score = 0
    for char in string:
        score = 5* score + completion_score[char]
    return score


with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()
scores = []
for line in lines:
    result = find_incomplete_line(line)
    if result:
        scores.append(get_completion_score(get_matching_string(result)))
scores.sort()
mid_index = int((len(scores)-1)/2)
print(scores[mid_index])