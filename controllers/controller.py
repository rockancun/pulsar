class Controller(object):

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__view.set_controller(self)
        self.__view.update_model(self.__model)

    def action(self, action):
        print(action)
