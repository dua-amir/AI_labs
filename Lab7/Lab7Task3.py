# Define possible directions the blank (0) tile can move from its current position
def get_moves(pos):
    x, y = pos  # Current position of the blank tile
    return {
        "UP": (x - 1, y),     # Move blank up
        "DOWN": (x + 1, y),   # Move blank down
        "LEFT": (x, y - 1),   # Move blank left
        "RIGHT": (x, y + 1)   # Move blank right
    }

# Find where the blank tile (represented by 0) is in the current board
def find_blank(board):
    for i in range(3):             # Loop through rows
        for j in range(3):         # Loop through columns
            if board[i][j] == 0:   # If blank tile is found
                return (i, j)      # Return its position (row, column)

# Make a copy of the board and perform the tile move (swap blank with adjacent tile)
def move_tile(board, from_pos, to_pos):
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    x1, y1 = from_pos                      # Position of the blank
    x2, y2 = to_pos                        # New position to move the blank to
    # Swap the blank with the target tile
    new_board[x1][y1], new_board[x2][y2] = new_board[x2][y2], new_board[x1][y1]
    return new_board                       # Return the new board after the move

# Check if two boards are the same (used to check if we reached the goal)
def boards_equal(b1, b2):
    return b1 == b2  # Returns True if both boards are equal

# Convert board to a tuple of tuples (needed to store in visited list)
def board_to_tuple(board):
    return tuple(tuple(row) for row in board)  # Convert nested lists to nested tuples

# Solve the puzzle using Breadth-First Search
def solve_puzzle(start, goal):
    queue = [(start, [])]  # Each item is (current_board, moves_taken_so_far)
    visited = []           # To keep track of boards we've already explored

    # Loop until queue is empty
    while queue:
        current_board, path = queue.pop(0)  # Get the first board and the path taken

        # If goal state is reached
        if boards_equal(current_board, goal):
            print("Solved in", len(path), "moves!")        # Print total number of moves
            print("Moves:", " -> ".join(path))                # Print the move sequence
            return path                                       # Return the path of moves

        board_key = board_to_tuple(current_board)             # Convert current board to tuple form
        if board_key in visited:                              # If we've already visited this state
            continue                                           # Skip to the next iteration
        visited.append(board_key)                             # Mark this board as visited

        blank_pos = find_blank(current_board)                 # Find where the blank tile is
        possible_moves = get_moves(blank_pos)                 # Get all possible move directions

        # Try every move (up, down, left, right)
        for move_name in possible_moves:
            new_pos = possible_moves[move_name]               # New position of the blank after move
            x, y = new_pos
            if 0 <= x < 3 and 0 <= y < 3:                     # Check if the move is within bounds
                new_board = move_tile(current_board, blank_pos, new_pos)  # Get new board after move
                queue.append((new_board, path + [move_name]))             # Add to queue with updated path

    # If the loop ends without finding a solution
    print("No solution found.")
    return None  # Return nothing

# Starting board
initial_state = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

# Target board (goal)
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Print initial board
print("Initial State:")
for row in initial_state:
    print(row)

# Print goal board
print("\nGoal State:")
for row in goal_state:
    print(row)

print("\nSolving...\n")  # Let the user know it's working...

# Call the function to solve the puzzle
solve_puzzle(initial_state, goal_state)
