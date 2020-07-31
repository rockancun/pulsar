from tkinter import Canvas

class Board(Canvas):

    def __init__(self, parent, matrix, **kargs):
        self.__matrix = matrix
        self.__zoom = 10
        super().__init__(parent, width=1, height=1, highlightthickness=0, **kargs)
        self.bind( "<Button-1>", self.paint )
        self.draw_canvas()
        self.draw_grid()


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
            self.create_line(column_to_paint, 0, column_to_paint, self.calculate_canvas_pixels(), fill="#6C7883", width=1)

    def draw_grid_axis_y(self):
       for row in range(self.get_grid_pixels()):
            cell_pixels = self.__zoom * (row+1)
            grid_pixels = row
            row_to_paint = cell_pixels + grid_pixels
            self.create_line(0, row_to_paint, self.calculate_canvas_pixels(), row_to_paint , fill="#6C7883", width=1)

    def calculate_canvas_pixels(self):
        return self.get_cell_pixels() + self.get_grid_pixels()

    def get_grid_pixels(self):
        return len(self.__matrix) - 1 

    def get_cell_pixels(self):
        return len(self.__matrix) * self.__zoom

    def register_touch_cell_observer(self, observer):
        pass

    def paint(self, event):
        python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.create_oval( x1, y1, x2, y2, fill = python_green )