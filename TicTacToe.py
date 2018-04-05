# Tic Tac Toe


def drawBoard(board):
    # Prints out the board that it was passed.
    # 'board' is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def playAgain():
    # This function returns True if the player wants to play again.
    print('Play Again? (y/n)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    # Make a duplicate of the board list.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    # Return True if the passed move is free.
    return board[move] == ' '


def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or \
            not isSpaceFree(board, int(move)):
        print('Next Move? (1-9)')
        move = input()
    return int(move)


def isBoardFull(board):
    # Return True if every space on the board has been taken.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def getComputerMove(board):
    child, _ = maximize(getBoardCopy(board))
    for i in range(1,10):
        if child[i] != board[i]:
            return i


def score(board):
    if isWinner(board, 'X'):
        return 10
    elif isWinner(board, 'O'):
        return -10
    else:
        return 0


def maximize(board):
    if score(board) != 0:
        return [None, score(board)]

    maxChild, maxUtility = None, float('-inf')

    for i in range(1, 10):
        child = getBoardCopy(board)
        if isSpaceFree(child, i):
            makeMove(child, 'X', i)
            _, utility = minimize(child)

            if utility > maxUtility:
                maxChild, maxUtility = child, utility

    return maxChild, maxUtility


def minimize(board):
    if score(board) != 0:
        return [None, score(board)]

    minChild, minUtility = None, float('inf')

    for i in range(1, 10):
        child = getBoardCopy(board)
        if isSpaceFree(child, i):
            makeMove(child, 'O', i)
            _, utility = maximize(child)

            if utility < minUtility:
                minChild, minUtility = child, utility

    return minChild, minUtility

print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter  = 'O'
    computerLetter = 'X'
    turn = 'Computer'
    print('The ' + turn + ' Will Go First.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You Won!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Game Tie!')
                    break
                else:
                    turn = 'Computer'
        else:
            # Computer’s turn.
            depth = 0
            move = getComputerMove(theBoard)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You Lose!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Game Tie!')
                    break
                else:
                    turn = 'Player'
    if not playAgain():
        break
