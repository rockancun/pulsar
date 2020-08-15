import tkinter
from tkinter import Canvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.cm as cm
import numpy as np


class Board(Canvas):

    def __init__(self, parent, **kargs):
        size = 10
        self.__matrix = np.random.randint(2, size=(size, size))
        self.__parent = parent
        super().__init__(parent, width=1, height=1,
                         highlightthickness=0, **kargs)
        fig = Figure()
        plot = fig.add_subplot(111)

        plot.imshow(self.__matrix, interpolation='nearest', cmap='winter')

        self.__canvas = FigureCanvasTkAgg(fig, master=parent)
        self.__canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.__canvas.draw()

    def register_touch_cell_observer(self, observer):
        self.__observer = observer

    def onclick(self, event):
        if (event.ydata is not None) and (event.xdata is not None):
            cell_index_x = int(event.ydata + 0.5)
            cell_index_y = int(event.xdata + 0.5)

            if(self.__observer):
                self.__observer(cell_index_x, cell_index_y)

    def update_matrix(self, matrix):
        self.__matrix = matrix
        fig = Figure()
        plot = fig.add_subplot(111)
        plot.imshow(self.__matrix, interpolation='nearest', cmap='winter')
        self.__canvas.figure = fig
        self.__canvas.draw()
