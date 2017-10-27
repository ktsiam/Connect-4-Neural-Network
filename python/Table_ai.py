from board import Board
import random
import pickle
import sys
import numpy as np
import time

# table = {}
NUM_COLS = 7
NUM_ROWS = 6
NUM_ITERATIONS = 30
DEFAULT_STATE = {'wins': 12, 'seen': 20}
WIN_STATE = {'wins': 10, 'seen': 10}

class Table_ai:
    def __init__(self, readFile=False):
        if readFile:
            with open(readFile, "rb") as fp:
                self.table = pickle.load(fp)
        else:
            self.table = {}

    def playHuman(self):
        b = Board()
        while(1):
            b.play(greedyMove(b, self.table, True), True)
            b.play(int(input()), True)
            time.sleep(1)
        

    def updateState(self, pos_stack, flag, table):
        br = Board()
        if flag == 2:
            print('draw')
        # print("new_game")
        # print(len(pos_stack))
        for i in range(len(pos_stack)):


            pos = pos_stack.pop()
            if pos not in self.table:
                self.table[pos] = DEFAULT_STATE.copy()

            # print(self.table[pos])
            ## add 1 to wins for player who had last state
            self.table[pos]["wins"] += i & 1 ^ 1
            self.table[pos]["seen"] += 1

            # print(self.table[pos])
            # br.print_board(pos, 1)
        # return table

    def Run(self, ITER=1, rand=0.01, debug=False, saveFile="table.txt"):
        b = Board()
        # if table == False:
        #     table = self.table

        print(ITER, rand, debug)
        for i in range(ITER):
            # print(i, end=" ")
            # print(i)

            # play one game
            pos_stack = []
            while(1 ):
                # print("p", end=" ")

                ## epsilon exploration
                if random.random() < rand:
                    flag = 4
                    cnt = 0
                    while (flag == 4 and cnt < 200):
                        best_move = np.random.randint(0, NUM_COLS)
                        next_pos, flag = b.tryMove( best_move )
                        cnt += 1
                        # if cnt > 3:

                            # print("f:",flag, flag==4, end= "  ")
                ## choose best move
                else:
                    best_move = greedyMove(b, self.table, debug)

                ## play chosen move
                flag, pos = b.play(best_move, debug)

                pos_stack.append( tuple(pos) )
                # game over
                if flag != 0:
                    # win_clr = curr_clr
                    break

            self.updateState(pos_stack, flag, self.table)
        if saveFile:
            with open(saveFile, "wb") as fp:
                pickle.dump(self.table, fp)
        return self.table



def greedyMove( b, table, debug=False):
    best_move = -1
    best_prob = 0.0

    for col in range(NUM_COLS):

        next_pos, flag = b.tryMove(col)
        next_pos = tuple(next_pos)
        if flag == 0:
            ## code

            values = table.get(next_pos, DEFAULT_STATE)
            prob = values["wins"] / float(values["seen"])


            prob += random.gauss(0, 0.001 )

            if debug:
                print(col, round(prob, 4), values)

            if (prob > best_prob):
                best_move = col
                best_prob = prob

        elif flag == 4:
            continue
        else: # won or drawed game
            best_move = col
            table[next_pos] = WIN_STATE.copy()
            break
    return best_move


##
if __name__ == "__main__":
    t = Table_ai("table.txt")
    t.playHuman()
