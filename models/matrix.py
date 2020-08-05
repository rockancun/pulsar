import numpy as np


class Matrix():

    BORDER = 2

    def __init__(self, size):
        self.__size = size
        self.__matrix = self.create_empty_matrix()

    def create_empty_matrix(self):
        size_with_borer = self.get_size_with_border()
        return np.zeros((size_with_borer, size_with_borer), dtype=int)

    def get_matrix(self):
        limit = self.__size + 1
        return self.__matrix[1:limit, 1:limit]

    def update_cell(self, cell_index_x, cell_index_y):
        showable_cell_x = cell_index_x + 1
        showable_cell_y = cell_index_y + 1
        cell = self.__matrix[showable_cell_x][showable_cell_y]
        self.__matrix[showable_cell_x][showable_cell_y] = 1 if cell == 0 else 0

    def get_size_with_border(self):
        return self.__size + self.BORDER

    def next_genetration(self):
        temp_matrix = self.create_empty_matrix()
        for x in range(1, self.__size + 1):
            for y in range(1, self.__size + 1):
                count_neighborhood = self.count_neighborhood(x, y)
                if (self.__matrix[x][y] == 0) and (count_neighborhood == 3):
                    temp_matrix[x][y] = 1
                elif self.__matrix[x][y] == 1 and (count_neighborhood == 3 or count_neighborhood == 2):
                    temp_matrix[x][y] = 1
                else:
                    temp_matrix[x][y] = 0
        self.__matrix = temp_matrix

    def count_neighborhood(self, x, y):
        count = 0
        count += self.__matrix[x-1][y-1]
        count += self.__matrix[x][y-1]
        count += self.__matrix[x+1][y-1]
        count += self.__matrix[x-1][y]
        count += self.__matrix[x+1][y]
        count += self.__matrix[x-1][y+1]
        count += self.__matrix[x][y+1]
        count += self.__matrix[x+1][y+1]
        return count
