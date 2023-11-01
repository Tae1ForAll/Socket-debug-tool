import customtkinter as ctk

class ScrollEventPanel_Widgets(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTkFrame):
        super().__init__(parent, width=250, height=50)
        self.place(x=0, y=0)
