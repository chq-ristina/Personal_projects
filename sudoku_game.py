import pygame
import sudoku_solver
"""
Christina Phillips

A sudoku game that uses the program sudoku_solver.py
To input a number: The player must click on the box and then input the number
If the number that the player inputted was correct, the number will be purple,
if it is incorrect, the number will be red
To delete a number: Click on the box and hit the backspace button
To have the computer solve the puzzle for the player: Hit the spacebar
To clear the sudoku board: Hit enter
"""
#initialize pygame
pygame.init()

#initalize pygame font
pygame.font.init()

background_color = (245, 244, 237)
buffer = 5

#board that will be edited
board = sudoku_solver.get_board()

# will store the original board and will be used if the user wants the solution to the board
old_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]

#holds the solved board for comparisons
solved = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
sudoku_solver.solve(solved)

"""
Clears the board
"""
def clear(screen):
    for i in range(len(old_board)):
        for j in range(len(old_board)):
            if(old_board[i][j] == 0):
                board[i][j] = 0
                pygame.draw.rect(screen, background_color, (
                    (j + 1) * 50 + buffer, (i + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                pygame.display.update()

"""
Inserts a number into the board
"""
def insert(screen, position):
    i,j = position[1], position[0]
    font_ = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(old_board[i-1][j-1] != 0):
                    return
                #deletes a value from the board
                if(event.key == pygame.K_BACKSPACE):
                    board[i-1][j-1] = 0
                    pygame.draw.rect(screen, background_color, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  #Checking for valid input
                    pygame.draw.rect(screen, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    #value is correct
                    if (event.key - 48 == solved[i-1][j-1]):
                        value = font_.render(str(event.key-48), True, (75, 12, 102))
                    #value is wrong
                    else:
                        value = font_.render(str(event.key - 48), True, (255, 0, 0))
                    screen.blit(value, (position[0]*50 +15, position[1]*50))
                    board[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return
"""
Shows how sudoku_solver.py solves the board 
"""
def solving(screen, board):
    #clear screen in case of existing numbers already on the board
    clear(screen)
    font_ = pygame.font.SysFont('Comic Sans MS', 35)

    # finds an empty space in the board
    empty = sudoku_solver.find_empty(board)

    # board is solved
    if not empty:
        return True
    # board is not solved
    else:
        r, c = empty

    # Goes through all the possible solution numbers
    for x in range(1, 10):
        # x is not already in the board
        if not sudoku_solver.contains(board, x, r, c):
            board[r][c] = x  # add x to board
            #adds value to board
            value = font_.render(str(board[r][c]), True, (75, 12, 102))
            screen.blit(value, ((c + 1) * 50 + 15, (r + 1) * 50))
            pygame.display.update()

            # check if the board has been solved
            if solving(screen, board):
                return True

            # board hasn't been solved so return that value back to 0 and try again with a new number
            board[r][c] = 0
            if(board[r][c] == 0):
                #Erases value from board
                pygame.draw.rect(screen, background_color, (
                    (c + 1) * 50 + buffer, (r + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                pygame.display.update()

    return False


def main():
    #create screen
    screen = pygame.display.set_mode((550, 550))

    #Title and Icon
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load('sudoku.png')
    pygame.display.set_icon(icon)

    screen.fill(background_color)

    font_ = pygame.font.SysFont('Comic Sans MS', 35)

    #Make grid
    for i in range(0, 10):
        #for the boxes
        if (i % 3 == 0):
            # vertical
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            # horizontal
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        #vertical
        pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        #horizontal
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(len(board)):
        for j in range(len(board)):
            if(0 < board[i][j] and board[i][j] < 10):
                value = font_.render(str(board[i][j]), True, (27, 49, 56))
                #add it to screen
                screen.blit(value, ((j+1)*50 + 15, (i + 1)*50))
    pygame.display.update()

    #Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(screen, (pos[0]//50, pos[1]//50))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving(screen, old_board)
                if event.key == pygame.K_RETURN:
                    clear(screen)
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
