from player import HumanPlayer,RandomComputerPLayer

class TicTacToe:
    def __init__(self):
        self.board=[] #X O ' '
        for i in range(9):
            self.board.append(' ')
        self.current_winner=None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+'| '.join(row)+'|')

    @staticmethod
    def print_num_board():
        # number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        num_board = []
        for i in range(3):
            row = []
            for j in range(i*3,(i+1)*3):
                row.append(str(j))
            num_board.append(row)
        # print(number_board)
        for each in num_board:
            row = '| '.join(each)
            print('| '+row+'|')
        # print(num_board)

    def available_moves(self):
        available_moves=[]
        for each_position in range(len(self.board)):
            if self.board[each_position] == ' ':
                available_moves.append(each_position)
        return available_moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        row_index = square // 3 #0 1 2  modulus 4 // 3 -> 1
        row = self.board[row_index*3:(row_index+1)*3]
        row_count = 0
        for each in row:
            if each == letter:
                row_count+=1
        if row_count == 3:
            return True

        col_index = square % 3
        column = [self.board [col_index + (i*3)] for i in range(3)]
        column_count = 0
        for each in column:
            if each == letter:
                column_count += 1
        if column_count == 3:
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[x] for x in [0,4,8]]
            diagonal1_count = 0
            for each in diagonal1:
                if each == letter:
                    diagonal1_count += 1
            if diagonal1_count == 3:
                return True

            diagonal2 = [self.board[x] for x in [2,4,6]]
            diagonal2_count = 0
            for each in diagonal2:
                if each == letter:
                    diagonal2_count += 1
            if diagonal2_count == 3:
                return True
            # pass
        return False

def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_num_board()
    letter = 'X'
    while game.empty_squares():
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(f"{letter} make a move in the game to {square}")
                game.print_board()
            if game.current_winner == letter:
                if print_game:
                    print(f"{letter} wins")
                    break


        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'

    if print_game and game.current_winner != letter:
        print('It is a Tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPLayer('O')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)


# | 0 | 1 | 2 |
# | 3 | 4 | 5 |
# | 6 | 7 | 8 |