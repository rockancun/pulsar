from tkinter import Canvas


class Board(Canvas):

    def __init__(self, parent, **kargs):
        self.__matrix = [[0 for x in range(0)] for y in range(0)]

        self.__zoom = 10
        self.__observer = None
        super().__init__(parent, width=1, height=1,
                         highlightthickness=0, **kargs)
        self.bind("<Button-1>", self.paint)
        self.draw_canvas()
        self.draw_grid()
        self.print_cells()

    def update_matrix(self, matrix):
        self.__matrix = matrix
        self.draw_canvas()
        self.draw_grid()
        self.print_cells()

    def print_cells(self):
        matrix_size = self.matrix_size()
        for column in range(matrix_size):
            for row in range(matrix_size):
                self.print_live_or_dead_cell(column, row)

    def print_live_or_dead_cell(self, column, row):

        if self.__matrix[column][row] == 0:
            self.print_dead_cell(column, row)
            return
        self.print_live_cell(column, row)

    def print_live_cell(self, x, y):
        self.print_cell(x, y, '#2B5278')

    def print_dead_cell(self, x, y):
        self.print_cell(x, y, '#242F3D')

    def print_cell(self, x, y, color='black'):
        origin_x = x * self.__zoom + x
        origin_y = y * self.__zoom + y
        destiny_x = origin_x + self.__zoom - 1
        destiny_y = origin_y + self.__zoom - 1
        self.create_rectangle(origin_x, origin_y, destiny_x,
                              destiny_y, fill=color, width=0)

    def draw_canvas(self):
        canvas_size = self.calculate_canvas_pixels()
        self.config(width=canvas_size, height=canvas_size)

    def draw_grid(self):
        self.draw_grid_axis_x()
        self.draw_grid_axis_y()

    def draw_grid_axis_x(self):
        for column in range(self.get_grid_pixels()):
            cell_pixels = self.__zoom * (column+1)
            grid_pixels = column
            column_to_paint = cell_pixels + grid_pixels
            height_zero = 0
            self.create_line(
                column_to_paint,
                height_zero,
                column_to_paint,
                self.calculate_canvas_pixels(),
                fill="#6C7883",
                width=1)

    def draw_grid_axis_y(self):
        for row in range(self.get_grid_pixels()):
            cell_pixels = self.__zoom * (row+1)
            grid_pixels = row
            row_to_paint = cell_pixels + grid_pixels
            position_zero = 0
            self.create_line(
                position_zero,
                row_to_paint,
                self.calculate_canvas_pixels(),
                row_to_paint,
                fill="#6C7883",
                width=1)

    def calculate_canvas_pixels(self):
        return self.get_cell_pixels() + self.get_grid_pixels()

    def get_grid_pixels(self):
        return self.matrix_size() - 1

    def get_cell_pixels(self):
        return self.matrix_size() * self.__zoom

    def register_touch_cell_observer(self, observer):
        self.__observer = observer

    def paint(self, event):
        x, y = (event.x - 1), (event.y - 1)

        cell_index_x = self.calculate_cell_index(x)
        cell_index_y = self.calculate_cell_index(y)

        if(self.__observer):
            self.__observer(cell_index_x, cell_index_y)

    def calculate_cell_index(self, pixel):
        grid_pixels_to_discount = pixel // (self.__zoom + 1)
        pixels_without_grid_pixel = pixel - grid_pixels_to_discount
        return pixels_without_grid_pixel // self.__zoom

    def matrix_size(self):
        return len(self.__matrix)
