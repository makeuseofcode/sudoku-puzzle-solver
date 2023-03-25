board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    # Check row
    for col in range(9):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Check column
    for row in range(9):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # Check 3x3 box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for row in range(box_row*3, box_row*3 + 3):
        for col in range(box_col*3, box_col*3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - - ")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")



print_board(board)
solve(board)
print("Solved:")
print_board(board)