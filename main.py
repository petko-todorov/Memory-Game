import customtkinter
from PIL import Image
import random

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Memory Game")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+400+200")
        self.resizable(False, False)

        self.buttons = []
        self.symbols = [str(i) for i in range(1, 9)] * 2
        random.shuffle(self.symbols)

        self.default_image = customtkinter.CTkImage(Image.open("./images/question-sign.png"), size=(50, 50))

        self.symbol_to_image = {
            "1": customtkinter.CTkImage(Image.open("./images/sunny.png"), size=(50, 50)),
            "2": customtkinter.CTkImage(Image.open("./images/star.png"), size=(50, 50)),
            "3": customtkinter.CTkImage(Image.open("./images/crescent-moon.png"), size=(50, 50)),
            "4": customtkinter.CTkImage(Image.open("./images/tree.png"), size=(50, 50)),
            "5": customtkinter.CTkImage(Image.open("./images/transport.png"), size=(50, 50)),
            "6": customtkinter.CTkImage(Image.open("./images/heart.png"), size=(50, 50)),
            "7": customtkinter.CTkImage(Image.open("./images/3d-house.png"), size=(50, 50)),
            "8": customtkinter.CTkImage(Image.open("./images/cloud.png"), size=(50, 50)),
        }
        self.revealed = []

        for row in range(1, 5):
            row_buttons = []
            for col in range(4):
                index = (row - 1) * 4 + col
                symbol = self.symbols[index]

                button = customtkinter.CTkButton(self, image=self.default_image, text="")
                button.configure(command=lambda b=button, s=symbol: self.reveal(b, s))
                button.grid(
                    row=row,
                    column=col,
                    padx=10,
                    pady=10,
                    sticky="nsew"
                )
                row_buttons.append(button)

            self.buttons.append(row_buttons)

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def reveal(self, button, symbol):
        if len(self.revealed) < 2 and button not in [b for b, _ in self.revealed]:
            button.configure(image=self.symbol_to_image[symbol], text="")
            self.revealed.append((button, symbol))

            if len(self.revealed) == 2:
                self.after(800, self.check_match)

    def check_match(self):
        b1, s1 = self.revealed[0]
        b2, s2 = self.revealed[1]

        if s1 != s2:
            b1.configure(image=self.default_image)
            b2.configure(image=self.default_image)
        else:
            b1.configure(state="disabled")
            b2.configure(state="disabled")

        self.revealed.clear()


app = App()
app.mainloop()
