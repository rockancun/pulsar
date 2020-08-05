class Controller(object):

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__view.set_controller(self)
        self.__view.update_model(self.__model)

    def action(self, **event):
        name = event['name']
        if name == 'CELL_CHANGE':
            self.update_cell(event)
        elif name == 'PLAY':
            self.next_generation()
        else:
            pass

    def update_cell(self, event):
        self.__model.update_cell(event['cell_index_x'], event['cell_index_y'])
        self.__view.update_model(self.__model)

    def next_generation(self):
        self.__model.next_genetration()
        self.__view.update_model(self.__model)
