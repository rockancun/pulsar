import numpy as np


class Matrix():

    BORDER = 2

    def __init__(self, size):
        self.size = size + self.BORDER
        self.__matrix = np.zeros((size, size), dtype=int)

    def get_matrix(self):
        return self.__matrix
