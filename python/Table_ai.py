from board import Board
import random
import pickle
import sys
import numpy as np

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

    def train(self, readFile=False, saveFile="table.txt"):

        if readFile:
            with open(readFile, "rb") as fp:
                table = pickle.load(fp)
        else:
            table = self.table

        Run(1000, 0.1)
        Run(1000, 0.08)
        Run(1000, 0.05)
        Run(50000, 0.02)
        Run(1000, 0.07)
        Run(100000, 0.01)
        print('done')

        if saveFile:
            with open(saveFile, "wb") as fp:
                pickle.dump(table, fp)

        return table

    def updateState(self, pos_stack, flag, table):
        br = Board()
        if flag == 2:
            print('draw')
        # print("new_game")
        # print()
        # print()
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

    def Run(self, ITER=1, rand=0.01, debug=False, table=False, saveFile="table.txt"):
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
                    while (flag == 4 and cnt < 20):
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
                pickle.dump(table, fp)
        return table


def greedyMove( b, table, debug):
    best_move = -1
    best_prob = 0.0

    for col in range(NUM_COLS):

        next_pos, flag = b.tryMove(col)
        next_pos = tuple(next_pos)
        if flag == 0:
            ## code

            values = table.get(next_pos, DEFAULT_STATE)
            prob = values["wins"] / float(values["seen"])


            prob += random.gauss(0, 0.01 )

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
