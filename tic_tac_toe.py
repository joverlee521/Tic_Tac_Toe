import random 

def display_board(board):
    '''
    Prints tic tac toe board in the console
    INPUT: list of markers on the board
    OUTPUT: none
    '''
    print("\n" * 2)
    display = (" {} | {} | {} ".format(board[1], board[2], board[3]), " {} | {} | {} ".format(board[4], board[5], board[6]), " {} | {} | {} ".format(board[7], board[8], board[9]))
    for index, line in enumerate(display):
        print(line)
        # Print dashes only if not the last line of the board
        if index != len(display) -1:
            print("-----------")

def player_input():
    '''
    Asks player to choose a marker
    INPUT: none, takes in input from console
    OUTPUT: 'X' or 'O' depending on which marker player chose
    '''
    marker = " "
    while(marker != "X" and marker != "O"):
        # Continues to ask for player input until they enter X or O
        marker = input("Player 1, please pick a marker 'X' or 'O': ").upper()
    return marker

def place_marker(board, marker, position):
    '''
    Adds a new marker to the board
    INPUT: board list, marker('X' or 'O'), position(int 1-9)
    OUTPUT: updated board list
    '''
    board[position] = marker
    return board 

def win_check(board, marker):
    '''
    Checks if marker has won the game
    INPUT: board list, marker('X' or 'O')
    OUTPUT: boolean(True = won)
    '''
    return (
        # Checks all horizontal lines on the board
        (marker == board[1] == board[2] == board[3]) or (marker == board[4] == board[5] == board[6]) or (marker == board[7] == board[8] == board[9])
        # Checks all vertical lines on the board
    or (marker == board[1] == board[4] == board[7]) or (marker == board[2] == board[5] == board[8]) or (marker == board[3] == board[6] == board[9])
        # Checks the two diagonal lines on the board
    or (marker == board[1] == board[5] == board[9]) or (marker == board[3] == board[5] == board[7]))

def choose_first():
    '''
    Randomly chooses which marker goes first
    INPUT: none
    OUTPUT: choosen marker
    '''
    num = random.randint(1,2)
    print("Randomly choosing who goes first...")
    if num == 1:
        print("X goes first")
        return "X"
    else:
        print("O goes first")
        return "O"

def space_check(board, position):
    '''
    Checks if indicated position on board is empty
    INPUT: board list and position(int 1-9)
    OUTPUT: boolean(True = empty)
    '''
    return board[position] == " "

def full_board_check(board):
    '''
    Checks if the board is full
    INPUT: board list
    OUTPUT: boolean(True = full)
    '''
    return " " not in board

def player_choice(board):
    '''
    Asks player to choose a position by entering an int 1-9, and calls space_check
    INPUT: board list
    OUTPUT: returns position(int 1-9) only if empty
    '''
    position = int(input("Please enter a number (1-9): "))
    if position < 1 or position > 9 or position == '':
        return player_choice(board)
    if space_check(board, position):
        return position
    else:
        print("That space is already taken!")
        return player_choice(board)

def replay():
    '''
    Asks player if they want to play again
    INPUT: none, takes input from console
    OUTPUT: boolean(True = play again)
    '''
    response = input("Would you like to play again? (Y/N): ").upper()
    if response != "Y" and response != "N":
        return replay()
    return response == "Y"

while True:
    board = ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("Welcome to Tic Tac Toe!")
    player_input()
    current_player = choose_first()
    game_on = True
    while(game_on):
        position = player_choice(board)
        place_marker(board, current_player, position)
        display_board(board)
        if win_check(board, current_player):
            print(f"\n {current_player} has won the game!")
            break
        elif full_board_check(board):
            print("\n It's a tie! \n")
            break
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        print(f"\n Change player to {current_player}! \n")
    if not replay():
        break