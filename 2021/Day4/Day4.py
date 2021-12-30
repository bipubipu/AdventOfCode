# Check if list/tuple A is contained in list B, return value would be True or False
def compareElements(A, B):
    return all(item in B for item in A)


# Check if a board bingoes row by row. A board is a n*n size array. This method will be called again when board is transposed. If it bingoes, the method returns the final score.
def checkBingo(board, n, num_list):
    for i in range(n):
        if compareElements(board[i], num_list):
            # Flatten the list
            flat_list = [item for sublist in board for item in sublist]
            # Remove marked elements
            unmarked_list = [
                int(item) for item in flat_list if not item in num_list
            ]
            return [unmarked_list, int(num_list[-1])]
    return False


with open('nums.csv', 'r') as f:
    nums = f.read().split(',')

with open('boards.csv', 'r') as infile:
    lines = [line.split() for line in infile.readlines() if line.strip()]
    # Get the size of bingo boards, which is the starting point of iteration
    size = len(lines[0])
    # Get the number of bingo boards.
    num_boards = int(len(lines) / size)

    # Create bingo boards.
    boards = []
    for i in range(num_boards):
        boards.append(lines[i * size:i * size + size])

    # Iterate the list of drawn numbers and check if each board bingoes. Start from the size of bingo boards, increment one each time.
    for i in range(size, len(nums) + 1):
        num_list = nums[:i]
        for board in boards:
            status = checkBingo(board, size, num_list)
        if status:
            print(board)
            print(status)
            break
        else:
            # Check columns by using transposed board.
            tboard = list(zip(*board))
            status = checkBingo(tboard, size, num_list)
            if status:
                print(tboard)
                print(status)
                break
            
