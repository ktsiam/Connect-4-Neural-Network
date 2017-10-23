from Brain import Brain
from enum import Enum

WHITE = 0
BLACK = 1
WC = 'o'
BC = 'x'

ROWS = [0x7F, 0x3F80, 0x1FC000, 0xFE00000, 0x7F0000000, 0x3F800000000]
COLS = [0x810204081, 0x1020408102, 0x2040810204, 0x4081020408, 0x8102040810, 0x10204081020, 0x20408102040]
FULL = 0x3FFFFFFFFFF

class Board:
    def __init__(self):
        self.position = [0, 0]
        self.color = WHITE    

    #returns flag (0 for none, 1 for win, 2 for draw, 4 for invalid) 
    def play(self, col, debug):
        position, flag = self.tryMove(self.position, self.color, col, debug)
        if (flag == 1 or flag == 2):
            self.position = [0, 0]
            self.color = WHITE
        if (flag == 0):
            self.color = not self.color
        return flag;

    #returns position, flag (0 for none, 1 for win, 2 for draw, 4 for invalid)
    def tryMove(self, pos, clr, col, debug):
        taken = self.all_pieces(pos) & COLS[col]
        for row, r in enumerate(ROWS):
            if not (taken & r):
                pos[clr] |= r & COLS[col]
                game_over = self.is_game_over(row, col, pos, clr, debug)
                return pos, game_over
        return pos, 4                                        

    def all_pieces(self, pos):
        return pos[WHITE] | pos[BLACK]

    def print_board(self, pos, clr):
        print("WHITE TO MOVE" if clr == WHITE else "BLACK TO MOVE")
        for indexr, r in enumerate(reversed(ROWS)):
            s = ""
            s += (str(6-indexr) + " ")
            for c in COLS:
                square = self.all_pieces(pos) & r & c
                if square == 0:
                    s += ("_ ")
                else:
                    s += (WC if (pos[WHITE] & square) else BC)
                    s+= (" ")
            print(s)
        print("  A B C D E F G\n")

    def is_game_over(self, row, col, pos, clr, debug) :
        if debug:
            self.print_board(pos, clr)
        pieces = pos[clr]

        full_col = COLS[col]
        full_row = ROWS[row]

        win_count = 0;        
        for r in ROWS :
            win_count = win_count+1 if r & full_col & pieces else 0
            if win_count > 3 : 
                if debug:
                    print("PLAYER WON | ")
                return 1

        win_count = 0
        for c in COLS :
            win_count = win_count+1 if c & full_row & pieces else 0
            if win_count > 3 : 
                if debug:
                    print("PLAYER WON - ")
                return 1
    
        win_count = 0
        if row >= col :
            for idx, r in enumerate(ROWS[row-col:]) :
                win_count = win_count+1 if r & COLS[idx] & pieces else 0
                if win_count > 3 : 
                    if debug:
                        print("PLAYER WON /+ ")
                    return True
                
        else :
            for idx, c in enumerate(COLS[col-row:]) :
                win_count = win_count+1 if c & ROWS[idx] & pieces else 0
                if win_count > 3 : 
                    if debug:
                        print("PLAYER WON /- ")
                    return 1
    
        win_count = 0
        col_max = len(COLS)-1
        if row >= col_max-col :
            for idx, r in enumerate(ROWS[row-(col_max-col): ]) :
                win_count = win_count+1 if r & COLS[col_max-idx] & pieces else 0
                if win_count > 3 : 
                    if debug:
                        print("PLAYER WON \+ ")
                    return 1

        else :
            for idx, r in enumerate(ROWS[0:row+col+1]) :
                win_count = win_count+1 if r & COLS[col+row-idx] & pieces else 0
                if win_count > 3 :
                    if debug:
                        print("PLAYER WON \- ")
                    return 1
    
        if self.all_pieces(self.position) == FULL :
            if debug:
                print("DRAW")
            return 2;
        return 0;

b = Board()
#brain = Brain()

while 1 :
    # if people are playing
    inp = ord(input())-ord('a')
    if inp > 6:
        print('invalid input')
    elif inp < 0:
        break
    else:
        res = b.play(inp, True)
        if res == 4:
            print('invalid move')
        elif res == 1:
            print('WHITE' if (b.color == WHITE) else 'BLACK', 'WINS!')
        elif res == 2:
            print('DRAW')
        
    # if robots are playing """
    #res = b.play(brain.make_move(b, b.color))
