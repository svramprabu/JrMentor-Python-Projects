import random

class Player:
    def __init__(self, letter):
        self.letter = letter #X,O

    def get_move(self, game):
        pass


class RandomComputerPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves()) #[0,1,2,3,5,6]
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while val not in game.available_moves():
            square = input(self.letter + "'s turn. Input ur move (0-9)")
            val = int(square)
        return val
    # while not valid_square:
        #     square = input(self.letter + "'s turn. Input ur move (0-9)")
        #     try:
        #         val = int(square)
        #         if val not in game.available_moves():
        #             raise ValueError
        #         valid_square = True
        #     except ValueError:
        #         print("Invalid square. Try again")
        # return val
