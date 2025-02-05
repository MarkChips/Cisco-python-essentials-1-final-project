# Noughts and Crosses Game

This is a simple implementation of the classic Noughts and Crosses game in Python, where a human player competes against a computer opponent.

## Features

- Interactive command-line interface
- Visual representation of the game board
- Input validation for user moves
- Random computer moves
- Win detection for both players
- Draw detection when the board is full

## How to Play

1. Run the script in a Python environment.
2. The game starts with the computer's 'X' in the center of the board.
3. Enter a number from 1-9 to place your 'O' in the corresponding position on the board.
4. The computer will automatically make its move after yours.
5. Continue until either you or the computer wins, or the game ends in a draw.

## Functions

- `display_board(board)`: Prints the current state of the board.
- `enter_move(board)`: Handles the human player's move.
- `make_list_of_free_fields(board)`: Returns a list of available moves.
- `victory_for(board, sign)`: Checks if the given sign ('O' or 'X') has won.
- `draw_move(board)`: Makes a random move for the computer.
- `main(board)`: Runs the game loop and determines the outcome.

## Requirements

- Python 3.x
- No additional libraries required

## How to Run

```
python noughts-and-crosses.py
```

Enjoy playing Noughts and Crosses against the computer!
