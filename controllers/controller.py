from datetime import datetime


class Controller(object):

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__view.set_controller(self)
        self.__view.update_model(self.__model)
        self._job = None
        self.seconds = 100

    def action(self, **event):
        name = event['name']
        if name == 'CELL_CHANGE':
            self.update_cell(event)
        elif name == 'PLAY':
            self.tictac()
        elif name == 'STOP':
            self.cancel()
        else:
            pass

    def update_cell(self, event):
        self.__model.update_cell(event['cell_index_x'], event['cell_index_y'])
        self.__view.update_model(self.__model)

    def cancel(self):
        if self._job is not None:
            self.__view.after_cancel(self._job)
            self._job = None

    def tictac(self):
        self.next_generation()
        self._job = self.__view.after(self.seconds, self.tictac)

    def next_generation(self):
        self.__model.next_genetration()
        self.__view.update_model(self.__model)
