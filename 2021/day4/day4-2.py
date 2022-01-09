import sys


# Check if list/tuple A is contained in list B, return True or False
def compare_lists(A, B):
    return all(item in B for item in A)


def calculate_score(board, drawn_nums):
    # Flatten the list
    flat_list = [item for sublist in board for item in sublist]
    # Remove marked elements
    unmarked_list = [int(item) for item in flat_list if not item in drawn_nums]
    return sum(unmarked_list) * int(drawn_nums[-1])


# Check if a board is bingo row by row and then transpose it and check again if there's no bingo.
# A board is a n*n size array.
# If it bingoes, the method returns the final score. Otherwise, return False.
def check_board_is_bingo(board, size, drawn_nums):
    for i in range(size):
        if compare_lists(board[i], drawn_nums):
            return calculate_score(board, drawn_nums)

    transposed_board = list(zip(*board))
    for i in range(size):
        if compare_lists(transposed_board[i], drawn_nums):
            return calculate_score(transposed_board, drawn_nums)
    return False


with open(sys.argv[1], 'r') as f:
    nums = f.read().split(',')

with open(sys.argv[2], 'r') as infile:
    lines = [line.split() for line in infile.readlines() if line.strip()]

# Get the size of bingo boards, which is the starting point of iteration
size = len(lines[0])
# Get the number of bingo boards.
num_boards = len(lines) // size

# Create bingo boards.
boards = []
for i in range(num_boards):
    boards.append(lines[i * size:i * size + size])

# Iterate the list of drawn numbers and check if each board bingoes.
# Start from the size of bingo boards, increment one each time.
scores = []
for i in range(size, len(nums) + 1):
    drawn_nums = nums[:i]
    for board in boards:
        status = check_board_is_bingo(board, size, drawn_nums)
        if status:
            # Remove the board if it bingoes, store scores in a list, the last one is what we are after
            boards.remove(board)
            scores.append(status)
print(scores[-1])
