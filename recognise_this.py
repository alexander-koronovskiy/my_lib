class Window(object):
    """Класс окно"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wdsqare = self.width * self.height

    def info(self):
        print('You have window {}x{}'.format(self.width, self.height))


class Room(object):
    """Класс комната"""
    window_list = []

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_window(self, window):
        self.window_list.append(window)

    def show_window_list(self):
        print('In this room:')
        for window in self.window_list:
            window.info()


if __name__ == "__main__":
    room = Room(10, 9, 8)
    window1 = Window(2, 1)
    room.add_window(window1)
    window2 = Window(2, 2)
    room.add_window(window2)
    window3 = Window(2, 3)
    room.add_window(window3)
    window4 = Window(2, 4)
    room.add_window(window4)
    room.show_window_list()
