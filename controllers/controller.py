from models.timer import Timer
from datetime import datetime


class Controller(object):

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__view.set_controller(self)
        self.__view.update_model(self.__model)
        self.__timer = Timer(self.tictac)

    def tictac(self):
        self.next_generation()

    def __start_play(self):
        self.__timer.start()

    def __stop_play(self):
        self.__timer.stop()

    def action(self, **event):
        name = event['name']
        if name == 'CELL_CHANGE':
            self.update_cell(event)
        elif name == 'PLAY':
            self.__start_play()
        elif name == 'STOP':
            self.__stop_play()
        else:
            pass

    def update_cell(self, event):
        self.__model.update_cell(event['cell_index_x'], event['cell_index_y'])
        self.__view.update_model(self.__model)

    def next_generation(self):
        print(datetime.now())
        self.__model.next_genetration()
        print(datetime.now())
        self.__view.update_model(self.__model)
        print(datetime.now())
        print("-----")
