import customtkinter
from PIL import Image
import random
import json


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
        random.shuffle(self.symbols)

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
        self.back_button.place(relx=0.01, rely=0.01)

        self.moves = 0
        self.moves_label = customtkinter.CTkLabel(
            self,
            text=f"Moves: {self.moves}",
            font=("Helvetica Neue", 20)
        )
        self.moves_label.place(relx=0.5, rely=0.05, anchor="center")

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

        self.matched_pairs = 0
        self.best_score = json.load(open("highscore.json"))
        self.best_score_label = customtkinter.CTkLabel(
            self,
            text=f"Best moves: {self.best_score[f'{grid_size}x{grid_size}']}",
            font=("Helvetica Neue", 20)
        )
        self.best_score_label.place(relx=0.88, rely=0.05, anchor="center")

        self.old_record = self.best_score[f"{grid_size}x{grid_size}"]

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
            self.flash(b1, b2)
            b1.configure(state="disabled")
            b2.configure(state="disabled")
            self.matched_pairs += 1

        self.revealed.clear()
        self.moves += 1
        self.moves_label.configure(text=f"Moves: {self.moves}")

        if self.matched_pairs == self.calculate_total_pairs():
            with open("highscore.json", "w") as f:
                if self.moves < self.best_score[f"{self.grid_size}x{self.grid_size}"]:
                    self.best_score[f"{self.grid_size}x{self.grid_size}"] = self.moves
                    json.dump(self.best_score, indent=4, fp=f)
                    self.best_score_label.configure(text=f"Best moves: {self.moves}")
                else:
                    json.dump(self.best_score, indent=4, fp=f)

            self.after(1000, self.end_game_effect)

    def flash(self, btn1, btn2, count=0):
        colors = ["green", "#607179"]
        if count < 4:
            new_color = colors[count % len(colors)]
            btn1.configure(fg_color=new_color)
            btn2.configure(fg_color=new_color)
            btn1.after(200, lambda: self.flash(btn1, btn2, count + 1))

    def calculate_total_pairs(self):
        total_cells = self.grid_size * self.grid_size
        if self.grid_size == 5:
            total_cells -= 1
        return total_cells // 2

    def end_game_effect(self):
        order = []
        rows = len(self.buttons)
        cols = len(self.buttons[0]) if rows > 0 else 0
        layers = (min(rows, cols) + 1) // 2

        for layer in range(layers):
            top = layer
            bottom = rows - 1 - layer
            left = layer
            right = cols - 1 - layer

            order.extend((top, c) for c in range(left, right + 1))
            order.extend((r, right) for r in range(top + 1, bottom + 1))
            if bottom > top:
                order.extend((bottom, c) for c in range(right - 1, left - 1, -1))
            if left < right:
                order.extend((r, left) for r in range(bottom - 1, top, -1))

        valid_coords = [(r, c) for r in range(rows) for c in range(cols) if self.buttons[r][c] is not None]
        order = [coord for coord in order if coord in valid_coords]

        def process_spiral(index=0):
            if index < len(order):
                r, c = order[index]
                self.buttons[r][c].configure(fg_color="#6296C0")
                self.after(100, lambda: process_spiral(index + 1))
            else:
                end_game_label = customtkinter.CTkLabel(
                    self,
                    text="You did it!",
                    font=customtkinter.CTkFont(size=60, weight="bold"),
                    text_color="#91b5d2",
                    width=500,
                    height=100,
                )
                end_game_label.place(relx=0.5, rely=0.54, anchor="center")

                record_label = customtkinter.CTkLabel(
                    self,
                    text=f"New record! {self.moves} moves",
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                    text_color="#91b5d2",
                    width=500,
                    height=50,
                )

                if self.moves < self.old_record:
                    record_label.place(relx=0.5, rely=0.64, anchor="center")

                if self.moves == self.old_record:
                    record_label.configure(text=f"Tied record! {self.moves} moves")
                    record_label.place(relx=0.5, rely=0.64, anchor="center")

                restart_button = customtkinter.CTkButton(
                    self,
                    text="Restart",
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                    height=50,
                    width=70,
                    hover=False,
                    command=lambda: MemoryGame(self.master, self.grid_size)
                )
                restart_button.place(relx=0.15, rely=0.01)

        process_spiral()

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
