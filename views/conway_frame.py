from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter.constants import BOTH, BOTTOM, X, LEFT

class ConwayFrame(Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.initialize()

    def initialize(self):
        canvas_frame = self.create_canvas_frame()
        info_frame = self.create_info_frame()
        action_frame = self.create_actions_frame()

        canvas_frame.pack(fill=BOTH, expand=True)
        action_frame.pack(fill=X, side=BOTTOM)
        info_frame.pack(fill=X, side=BOTTOM )
        
        self.pack(fill=BOTH, expand=True)

    def create_canvas_frame(self):
        canvas_frame = Frame(self, bg="red")
        return canvas_frame

    def create_info_frame(self):
        info_frame = Frame(self, bg="#17212B")

        center_frame = Frame(info_frame, bg="#17212B")

        generation_label = Label(center_frame, bg="#17212B", fg="white", text='Generation:',)
        life_death_label = Label(center_frame, bg="#17212B", fg="white", text='Live: 0 - Dead: 0')
        speed_label = Label(center_frame, bg="#17212B", fg="white", text='Speed: 1x')

        generation_label.grid(row=0, column=0, padx=10, pady=10)
        life_death_label.grid(row=0, column=1, padx=10, pady=10)
        speed_label.grid(row=0, column=2, padx=10, pady=10)

        center_frame.pack()

        return info_frame

    def create_actions_frame(self):
        actions_frame = Frame(self, bg="#17212B")

        actions_secondary_frame = self.create_secondary_actions_frame(actions_frame)
        actions_secondary_frame.pack(side = LEFT)

        actions_primary_frame = self.create_primary_actions_frame(actions_frame)
        actions_primary_frame.pack()

        return actions_frame

    def create_secondary_actions_frame(self, parent_frame):
        secondary_actions_frame = Frame(parent_frame, bg="#17212B")
        
        random_button = Button(secondary_actions_frame, text="Random", bg="#17212B", fg="#6C7883", command=self.action)
        grid_button = Button(secondary_actions_frame, text="Grid", bg="#17212B", fg="#6C7883", command=self.action)
        photo_button = Button(secondary_actions_frame, text="Photo", bg="#17212B", fg="#6C7883", command=self.action)

        random_button.grid(row=0, column=1, padx=10, pady=10)
        grid_button.grid(row=0, column=2, padx=10, pady=10)
        photo_button.grid(row=0, column=3, padx=10, pady=10)

        return secondary_actions_frame

    def create_primary_actions_frame(self, parent_frame):
        primary_actions= Frame(parent_frame, bg="#17212B")

        stop_button = Button(primary_actions, text="Stop", bg="#17212B", fg="#6C7883", command=self.action)
        speed_up_button = Button(primary_actions, text="Speed Up", bg="#17212B", fg="#6C7883", command=self.action)
        play_button = Button(primary_actions, text="Play", bg="#17212B", fg="#6C7883", command=self.action)
        speed_down = Button(primary_actions, text="Speed Down", bg="#17212B", fg="#6C7883", command=self.action)


        stop_button.grid(row=0, column=1, padx=10, pady=10)
        speed_up_button.grid(row=0, column=2, padx=10, pady=10 )
        play_button.grid(row=0, column=3, padx=10, pady=10 )
        speed_down.grid(row=0, column=4, padx=10, pady=10 )

        return primary_actions

    def action(self):
        pass