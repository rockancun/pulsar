

class Controller(object):

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__view.set_controller(self)
        self.__view.update_model(self.__model)
        self._job = None
        self.__speeds = (1000, 500, 250, 125, 50, 10, 1)
        self.__current_speed = 0
        self.seconds = self.__speeds[self.__current_speed]
        self.__generation = 0

    def action(self, **event):
        name = event['name']
        if name == 'CELL_CHANGE':
            self.update_cell(event)
        elif name == 'PLAY':
            self.tictac()
        elif name == 'STOP':
            self.cancel()
        elif name == 'SPEED_UP':
            self.increments_speed()
        elif name == 'SPEED_DOWN':
            self.decrements_speed()
        else:
            pass

    def update_cell(self, event):
        self.__model.update_cell(event['cell_index_x'], event['cell_index_y'])
        self.__view.update_model(self.__model)
        self.__view.set_alive_cells(self.__model.get_alive_cells_count())

    def cancel(self):
        if self._job is not None:
            self.__view.after_cancel(self._job)
            self.reset_generation()
            self.__view.set_generation(self.__generation)
            self._job = None

    def tictac(self):
        self.next_generation()
        self._job = self.__view.after(self.seconds, self.tictac)

    def next_generation(self):
        self.__model.next_genetration()
        self.__view.update_model(self.__model)
        self.__view.set_alive_cells(self.__model.get_alive_cells_count())
        self.increments_generation()
        self.__view.set_generation(self.__generation)

    def increments_speed(self):
        if(self.__current_speed >= len(self.__speeds) - 1):
            return
        self.__current_speed = self.__current_speed + 1
        self.seconds = self.__speeds[self.__current_speed]
        self.__view.set_speed(self.__current_speed + 1)

    def decrements_speed(self):
        if(self.__current_speed <= 0):
            return
        self.__current_speed = self.__current_speed - 1
        self.seconds = self.__speeds[self.__current_speed]
        self.__view.set_speed(self.__current_speed + 1)

    def reset_generation(self):
        self.__generation = 0

    def increments_generation(self):
        self.__generation = self.__generation + 1
