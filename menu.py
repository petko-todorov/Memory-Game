import customtkinter


class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Memory Game",
            font=("Helvetica Neue", 30, "bold")
        )
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=5,
            pady=(40, 10)
        )

        self.subtitle_label = customtkinter.CTkLabel(
            self,
            text="Select Grid Size",
            font=("Helvetica Neue", 20)
        )
        self.subtitle_label.grid(
            row=1,
            column=0,
            columnspan=5,
        )

        self.button_4x4 = customtkinter.CTkButton(
            self,
            text="4x4",
            width=120,
            height=60,
            font=("Arial", 20),
            fg_color="#3C8C40",
            hover_color="#367E39",
            command=lambda: self.selected_type(self.button_4x4)
        )
        self.button_4x4.grid(row=2, column=1, padx=20, pady=0)

        self.button_5x5 = customtkinter.CTkButton(
            self,
            text="5x5",
            width=120,
            height=60,
            fg_color="#B76C00",
            hover_color="#925600",
            font=("Arial", 20),
            command=lambda: self.selected_type(self.button_5x5)
        )
        self.button_5x5.grid(row=2, column=2, padx=20, pady=0)

        self.button_6x6 = customtkinter.CTkButton(
            self,
            text="6x6",
            width=120,
            height=60,
            fg_color="#D32F2F",
            hover_color="#A82525",
            font=("Arial", 20),
            command=lambda: self.selected_type(self.button_6x6)
        )
        self.button_6x6.grid(row=2, column=3, padx=20, pady=20)

        for col in range(5):
            self.grid_columnconfigure(col, weight=1)
        for row in range(10):
            self.grid_rowconfigure(row, weight=1)

        self.start_button = customtkinter.CTkButton(
            self,
            text="Start Game",
            width=120,
            height=60,
            font=("Arial", 20),
            command=lambda: master.start_game(self.number)
        )
        self.number = None

    def selected_type(self, button):
        self.button_4x4.configure(text="4x4", state="normal")
        self.button_5x5.configure(text="5x5", state="normal")
        self.button_6x6.configure(text="6x6", state="normal")

        self.number = int(button.cget("text")[:1])

        button.configure(
            text="Selected",
            text_color_disabled="white",
            state="disabled",
        )

        selected_grid_info = customtkinter.CTkLabel(
            self,
            text=f"Grid Size {self.number}x{self.number}",
            font=("Helvetica Neue", 22)
        )
        selected_grid_info.grid(row=3, column=2)
        self.start_button.grid(row=4, column=2)
