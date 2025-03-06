# Jongmin Lee, 2432787
import random

def tileLabs(n):
    tile_board = []
    for i in range(1, n ** 2):
        if i < 10:
            tile_board.append(str(i) + ' ')
        else:
            tile_board.append(str(i))
    tile_board.append('  ')
    return tile_board
        
def getNewPuzzle(n):
    tile_board = tileLabs(n)
    random.shuffle(tile_board)
    puzzle = [tile_board[i * n:(i + 1) * n] for i in range(n)]
    return puzzle
    
def findEmptyTile(puzzle):
    row = 0
    col = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == '  ':
                row = i
                col = j
    return (row, col)

def nextMove(n):
    x = 7 * (n ** 2) - 32 + 100
    puzzle = getNewPuzzle(n)
    print(f'You have {x} moves left.')
    while True:
        if checkWin(puzzle):
            displayBoard(puzzle)
            print('-' * 57)
            print("Congratulations! You have solved the puzzle.")
            break
        else:
            if x == 0:
                print('Best of luck next time!')
                break

        (i, j) = findEmptyTile(puzzle)

        valid_moves = {}
        if i > 0:
            valid_moves['W'] = (i - 1, j)
        if i < n - 1:
            valid_moves['S'] = (i + 1, j)
        if j > 0:
            valid_moves['A'] = (i, j - 1)
        if j < n - 1:
            valid_moves['D'] = (i, j + 1)
            
        displayBoard(puzzle)
        move_display = ['(W)' if 'W' in valid_moves else '( )',
                        '(A)' if 'A' in valid_moves else '( )',
                        '(S)' if 'S' in valid_moves else '( )',
                        '(D)' if 'D' in valid_moves else '( )']
        
        print('     ' + move_display[0])
        print(move_display[1] + '  ' + move_display[2] + '  ' + move_display[3])

        move = input("Enter WASD (or QUIT): ").upper()
        
        if move in valid_moves:
            new_i, new_j = valid_moves[move]
            puzzle[i][j], puzzle[new_i][new_j] = puzzle[new_i][new_j], puzzle[i][j]
        elif move == 'quit'.upper():
            print("Game terminated by user.")
            break
        else:
            print("Invalid move. Try again.")
        print('-' * 57)
        x -= 1
        print(f'You have {x} moves left.')


def checkWin(puzzle):
    n = len(puzzle)
    correct = 1
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] != '  ':
                if int(puzzle[i][j]) != correct:
                    return False
                correct += 1
    return True

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))


print("Welcome to the Sliding Puzzle Game!")
n = int(input('Enter the size of the dimension of the puzzle board (minimum 3 & maximum 9): '))
while n < 3:
    print('Invalid input. Minimum size is 3.')
    n = int(input('Enter the size of the dimension of the puzzle board (minimum 3 & maximum 9): '))
while n > 9:
    print('Invalid input. Maximum size is 9.')
    n = int(input('Enter the size of the dimension of the puzzle board (minimum 3 & maximum 9): '))
print('+' + '-' * 54 + '+')
print(f'| You are playing a {n}x{n} puzzle board.                  |')
print('| The empty tile is represented by a blank space.      |')
print('| The goal is to arrange the tiles in ascending order  |')
print('| from left to right.                                  |')
print('| You can move the empty tile to the left, right, up,  |')
print('| or down.                                             |')
print("+" + "-" * 54 + "+")
play = input('Press enter if you understand the game').lower()

if play == '':
    nextMove(n)
else:
    print('Game terminated by user.')