from enum import Enum

WHITE = 0
BLACK = 1
WC = 'o'
BC = 'x'

ROWS = [127, 16256, 2080768, 266338304, 34091302912, 4363686772736]
COLS = [34630287489, 69260574978, 138521149956, 277042299912, 554084599824, 1108169199648, 2216338399296]

class Board:
    def __init__(self):
        self.position = [0, 0]
        self.color = WHITE

    def play(self, col):
        taken = self.all_pieces() & COLS[col]
        for row, r in enumerate(ROWS):
            if not(taken & r):
                self.position[self.color] |= r & COLS[col]
                self.print_board()
                self.is_game_over(row, col)
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

    def is_game_over(self, row, col) :
        pieces = self.position[self.color]

        full_col = COLS[col]
        full_row = ROWS[row]
        win_count = 0;
        
        for r in ROWS :
            win_count = win_count+1 if r & full_col & pieces else 0
            if win_count > 3 : print("PLAYER WON | ")

        for c in COLS :
            win_count = win_count+1 if c & full_row & pieces else 0
            if win_count > 3 : print("PLAYER WON - ")

        #/
        if row >= col :
               for idx, r in enumerate(ROWS[row-col:]) :
                   win_count = win_count+1 if r & COLS[idx] & pieces else 0
                   if win_count > 3 : print("PLAYER WON /+ ")
                   
        else :
            for idx, c in enumerate(COLS[col-row:]) :
                win_count = win_count+1 if c & ROWS[idx] & pieces else 0
                if win_count > 3 : print("PLAYER WON /- ")
    
        #NOT WORKING
        col_max = len(COLS)-1
        if row >= col_max-col :
            for idx, r in enumerate(ROWS[row-(col_max-col): ]) :
                win_count = win_count+1 if r & COLS[col_max-idx] & pieces else 0
                if win_count > 3 : print("PLAYER WON \+ ")

        else :
            for idx, c in enumerate(COLS[col+row: 0]) :
                win_count = win_count+1 if c & ROWS[idx] & pieces else 0
                if win_count > 3 : print("PLAYER WON \- ")
    
        #ALSO ADD DRAW
                

b = Board()

while 1 :    
    b.play(ord(input())-ord('a'))
