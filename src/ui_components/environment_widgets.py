import customtkinter as ctk
import theme_config as theme
import utilities.ui_factory as ui_factory
import configure

class Environment_Widgets(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk):
        super().__init__(parent, height=50, fg_color="#212121", bg_color="#212121")
        self.pack(side="right")

        self.environment_menu = ctk.CTkOptionMenu(
            master=self, 
            values=["no environment", "option 2"])
        self.environment_menu.set("no environment")
        self.environment_menu.grid(row=0, column=0, pady=10)

        self.save_button = ui_factory.buttonBorderGreen(self, "Save", configure.Size(30, 30), None)
        self.save_button.grid(row=0, column=1, padx=10, pady=10)