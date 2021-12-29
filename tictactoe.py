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
import tkinter as tk
import tkinter.messagebox
import random

root = tk.Tk()
root.title("Tic Tac Toe")

#How the program works:
#In the program, each symbol will be equivalent to the following values:
'''
0 = ' ' (Blank or empty space)
1 = 'X'
2 = 'O'
'''
board_values = {0:' ', 1:'X', 2:'O'}

class gameButton:
    def __init__(self, row, column):
        self.row = row
        self.column = column

gButton1 = gameButton(row=0, column=0)
gButton2 = gameButton(row=0, column=1)
gButton3 = gameButton(row=0, column=2)
gButton4 = gameButton(row=1, column=0)
gButton5 = gameButton(row=1, column=1)
gButton6 = gameButton(row=1, column=2)
gButton7 = gameButton(row=2, column=0)
gButton8 = gameButton(row=2, column=1)
gButton9 = gameButton(row=2, column=2)


def init_board () -> list:
    """Initializes a board filled with zeroes and returns it"""
    return [[0,0,0],[0,0,0],[0,0,0]]

button_1 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_1, current_player[0], gButton1))
button_2 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_2, current_player[0], gButton2))
button_3 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_3, current_player[0], gButton3))
button_4 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_4, current_player[0], gButton4))
button_5 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_5, current_player[0], gButton5))
button_6 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_6, current_player[0], gButton6))
button_7 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_7, current_player[0], gButton7))
button_8 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_8, current_player[0], gButton8))
button_9 = tk.Button(root, text=" ", font=("Helvetica", 30), height=3, width=4,
        command=lambda: click_btn(button_9, current_player[0], gButton9))
button_restart = tk.Button(root, text="Restart", font=("Helvetica", 10), height=3, width=45)

#Put the buttons on the screen
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_restart.grid(row=4, columnspan = 3)

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
            #raise ValueError("You can only enter values from 0 - 2")
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
#Current player turn. X player (1) goes first.
current_player = [1]
#Current row being played
row = 0
#Current column being played
col = 0


board = init_board()
print("Game Start!")

def click_btn(button: tk.Button, player: int, gButton: gameButton) ->None:
    """ Update the button that has been selected in the grid."""
    row = gButton.row
    col = gButton.column

    if board[row][col] != 0: #If that space has already been played
        tk.messagebox.showerror("Tic Tac Toe", "This space has been already been played")
        return None

    else:
        print("Writing Value")

        if player == 1:
            button.configure(text = "X")
            board[row][col] = 1

        else:
            button.configure(text = "O")
            board[row][col] = 2

    #Check if X already won the game
    if(find_winner(board) == 1):
        print("X won the game!")
        tk.messagebox.showinfo("Tic Tac Toe", "X won the game!")
        game_over = True

    #Check if Y already won the game
    elif(find_winner(board) == 2):
        print("O won the game!")
        tk.messagebox.showinfo("Tic Tac Toe", "O won the game!")
        game_over = True

    #Change the turn to the other player
    if (player == 1):
        current_player[0] = 2
    else:
        current_player[0] = 1



root.mainloop()
