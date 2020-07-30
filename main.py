from tkinter import Tk
from views.conway_frame import ConwayFrame

tk = Tk()
tk.title('Pulsar - Game of Life')
conway_frame = ConwayFrame(tk)
tk.mainloop()