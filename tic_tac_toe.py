def create_board():
    """
    Creates 3x3 board to be used in the game of tic-tac-toe.
    Returns dictionary representing board.
    """
    board =[]
    board.append([i for i in range(1, 4)])
    board.append([i for i in range(4, 7)])
    board.append([i for i in range(7, 10)])

    return board


def board_display(board):
    """
    Generates board to be displayed with numbers representing options 
    and player moves represented with X's and O's."""
    display = "\n"
    for row in board:
        display += "\t\t\t" + str(row[0]) + "   " + str(row[1]) 
        display += "   " + str(row[2]) + "\n"
    
    return display


def prompt_user(board, turn):
    """
    Prompts user to select valid number represented on board.
    returns number selected.
    """
    avail_numbers = []
    for row in board:
        for column in row:
            if type(column) == int: avail_numbers.append(column)

    while True:
        # Display board for user prompt attempt.
        print(board_display(board))

        number = input(turn + "'s Turn. Please Enter A Displayed Number: ").strip()

        if (number.lower() == "quit" and confirm_exit()): return 0

        if (number.isdigit() and int(number) in avail_numbers): return int(number)

        print("Invalid Number Entered...Try Again!")


def confirm_exit():
    """Confirms user decision to exit program."""
    confirmation = input("\nEnter \"No\" to Continue Playing" + 
        " / Any Key to Confirm Exit: ")

    print()

    return confirmation.lower().strip() != "no"


def update_board(board, turn, number):
    """
    Updates board with 'X'/'O', depending on whose turn it is 
    at the specific number slot selected by player.
    returns board, reflecting move.
    """
    for row in range(len(board)):
        for column in range(len(board[row])):
            if (board[row][column] == number):
                board[row][column] = turn

    return board


def evaluate_board(board):
    """
    Evaluates current state of game through board (win/draw/continue). 
    returns result of evaluation.
    """
    if (check_win(board)): return "win"
    
    # Check continue (numbers still present on board)
    for row in range(len(board)):
        for column in range(len(board[row])):
            if (type(board[row][column]) == int): return "continue"

    # Thus draw.
    return "draw"


def check_win(board):
    """
    Evaluates whether board contains 3 consecutive X/O's 
    (vertically, horizontally and diagonally) thus resulting in a win outcome.
    """
    # Check first Column, for win.
    return (board[0][0] == board[1][0] == board[2][0] or

    # Check second Column, for win.
    board[0][1] == board[1][1] == board[2][1] or

    # Check third Column, for win.
    board[0][2] == board[1][2] == board[2][2] or

    # Check first Row, for win.
    board[0][0] == board[0][1] == board[0][2] or  

    # Check second Row, for win.
    board[1][0] == board[1][1] == board[1][2] or

    # Check third Row, for win.
    board[2][0] == board[2][1] == board[2][2] or

    # Check left-right diagonal, for win.
    board[0][0] == board[1][1] == board[2][2] or 

    # Check right-left diagonal, for win.
    board[0][2] == board[1][1] == board[2][0])


def display_outcome(board, turn, evaluation):
    """Displays outcome of game."""
    if (evaluation == "win"):
        print("\n" + turn + " Has Won The Game...Congratulations!")

    elif (evaluation == "draw"):
        print("\nGame Ended in a Draw...Better Luck Next Time!")

    print(board_display(board))


def swap_turn(turn):
    """Swaps turn from one player (X/O) to other player (O/X)."""
    if turn == 'X': return 'O'
    return 'X'


def run_game():
    """Runs the tic-tac-toe game program."""
    # Welcome Message.
    print("Welcome to Tic Tac Toe!! Hope You are Ready to Compete!!")

    board = create_board()

    turn = 'X'

    while (True):
        number = prompt_user(board, turn)
        if (number == 0): 
            print("Sad to See You Go...Goodbye!")
            break

        board = update_board(board, turn, number)
        evaluation = evaluate_board(board)

        if (evaluation != "continue"):
            display_outcome(board, turn, evaluation)
            break

        # Swap turn to other player.
        turn = swap_turn(turn)


if __name__ == "__main__":
    run_game()