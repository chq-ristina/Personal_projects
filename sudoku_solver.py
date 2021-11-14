"""
Christina Phillips

A sudoku solver that uses backtracking to solve the given sudoku puzzle
"""

"""
Solves the sudoku board
"""
def solve(board):
    #finds an empty space in the board
    empty = find_empty(board)

    #board is solved
    if not empty:
        return True
    #board is not solved
    else:
        r, c = empty

    #Goes through all the possible solution numbers
    for x in range(1, 10):
        #x is not already in the board
        if not contains(board, x, r, c):
            board[r][c] = x  #add x to board

            #check if the board has been solved
            if solve(board):
                return True

            #board hasn't been solved so return that value back to 0 and try again with a new number
            board[r][c] = 0
    return False

"""
Returns the list of numbers in the given row
"""
def row(board, idx):
    for y in range(len(board)):
        if y == idx:
            return board[y]

"""
Returns the list of numbers in the given column
"""
def col(board, idx):
    lst_c = []  #will hold the list of numbers in column
    for y in range(len(board)):
        for x in range(len(board)):
            if x == idx:
                lst_c.append(board[y][x])   #adds number to list
    return lst_c

"""
Returns a list of the numbers in the box that the number is in
"""
def box(board, i, j):
    lst_box = [] #holds the list of numbers in the box

    #The range of the box
    if i >= 0 and 2 >= i:
        lst_i = [0, 1, 2]
    elif i >= 3 and 5 >= i:
        lst_i = [3, 4, 5]
    else:
        lst_i = [6, 7, 8]

    #The range of the box
    if j >= 0 and 2 >= j:
        lst_j = [0, 1, 2]
    elif j >= 3 and 5 >= j:
        lst_j = [3, 4, 5]
    else:
        lst_j = [6, 7, 8]

    #goes through the ranges made for the i and j value and
    #appends the values at board[i][j] to the lst_box
    for y in lst_i:
        for x in lst_j:
            lst_box.append(board[y][x])

    return lst_box

"""
Will get the list of the row, column, and box the number is in
If the given value is in the either three lists, return true, if not return false
"""
def contains(board, val, r, c):
    lst_r = row(board, r)
    for x in lst_r:
        if x == val:
            return True

    lst_c = col(board, c)
    for x in lst_c:
        if x == val:
            return True

    lst_b = box(board, r, c)
    for x in lst_b:
        if x == val:
            return True

    return False

"""
Finds where the empty values are inside the board
"""
def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 0:
                return (y, x)
    return None

"""
Sudoku board
Any place that has a 0 needs to be solved
"""
def get_board():
    board = [
        [0, 0, 0, 4, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 1, 8],
        [5, 0, 6, 9, 0, 0, 0, 3, 0],
        [0, 6, 9, 0, 0, 0, 3, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 2, 1],
        [8, 0, 0, 1, 5, 7, 6, 0, 9],
        [0, 0, 0, 0, 3, 0, 9, 6, 0],
        [9, 0, 0, 6, 0, 2, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 2]
    ]
    return board

def main():
    #sudoku board
    #Any place that has a 0 needs to be solved
    board = get_board()

    print("Original board:", end='\n')
    for y in board:
        print(y)

    solve(board)
    print()
    print("Solved board:")
    for y in board:
        print(y)

if __name__ == '__main__':
    main()

