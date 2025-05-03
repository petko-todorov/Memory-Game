import customtkinter
from PIL import Image
import random


class MemoryGame(customtkinter.CTkFrame):
    def __init__(self, master, grid_size):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        self.grid_size = grid_size
        self.buttons = []
        self.revealed = []

        total_cards = grid_size * grid_size
        if grid_size == 5:
            total_cards -= 1

        num_pairs = total_cards // 2

        self.symbols = [str(i) for i in range(1, num_pairs + 1)] * 2
        # random.shuffle(self.symbols)

        self.default_image = customtkinter.CTkImage(Image.open("./images/question-sign.png"), size=(50, 50))

        self.symbol_to_image = self.load_image_mapping()

        self.back_button = customtkinter.CTkButton(
            self,
            text="Back to Menu",
            height=50,
            width=50,
            hover=False,
            command=self.return_to_menu
        )
        self.back_button.grid(row=0, column=0, pady=20)

        symbol_index = 0
        for row in range(grid_size):
            row_buttons = []
            for col in range(grid_size):
                if grid_size == 5 and row == 2 and col == 2:
                    row_buttons.append(None)
                    continue

                symbol = self.symbols[symbol_index]
                symbol_index += 1

                button = customtkinter.CTkButton(
                    self,
                    image=self.default_image,
                    text="",
                    fg_color="#607179",
                    hover_color="#546E7A",
                )
                button.configure(command=lambda b=button, s=symbol: self.reveal(b, s))
                button.grid(
                    row=row + 2,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
                row_buttons.append(button)

            self.buttons.append(row_buttons)

        for i in range(grid_size + 2):
            self.grid_rowconfigure(i, weight=1)
        for i in range(grid_size):
            self.grid_columnconfigure(i, weight=1)

    @staticmethod
    def load_image_mapping():
        image_paths = [
            "sunny.png",
            "star.png",
            "crescent-moon.png",
            "tree.png",
            "transport.png",
            "heart.png",
            "3d-house.png",
            "cloud.png",
            "wave.png",
            "mountain.png",
            "compass.png",
            "earth.png",
            "fire.png",
            "clock.png",
            "bridge.png",
            "anchor.png",
            "road.png",
            "telescope.png",
        ]

        random.shuffle(image_paths)

        mapping = {}
        for i in range(1, len(image_paths) + 1):
            mapping[str(i)] = customtkinter.CTkImage(
                Image.open(f"./images/{image_paths[i - 1]}"),
                size=(50, 50)
            )

        return mapping

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

    def return_to_menu(self):
        for row in self.buttons:
            for button in row:
                if button is not None:
                    button.destroy()

        self.buttons = []
        self.revealed = []
        self.symbols = []
        self.symbol_to_image = {}

        self.master.show_menu()
        self.destroy()
