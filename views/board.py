from tkinter import Canvas

class Board(Canvas):

    def __init__(self, parent, data, **kargs):
        super().__init__(parent, width=data['width'], height=data['height'])
        self.bind( "<Button-1>", self.paint )

    def register_touch_cell_observer(self, observer):
        pass

    def paint(self, event):
        python_green = "#476042"
        x1 = event.x - 1 
        y1 = event.y - 1
        x2 = event.x + 1
        y2 = event.y + 1
        self.create_oval( x1, y1, x2, y2, fill = python_green )