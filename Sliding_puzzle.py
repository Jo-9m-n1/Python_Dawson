import random
def tileLabs(n):
    tile_board = []
    for i in range(1, n ** 2):
        tile_board.append(str(i) + ' ')
    tile_board.append('  ')
    return tile_board
        
def getNewPuzzle(n):
    tile_board = tileLabs(n)
    random.shuffle(tile_board)
    puzzle = [tile_board[i * n:(i + 1) * n] for i in range(n)]
    return puzzle
    
def findEmptyTile(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == '  ':
                return (i, j)

def nextMove(n):
    puzzle = getNewPuzzle(n)
    while True:
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
        print("Valid moves: ", valid_moves)
        move = input("Enter WASD (or QUIT): ").upper()
        
        if move in valid_moves:
            new_i, new_j = valid_moves[move]
            puzzle[i][j], puzzle[new_i][new_j] = puzzle[new_i][new_j], puzzle[i][j]
            displayBoard(puzzle)
            print("Valid moves: ", valid_moves)
        elif move == 'quit'.upper():
            print("Game terminated by user.")
            break
        else:
            print("Invalid move. Try again.")
            displayBoard(puzzle)
            print("Valid moves: ", valid_moves)

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

print(nextMove(3))








        
        
        




