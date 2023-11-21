import random

snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

class Player:
    def __init__(
        self,
        start: int=0,
        end: int=100,
        snakes: dict={},
        ladders: dict={},
        num_of_dice: int=1,
        sides_of_dice: int=6
        ) -> None:

        self.position = start
        self.end = end
        self.snakes = snakes
        self.ladders = ladders

        self.num_of_dice = num_of_dice
        self.sides_of_dice = sides_of_dice

        self.num_turns = 0
        self.game_has_ended = False

    def __str__(self) -> str:
        return f"Player position: {self.position}\nNumber of moves: {self.num_turns}\n"

    @property
    def roll(self) -> int:
        moves = 0
        for i in range(self.num_of_dice):
            moves += random.randint(1, self.sides_of_dice)
        return moves

    @property
    def check_position(self) -> int:
        if self.position in self.ladders.keys():
            return self.ladders[self.position]
        elif self.position in self.snakes.keys():
            return self.snakes[self.position]
        else:
            return self.position
        
    def make_a_move(self, position: int) -> None:
        self.num_turns += 1
        self.position = self.position + self.roll

        if self.position >= self.end:
            self.game_has_ended = True
            print(f"Game won after {self.num_turns} moves!\n")
        else:
            self.position = self.check_position
            # print(self)

    @property
    def play_a_game(self) -> None:
        while self.num_turns <= self.end and self.game_has_ended == False:
            self.make_a_move(self.position)
            

n = 0
turns = []

while n < 10000:
    n += 1
    print(f"Round {n}")
    player_one = Player(snakes=snakes, ladders=ladders)
    player_one.play_a_game
    turns.append(player_one.num_turns)

print(f"Minimum turns after {n} tries: {min(turns)}")
