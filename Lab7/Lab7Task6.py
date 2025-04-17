import math  # Importing math library for infinity values

# Function to print the current Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Print each row, separating elements with ' | '
    print("\n")  # Print a blank line after the board


# Function to check for a winner in the Tic-Tac-Toe game
def check_winner(board):
    # Check rows and columns for a winner
    for i in range(3):
        # Check if all cells in a row are the same and not empty (' ')
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]  # Return 'X' or 'O' if there's a winner
        # Check if all cells in a column are the same and not empty
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]  # Return 'X' or 'O' if there's a winner

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]  # Return winner from the main diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]  # Return winner from the anti-diagonal

    return None  # Return None if there's no winner yet


# Function to check if there are any moves left on the board
def is_moves_left(board):
    for row in board:
        if ' ' in row:  # If there's an empty space (' ') in any row
            return True  # There are still moves left
    return False  # No moves left


# Minimax algorithm to evaluate the best possible move for a player
def minimax(board, is_maximizing):
    winner = check_winner(board)  # Check if there's a winner

    if winner == 'X':  # If 'X' wins
        return 1  # Return 1 (Maximizing player wins)
    elif winner == 'O':  # If 'O' wins
        return -1  # Return -1 (Minimizing player wins)
    elif not is_moves_left(board):  # If no moves left (draw)
        return 0  # Return 0 (draw)

    if is_maximizing:  # Maximizing player's turn ('X')
        best_score = -math.inf  # Start with the lowest possible score
        # Try every possible move on the board
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Try placing 'X' in the current cell
                    score = minimax(board, False)  # Call minimax recursively for 'O'
                    board[i][j] = ' '  # Undo the move
                    best_score = max(best_score, score)  # Keep the maximum score
        return best_score  # Return the best score for 'X'

    else:  # Minimizing player's turn ('O')
        best_score = math.inf  # Start with the highest possible score
        # Try every possible move on the board
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Try placing 'O' in the current cell
                    score = minimax(board, True)  # Call minimax recursively for 'X'
                    board[i][j] = ' '  # Undo the move
                    best_score = min(best_score, score)  # Keep the minimum score
        return best_score  # Return the best score for 'O'


# Function to find the best move for 'X' (Maximizing player)
def find_best_move(board):
    best_score = -math.inf  # Start with the lowest possible score
    best_move = (-1, -1)  # Initialize the best move as (-1, -1)

    # Try every possible move on the board for 'X'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  # Try placing 'X' in the current cell
                move_score = minimax(board, False)  # Evaluate the move using minimax
                board[i][j] = ' '  # Undo the move

                if move_score > best_score:  # If this move is better than the current best
                    best_score = move_score  # Update the best score
                    best_move = (i, j)  # Update the best move

    return best_move  # Return the best move for 'X'


# Example Tic-Tac-Toe Board
board = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', ' ', 'O']
]

# Print the current board
print("Current Board:")
print_board(board)

# Find and print the best move for 'X'
best_move = find_best_move(board)
print(f"Best Move for X: {best_move}")
