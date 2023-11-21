import numpy as np


def create_transition_matrix(board_size: int, snake_ladder: dict, sides_of_dice: int = 6) -> np.ndarray:
    
    size = board_size + 1
    transition_matrix = np.zeros((size, size))

    # Fill in transition probabilities based on dice roll
    for i in range(size):
        for j in range(1, sides_of_dice + 1):
            next_position = min(i + j, size - 1)  # Ensure we stay within the board
            transition_matrix[i, next_position] += 1 / sides_of_dice  # Assume a fair 6-sided dice

    # Incorporate snakes and ladders
    for row in transition_matrix:
        for ladder_bottom, ladder_top in snake_ladder["ladders"].items():
            if row[ladder_bottom] > 0:
                row[ladder_top] = row[ladder_top] + row[ladder_bottom]
                row[ladder_bottom] = 0
        for snake_head, snake_tail in snake_ladder["ladders"].items():
            if row[snake_head] > 0:
                row[snake_tail] = row[snake_tail] + row[snake_head]
                row[snake_head] = 0

    return transition_matrix


# Define game board.
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
size = 100

transition_matrix = create_transition_matrix(
    board_size = size,
    snake_ladder={
        "snakes":snakes,
        "ladders":ladders
    },
)
 
#set start position:
row_vector = np.zeros((1, size + 1))[0]
row_vector[0]  = 1 # probability is 100% in the first round to start here

n = 0

while row_vector[-1] == 0 and n < 100:
    n += 1
    row_vector = np.dot(row_vector, transition_matrix)

print(f"Minimum turns: {n}")




