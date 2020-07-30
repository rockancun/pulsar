from tkinter import Tk
from views.conway_frame import ConwayFrame

tk = Tk()
tk.title('Pulsar - Game of Life')
tk.config(bg="#0E1621")
conway_frame = ConwayFrame(tk)
tk.mainloop()