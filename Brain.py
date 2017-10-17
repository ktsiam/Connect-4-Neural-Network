import numpy as np

class Brain(object):
    """Takes in a board and returns a move"""
    def __init__(self):
        self.neural_network_stuff = 0#who_knows

    def make_move(self, board, color):
        return np.random.randint(0, 7)
