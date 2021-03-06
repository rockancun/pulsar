import numpy as np


class Matrix():

    BORDER = 2

    def __init__(self, size):
        self.__size = size
        self.__matrix = self.__create_empty_matrix()

    def __create_empty_matrix(self):
        size_with_borer = self.__get_size_with_border()
        return np.zeros((size_with_borer, size_with_borer), dtype=int)

    def __get_size_with_border(self):
        return self.__size + self.BORDER

    def get_matrix(self):
        limit = self.__size + 1
        return self.__matrix[1:limit, 1:limit]

    def update_cell(self, cell_index_x, cell_index_y):
        showable_cell_x = cell_index_x + 1
        showable_cell_y = cell_index_y + 1
        cell = self.__matrix[showable_cell_x][showable_cell_y]
        self.__matrix[showable_cell_x][showable_cell_y] = 1 if cell == 0 else 0

    def get_alive_cells_count(self):
        return np.count_nonzero(self.__matrix)

    def next_genetration(self):
        temp_matrix = self.__create_empty_matrix()
        for x in range(1, self.__size + 1):
            for y in range(1, self.__size + 1):
                count_neighborhood = self.__count_neighborhood(x, y)
                if (self.__matrix[x][y] == 0) and (count_neighborhood == 3):
                    temp_matrix[x][y] = 1
                elif self.__matrix[x][y] == 1 and (count_neighborhood == 3 or count_neighborhood == 2):
                    temp_matrix[x][y] = 1
                else:
                    temp_matrix[x][y] = 0
        self.__matrix = temp_matrix

    def set_random_matrix(self):
        size_with_border = self.__get_size_with_border()
        self.__matrix = np.random.randint(2, size=(size_with_border, size_with_border))
        self.__clear_border(size_with_border)

    def __clear_border(self, size_with_border):
        border_index = size_with_border - 1

        for y in range(0, border_index):
            self.__matrix[0][y] = 0
            self.__matrix[border_index][y] = 0

        for x in range(0, border_index):
            self.__matrix[x][0] = 0
            self.__matrix[x][border_index] = 0

    def __count_neighborhood(self, x, y):
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
