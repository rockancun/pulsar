from views.conway_frame import ConwayFrame
from controllers.controller import Controller
from models.matrix import Matrix
from tkinter import Tk


tk = Tk()
tk.title('Pulsar - Game of Life')
view = ConwayFrame(tk)
model = Matrix(10)
controller = Controller(view, model)
tk.mainloop()
