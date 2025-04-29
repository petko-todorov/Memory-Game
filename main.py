import customtkinter

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Memory Game")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+400+200")

        self.buttons = []
        self.symbols = [str(i) for i in range(1, 9)] * 2
        self.revealed = []

        for row in range(4):
            row_buttons = []
            for col in range(4):
                index = row * 4 + col
                symbol = self.symbols[index]

                button = customtkinter.CTkButton(self, text="?")
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

        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def reveal(self, button, symbol):
        print(self.revealed)
        if len(self.revealed) < 2 and button not in [b for b, _ in self.revealed]:
            button.configure(text=symbol)
            self.revealed.append((button, symbol))

            if len(self.revealed) == 2:
                self.after(800, self.check_match)

    def check_match(self):
        b1, s1 = self.revealed[0]
        b2, s2 = self.revealed[1]

        if s1 != s2:
            b1.configure(text="?")
            b2.configure(text="?")
        else:
            b1.configure(state="disabled")
            b2.configure(state="disabled")

        self.revealed.clear()


app = App()
app.mainloop()
