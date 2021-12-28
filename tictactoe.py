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

#Import modules
import random

#How the program works:
#In the program, each symbol will be equivalent to the following values:
'''
0 = ' ' (Blank or empty space)
1 = 'X'
2 = 'O'
'''
board_values = {0:' ', 1:'X', 2:'O'}

def init_board () -> list:
    """Initializes a board filled with zeroes and returns it"""
    return [[0,0,0],[0,0,0],[0,0,0]]


def display_board(board: list) -> None:
    """Print the board in the terminal."""
    board_sep = ('-'*5 + '|')*2 + ('-'*5)

    for i in range(3): #Print row
        print(board_sep)
        for j in range(3): #Print column
            if j == 2: #if the last column of the row is printed, ommit the column separator 'I'
                print('  ' + board_values[board[i][j]], end = "")
            else:
                print('  ' + board_values[board[i][j]] + '  |', end = "")

        print() #Prints newline


def rand_input(board: list) -> int:
    """ Pick a random space in the board to play."""

    valid_input = False #Flag used to control the validatio of user input

    while(valid_input == False):

        row = random.randrange(3)
        column = random.randrange(3)

        #Verify the space randomly chosen is empty
        if (board[row][column] == 0):
            valid_input = True
        else: #if the slot already contains an X or O, the input is Invalid
            #print(f"This space ({row},{column}) has already been played, choose another one")
            valid_input = False

    return row, column
    

#Get input from player
def player_input(board: list) -> int:
    """
    Request the current player to enter the slot they want to play and verify if 
    it is a playable space.

    Args:
        board -- 2 dimmensional list that represents the board
    Return:
        row, column -- these values represent the space in the board chosen by the player
    """

    valid_input = False #Flag used to control the validatio of user input

    while(valid_input == False):

        row, column = [int(x) for x in input("Enter the row and column values you want to play (separated by a comma): ").split(',')]

        #Verify the user entered valid row and column positions
        if(row > 2 or row < 0 or column > 2 or column < 0):
            print("Error: You can only enter values from 0 - 2 \n")
            valid_input = False
        else:
            print(f"You entered the values: {row}, {column}")
            valid_input = True

        #Verify the slot chosen by the player is actually empty
        if (board[row][column] == 0):
            valid_input = True
        else: #if the slot already contains an X or O, the input is Invalid
            print("This space has already been played, choose another one")
            valid_input = False

    return row, column


#Define all the possible winning positions and scan the board to find if Xs or Os are filling
#the winning positions
#Winning  row positions: [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]
#Winning  column  positions: [[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]]
#Winning  diagonal positions: [[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]

def find_winner (board: list) -> int:
    """ Determine if the board contains a winner position

    Args:
        board -- a two dimmensional list that represents the board
    Returns:
        int: 0 = No winner, 1 = X won, 2 = O won

    """
    winner = 0

    for i in range(3):
        #Check if there is a winning row
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            if board[i][0] == 1:
                winner = 1
            elif board[i][0] == 2:
                winner = 2
            else:
                winner = 0
        #Check if there is a winning column
        if(board[0][i] ==  board[1][i] and board[1][i] == board[2][i]):
            if board[0][i] == 1:
                winner = 1
            elif board[0][i] == 2:
                winner = 2
            else:
                winner = 0

        #Check if there is a winning column
        if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if board[0][0] == 1:
                winner = 1
            elif board[0][0] == 2:
                winner = 2
            else:
                winner = 0
        if(board[2][0] == board[1][1] and board[1][1] == board[0][2]):
            if board[2][0] == 1:
                winner = 1
            elif board[2][0] == 2:
                winner = 2
            else:
                winner = 0

    return winner



#Flag for controlling the end of the game
game_over = False
#Total number of turns played
turn_num= 0
#Current player turn. X player (1) goes first.
current_player = 1
#Current row being played
row = 0
#Current column being played
col = 0


board = init_board()
print("Game Start!")

#Game loop
while (game_over == False):

    print(f"It's {board_values[current_player]}'s turn!")
    
    #If it's X's turn, player enters the input
    if (current_player == 1):
        row, col = player_input(board)
    else: #If it's O's turn, computer randomly enters the input
        row, col = rand_input(board)

    #Space is updated with the corresponding symbol
    if (current_player == 1): #If it's X's turn 
        board[row][col] = 1
    elif (current_player == 2): #If it's O's turn
        board[row][col] = 2
    else:
        board[row][col] = 0

    #Display the board with the updated values
    display_board(board)

    #Check if X already won the game
    if(find_winner(board) == 1):
        print("X won the game!")
        game_over = True

    #Check if Y already won the game
    elif(find_winner(board) == 2):
        print("O won the game!")
        game_over = True

    #Change the turn to the other player
    if (current_player == 1):
        current_player = 2
    else:
        current_player = 1


