from tkinter import Tk
import tkinter.font as font
import tkinter as tk

class Window:
    def __init__(self, x , y):
        self.__root = Tk()
        self.__root.title("Tick-tack-toe Game")
        self.x = x # Set the window width
        self.y = y  # Set the window height
        
    def get_root(self):
        return self.__root

    def make_window(self):
        self.__root
        self.__root.geometry(f"{self.x}x{self.y}")
        self.__root.eval('tk::PlaceWindow . center')
        self.__root.mainloop()

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", font_size= 12,**kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.font = font.Font(size=font_size)
        self.config(font=self.font)
        self.insert(0, self.placeholder)
        self.config(fg="gray")
        self.bind("<FocusIn>", self.remove_placeholder)
        self.bind("<FocusOut>", self.add_placeholder)


    def remove_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg="black")

    def add_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg="gray")

class CustomButton(tk.Button):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        self.config(bg="lightblue", fg="black", font=("Arial", 12))
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        self.config(bg="lightgreen")

    def on_leave(self, event):
        self.config(bg="lightblue")