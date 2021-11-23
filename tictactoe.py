#Tic tac toe
#Tic tac toe is a two player game that is played in a three by three grid where each player will
#mark one space of the grid with one of two symbols "X" or "O". Only one space per turn can be marked

#Wins the player who can align 3 symbols in either a column, row or diagonal line
#Example of a game:
'''
-----I-----I-----
  X  I  X  I  O 
-----I-----I-----
  O  I  X  I  X
-----I-----I-----
  O  I  O  I  X 
'''
#In the example above, the X player wins because it aligned the three Xs in (0,0) (1,1) and (2,2)
#Software functions and components needed:

#Player X: Virtual or human entity that will provide the inputs to the game
#Player O: Virtual or human entity that will provide the inputs to the game
#Game control: Function that controls the game, keeps track of the turn and current player
#Board: Matrix or variable that contains the values of the board
#Display Board: Function that displays the board on the terminal
#Initialize Board: Function that initializes the board with empy or blank values
#Update Board: Function that updates the values of the board

#How the program works:
#In the program, each symbol will be equivalent to the following values:
'''
0 = ' ' (Blank or empty space)
1 = 'X'
2 = 'O'
'''
boardValues = {0:' ', 1:'X', 2:'O'}

#First, the board is initialized with the empty values
#The board will be stored in a two dimmensional list
def initBoard ():
    return [[0,0,0],[0,0,0],[0,0,0]]

def initBoardX ():
    return [[1,1,1],[1,1,1],[1,1,1]]

def initBoardO ():
    return [[2,2,2],[2,2,2],[2,2,2]]

#Display a 3x3 board using a 3x3 list as input
def displayBoard(board):
    boardSep = ('-'*5 + 'I')*2 + ('-'*5)

    for i in range(3): #Print row
        print(boardSep)
        for j in range(3): #Print column
            if j == 2: #if the last column of the row is printed, ommit the column separator 'I'
                print('  ' + boardValues[board[i][j]], end = "")
            else:
                print('  ' + boardValues[board[i][j]] + '  I', end = "")

        print() #Prints newline

board = initBoardO()
displayBoard(board)
