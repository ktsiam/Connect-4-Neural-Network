from enum import Enum

WHITE = 0
BLACK = 1
WC = 'o'
BC = 'x'

ROWS = [127, 16256, 2080768, 266338304, 34091302912, 4363686772736]
COLS = [34630287489, 69260574978, 138521149956, 277042299912, 554084599824, 1108169199648, 2216338399296]

class Col(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Board:
    def __init__(self):
        self.position = [0, 0]
        self.color = WHITE

    def play(self, col):
        taken = self.all_pieces() & COLS[col]
        for index, r in enumerate(ROWS):
            if not(taken & r):
                self.position[self.color] |= r & COLS[col]
                self.print_board()
                is_game_over(index, col)
                self.color ^= True
                return True
        return False

    def all_pieces(self):
        return self.position[WHITE] | self.position[BLACK]

    def print_board(self):
        print("WHITE TO MOVE" if self.color == WHITE else "BLACK TO MOVE")
        for indexr, r in enumerate(reversed(ROWS)):
            s = ""
            s += (str(6-indexr) + " ")
            for c in COLS:
                square = self.all_pieces() & r & c
                if square == 0:
                    s += ("_ ")
                else:
                    s += (WC if (self.position[WHITE] & square) else BC)
                    s+= (" ")
            print(s)
        print("  A B C D E F G\n")

    def is_game_over(self, row, col)


b = Board()
b.print_board() 
b.play(0)