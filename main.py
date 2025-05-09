import customtkinter
from menu import Menu
from memory_game import MemoryGame

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.menu = None
        self.game = None
        self.title("Memory Game")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+400+200")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.show_menu()

    def show_menu(self):
        self.menu = Menu(self)

    def start_game(self, grid_size):
        self.menu.destroy()
        self.game = MemoryGame(self, grid_size)


app = App()
app.mainloop()
