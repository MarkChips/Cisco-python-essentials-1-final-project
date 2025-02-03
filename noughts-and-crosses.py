board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(
        f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
"""
    )


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    user = None

    while user == None:
        try:
            user = int(input('Your turn:'))
        except ValueError:
            user = None
            print("That's not a number! Please pick a number 1-9")
        else:
            if user > 9 or user < 1:
                user = None
                print('Invalid number, please pick a number 1-9')

    if user == 1:
        board[0][0] = 'O'
    elif user == 2:
        board[0][1] = 'O'
    elif user == 3:
        board[0][2] = 'O'
    elif user == 4:
        board[1][0] = 'O'
    elif user == 6:
        board[1][2] = 'O'
    elif user == 7:
        board[2][0] = 'O'
    elif user == 8:
        board[2][1] = 'O'
    elif user == 9:
        board[2][2] = 'O'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [(row, column) for row in range(3) for column in range(3) if board[row][column] != 'O' and board[row][column] != 'X']


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    col_1 = [board[0][0], board[1][0], board[2][0]]
    col_2 = [board[0][1], board[1][1], board[2][1]]
    col_3 = [board[0][2], board[1][2], board[2][2]]
    diag_1 = [board[0][0], board[1][1], board[2][2]]
    diag_2 = [board[0][2], board[1][1], board[2][0]]

    board.append(col_1)
    board.append(col_2)
    board.append(col_3)
    board.append(diag_1)
    board.append(diag_2)

    for line in board:
        print(line)
        if line.count(sign) == 3:
            return True
    return False


# def draw_move(board):
    # The function draws the computer's move and updates the board.
