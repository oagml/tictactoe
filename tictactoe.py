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
    boardSep = ('-'*5 + '|')*2 + ('-'*5)

    for i in range(3): #Print row
        print(boardSep)
        for j in range(3): #Print column
            if j == 2: #if the last column of the row is printed, ommit the column separator 'I'
                print('  ' + boardValues[board[i][j]], end = "")
            else:
                print('  ' + boardValues[board[i][j]] + '  |', end = "")

        print() #Prints newline


#Get input from player
def playerInput(board):

    validInput = False #Flag used to control the validatio of user input

    while(validInput == False):

        row, column = [int(x) for x in input("Enter the row and column values you want to play (separated by a comma): ").split(',')]

        #Verify the user entered valid row and column positions
        if(row > 2 or row < 0 or column > 2 or column < 0):
            print("Error: You can only enter values from 0 - 2 \n")
            validInput = False
        else:
            print(f"You entered the values: {row}, {column}")
            validInput = True

        #Verify the slot chosen by the player is actually empty
        if (board[row][column] == 0):
            validInput = True
        else: #if the slot already contains an X or O, the input is Invalid
            print("This space has already been played, choose another one")
            validInput = False

    return row, column


#Create a function that determines the winner of the game
#How does it work?
#Define all the possible winning positions and scan the board to find if Xs or Os are filling
#the winning positions
#This is not an elegant solution in any way
#Winning  row positions: [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]
#Winning  column  positions: [[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]]
#Winning  diagonal positions: [[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]

def findWinner (board):
    
    winningRows = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]
    winningCols = [[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]]
    winningDiags = [[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]

    for i in winningRows:
        for j in winningRows[i]:
            









#Flag for controlling the end of the game
gameOver = False
#Total number of turns played
turnNum= 0
#Current player turn. X player (1) goes first.
currentPlayer = 1
#Current row being played
cRow = 0
#Current column being played
cCol = 0


board = initBoard()
print("Game Start!")
#Game loop
while (gameOver == False):

    print(f"It's {boardValues[currentPlayer]}'s turn!")
    
    #Player enters the slot he/she wants to play
    cRow, cCol = playerInput(board)

    #Slot is updated with the corresponding symbol
    if (currentPlayer == 1): #If it's X's turn 
        board[cRow][cCol] = 1
    elif (currentPlayer == 2): #If it's O's turn
        board[cRow][cCol] = 2
    else:
        board[cRow][cCol] = 0

    #Display the board with the updated values
    displayBoard(board)

    #Change the turn to the other player
    if (currentPlayer == 1):
        currentPlayer = 2
    else:
        currentPlayer = 1














