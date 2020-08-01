from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from views.board import Board
from tkinter.constants import BOTH, BOTTOM, X, LEFT, CENTER, TRUE
from random import randrange

class ConwayFrame(Frame):
    
    def __init__(self, parent):
        super().__init__(parent, bg="#0E1621")
        self.__matrix = [[(randrange(0, 2)) for x in range(100)] for y in range(100)]

        self.initialize()

    def initialize(self):
        canvas_frame = self.create_canvas_frame()
        info_frame = self.create_info_frame()
        action_frame = self.create_actions_frame()

        canvas_frame.pack(fill=X, expand=TRUE)
        action_frame.pack(fill=X, side=BOTTOM)
        info_frame.pack(fill=X, side=BOTTOM )
        
        self.pack(fill=BOTH, expand=TRUE)

    def create_canvas_frame(self):
        canvas_frame = Frame(self, bg="#0E1621")
        
        self.__board = Board(canvas_frame, self.__matrix, bg="#242F3D")
        self.__board.register_touch_cell_observer(self.touch_event_hadler)
        self.__board.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__board.pack()
        return canvas_frame

    def touch_event_hadler(self, cell_index_x, cell_index_y):
        self.__matrix[cell_index_x][cell_index_y] = 1 if self.__matrix[cell_index_x][cell_index_y] == 0 else 0
        self.__board.update_matrix(self.__matrix)

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
        
        photo_random = PhotoImage(file="resources/random.png")
        random_button = Button(secondary_actions_frame, text="Random", image=photo_random, fg="#6C7883", command=self.action)
        random_button.image = photo_random

        photo_grid = PhotoImage(file="resources/grid.png")
        grid_button = Button(secondary_actions_frame, text="Grid", image=photo_grid, fg="#6C7883", command=self.action)
        grid_button.image = photo_grid

        photo_photo = PhotoImage(file="resources/photo.png")
        photo_button = Button(secondary_actions_frame, text="Photo", image=photo_photo, fg="#6C7883", command=self.action)
        photo_button.image = photo_photo

        random_button.grid(row=0, column=1, padx=10, pady=10)
        grid_button.grid(row=0, column=2, padx=10, pady=10)
        photo_button.grid(row=0, column=3, padx=10, pady=10)

        return secondary_actions_frame

    def create_primary_actions_frame(self, parent_frame):
        primary_actions= Frame(parent_frame, bg="#17212B")

        photo_stop = PhotoImage(file="resources/stop.png")
        stop_button = Button(primary_actions, text="Stop", image=photo_stop, fg="#6C7883", command=self.action)
        stop_button.image = photo_stop

        photo_speed_up = PhotoImage(file="resources/speed_up.png")
        speed_up_button = Button(primary_actions, text="Speed Up", image=photo_speed_up, fg="#6C7883", command=self.action)
        speed_up_button.image = photo_speed_up

        photo_play = PhotoImage(file="resources/play.png")
        play_button = Button(primary_actions, text="Play", image=photo_play, fg="#6C7883", command=self.action)
        play_button.image = photo_play

        photo_speed_down = PhotoImage(file="resources/speed_down.png")
        speed_down = Button(primary_actions, text="Speed Down", image=photo_speed_down, fg="#6C7883", command=self.action)
        speed_down.image = photo_speed_down


        stop_button.grid(row=0, column=1, padx=10, pady=10)
        speed_up_button.grid(row=0, column=2, padx=10, pady=10 )
        play_button.grid(row=0, column=3, padx=10, pady=10 )
        speed_down.grid(row=0, column=4, padx=10, pady=10 )

        return primary_actions

    def action(self):
        pass