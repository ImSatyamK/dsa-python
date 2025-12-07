import ctypes

class ThunderList:
    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__create_list(self.size)

    def __create_list(self, size):
        return (size*ctypes.py_object)()

L = ThunderList()