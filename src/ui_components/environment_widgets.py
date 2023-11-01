import customtkinter as ctk

class Environment_Widgets(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTk):
        super().__init__(parent, height=50, fg_color="Orange", bg_color="Orange")
        self.pack(side="right")

        self.environment_menu = ctk.CTkOptionMenu(master=self, values=["no environment", "option 2"])
        self.environment_menu.set("no environment")
        self.environment_menu.grid(row=0, column=0, pady=10)

        self.save_button = ctk.CTkButton(
            master=self, 
            width=50, 
            text="SAVE", 
            fg_color="#91e391", 
            text_color="#404040")
        self.save_button.grid(row=0, column=1, padx=10, pady=10)