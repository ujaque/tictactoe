
board = [' ' for x in range(10)]


def clearBoard():
    for i in range(len(board)):
        board[i] = ' '

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def printBoard(board):
#    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#    print('   |   |   ')
    print('------------')
#    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#    print('   |   |   ')
    print('------------')
#    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#    print('   |   |   \n')
    print('\n')

def menu():
    print('=============')
    print('1) 1 player Game')
    print('2) 2 player Game')
    print('3) Rules')
    print('4) Exit Game')
    print('=============')

    gametype = input('Select: ')
    if gametype == '1':
        onePlayerGame()
    elif gametype == '2':
        twoPlayerGame()
    elif gametype == '3':
        rules()
    elif gametype == '4':
        return 4
    else:
        return '0'


def rules():
    header('RULES')
    print('Tic-tac-toe (American English), noughts and crosses (Commonwealth English),\n '
          'or Xs and Os is a paper-and-pencil game for two players, X and O, who take turns\n'
          ' marking the spaces in a 3×3 grid. The player who succeeds in placing three of their\n'
          ' marks in a horizontal, vertical, or diagonal row is the winner. ')



def header(title):
    print('\n\n===================')
    print('===================')
    print(f'==={title}===')
    print('===================')
    print('===================\n\n')

def isWinner(symbol,board):
    if board[1] == symbol and board[2] == symbol and board[3] == symbol:
        return True
    elif board[4] == symbol and board[5] == symbol and board[6] == symbol:
        return True
    elif board[7] == symbol and board[8] == symbol and board[9] == symbol:
        return True
    elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
        return True
    elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
        return True
    elif board[3] == symbol and board[6] == symbol and board[9] == symbol:
        return True
    elif board[1] == symbol and board[5] == symbol and board[9] == symbol:
        return True
    elif board[3] == symbol and board[5] == symbol and board[7] == symbol:
        return True
    else:
        return False


def game():

    menuoption = '1'
    while menuoption != '0':
        clearBoard()
        menuoption = menu()

def onePlayerGame():
    header('1 PLAYER')

    while not (isBoardFull(board)):
        if not (isWinner('0', board)):
            printBoard(board)
            print('player move')
            playermove()
            printBoard(board)
        else:
            print('computer wins!')
            break

        if isBoardFull(board):
            print('tie game')
            break

        if not (isWinner('X', board)):
            move = computerMove()
            if move == 0:
                print(' ')
            else:
                insertLetter('0', move)
                printBoard(board)
        else:
            print('you win')
            break





def twoPlayerGame():

    player = 1
    symbol = 'X'

    header('2 PLAYER')

    while isBoardFull(board) == False:

        printBoard(board)

        move = input(f'Insert move player {player}: ')

        if spaceIsFree(int(move)):

            insertLetter(symbol, int(move))

            printBoard(board)
            if isWinner(symbol, board):
                print(f'Victory Player {player}\n')
                break

            if player == 1:
                player = 2
                symbol = '0'
            else:
                player = 1
                symbol = 'X'
        else:
            print(f'La posicion {move}, ya esta ocupada, elije otra posicion')

def playermove():

    run = True
    while run:
        move = input(f'Insert move player: ')

        try:
            if spaceIsFree(int(move)):
                insertLetter('X',int(move))
                printBoard(board)
                run = False

            else:
                print(f'La posicion {move}, ya esta ocupada, elije otra posicion')
        except:
            print('Introduce un caracter valido')


def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['0','X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(let, boardcopy):
                move = i
                return move


    emptycorners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            emptycorners.append(i)
    if len(emptycorners) > 0:
        move = selectRandom(emptycorners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    emptysides = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            emptysides.append(i)
    if len(emptysides) > 0:
        move = selectRandom(emptysides)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


game()


