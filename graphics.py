from tkinter import Tk
class Window:
    def __init__(self, x , y):
        self.__root = Tk()
        self.__root.title("Tick-tack-toe")
        self.x = x
        self.y = y
        self.__is_running = False

    def make_window(self):
        self.__root
        self.__root.geometry(f"{self.x}x{self.y}")
        self.__root.mainloop()
        