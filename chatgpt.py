import numpy as np

def create_transition_matrix():
    # Create a transition matrix (assuming a 1-6 dice)
    size = 100  # Adjust the size based on your board size
    transition_matrix = np.zeros((size, size))

    # Fill in transition probabilities based on dice roll
    for i in range(size):
        for j in range(1, 7):
            next_position = min(i + j, size - 1)  # Ensure we stay within the board
            transition_matrix[i, next_position] += 1 / 6  # Assume a fair 6-sided dice

    # Incorporate snakes and ladders
    for snake_head, snake_tail in snakes.items():
        transition_matrix[snake_head - 1, snake_tail - 1] = 1

    for ladder_bottom, ladder_top in ladders.items():
        transition_matrix[ladder_bottom - 1, ladder_top - 1] = 1

    return transition_matrix

def min_rounds_to_end(transition_matrix):
    size = transition_matrix.shape[0]
    min_rounds = np.full(size, np.inf)  # Initialize with infinity
    min_rounds[0] = 0  # Starting position has 0 rounds

    for i in range(size):
        for j in range(1, 7):
            next_position = min(i + j, size - 1)  # Ensure we stay within the board
            min_rounds[next_position] = min(min_rounds[next_position], min_rounds[i] + 1)

    return min_rounds[-1]

# Example snakes and ladders
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Create the transition matrix
transition_matrix = create_transition_matrix()

# Find the minimum number of rounds
min_rounds = min_rounds_to_end(transition_matrix)

print(min_rounds)