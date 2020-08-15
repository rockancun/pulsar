from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from views.plot_board import Board
from tkinter.constants import BOTH, BOTTOM, X, LEFT, CENTER, TRUE


class ConwayFrame(Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#0E1621")
        self.initialize()

    def initialize(self):
        canvas_frame = self.create_canvas_frame()
        info_frame = self.create_info_frame()
        action_frame = self.create_actions_frame()

        canvas_frame.pack(fill=X, expand=TRUE)
        action_frame.pack(fill=X, side=BOTTOM)
        info_frame.pack(fill=X, side=BOTTOM)

        self.pack(fill=BOTH, expand=TRUE)

    def create_canvas_frame(self):
        canvas_frame = Frame(self, bg="#0E1621")

        self.__board = Board(canvas_frame, bg="#242F3D")
        self.__board.register_touch_cell_observer(self.touch_event_hadler)
        self.__board.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__board.pack()
        return canvas_frame

    def touch_event_hadler(self, cell_index_x, cell_index_y):
        self.action(name="CELL_CHANGE", cell_index_x=cell_index_x,
                    cell_index_y=cell_index_y)

    def update_model(self, model):
        self.__model = model
        self.__board.update_matrix(self.__model.get_matrix())

    def set_controller(self, controller):
        self.__controller = controller

    def action(self, **event):
        self.__controller.action(**event)

    def create_info_frame(self):
        info_frame = Frame(self, bg="#17212B")

        center_frame = Frame(info_frame, bg="#17212B")

        generation_label = Label(
            center_frame,
            bg="#17212B",
            fg="white",
            text='Generation:')

        life_death_label = Label(
            center_frame,
            bg="#17212B",
            fg="white",
            text='Live: 0 - Dead: 0')

        speed_label = Label(
            center_frame,
            bg="#17212B",
            fg="white",
            text='Speed: 1x')

        generation_label.grid(row=0, column=0, padx=10, pady=10)
        life_death_label.grid(row=0, column=1, padx=10, pady=10)
        speed_label.grid(row=0, column=2, padx=10, pady=10)

        center_frame.pack()

        return info_frame

    def create_actions_frame(self):
        frame = Frame(self, bg="#17212B")

        actions_secondary_frame = self.create_secondary_actions_frame(frame)
        actions_secondary_frame.pack(side=LEFT)

        actions_primary_frame = self.create_primary_actions_frame(frame)
        actions_primary_frame.pack()

        return frame

    def create_secondary_actions_frame(self, parent_frame):
        frame = Frame(parent_frame, bg="#17212B")

        random_button = self.create_random_button(frame)
        grid_button = self.create_grid_button(frame)
        photo_button = self.create_photo_button(frame)

        random_button.grid(row=0, column=1, padx=10, pady=10)
        grid_button.grid(row=0, column=2, padx=10, pady=10)
        photo_button.grid(row=0, column=3, padx=10, pady=10)

        return frame

    def create_random_button(self, parent):
        image = PhotoImage(file="resources/random.png")
        button = Button(
            parent,
            text="Random",
            image=image,
            fg="#6C7883",
            command=lambda: self.action(name='RANDOM'))
        button.image = image
        return button

    def create_grid_button(self, parent):
        image = PhotoImage(file="resources/grid.png")
        grid_button = Button(
            parent,
            text="Grid",
            image=image,
            fg="#6C7883",
            command=lambda: self.action(name='SHOW_GRID'))
        grid_button.image = image
        return grid_button

    def create_photo_button(self, parent):
        photo = PhotoImage(file="resources/photo.png")
        button = Button(
            parent,
            text="Photo",
            image=photo,
            fg="#6C7883",
            command=lambda: self.action(name='PHOTO'))
        button.image = photo
        return button

    def create_primary_actions_frame(self, parent_frame):
        frame = Frame(parent_frame, bg="#17212B")
        stop_button = self.create_stop_button(frame)
        speed_up_button = self.create_speed_button_up(frame)
        play_button = self.create_play_button(frame)
        speed_down_button = self.create_speed_down_button(frame)

        stop_button.grid(row=0, column=1, padx=10, pady=10)
        speed_up_button.grid(row=0, column=2, padx=10, pady=10)
        play_button.grid(row=0, column=3, padx=10, pady=10)
        speed_down_button.grid(row=0, column=4, padx=10, pady=10)

        return frame

    def create_stop_button(self, parent_frame):
        photo = PhotoImage(file="resources/stop.png")
        button = Button(parent_frame,
                        text="Stop",
                        image=photo,
                        fg="#6C7883",
                        command=lambda: self.action(name='STOP'))
        button.image = photo
        return button

    def create_speed_button_up(self, parent_frame):
        photo = PhotoImage(file="resources/speed_up.png")
        button = Button(parent_frame,
                        text="Speed Up",
                        image=photo,
                        fg="#6C7883",
                        command=lambda: self.action(name='SPEED_UP'))
        button.image = photo
        return button

    def create_play_button(self, parent_frame):
        photo = PhotoImage(file="resources/play.png")
        button = Button(parent_frame,
                        text="Play",
                        image=photo,
                        fg="#6C7883",
                        command=lambda: self.action(name='PLAY'))
        button.image = photo
        return button

    def create_speed_down_button(self, parent):
        photo = PhotoImage(file="resources/speed_down.png")
        button = Button(parent,
                        text="Speed Down",
                        image=photo,
                        fg="#6C7883",
                        command=lambda: self.action(name='SPEED_DOWN'))
        button.image = photo
        return button
