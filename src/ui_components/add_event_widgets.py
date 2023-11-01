import customtkinter as ctk

class AddEvent_Widgets(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTkFrame):
        super().__init__(parent, width=250, height=50)
        self.place(x=0, y=0)

        self.add_button = ctk.CTkButton(
            master=self, 
            width=50, 
            text="ADD", 
            fg_color="#91e391", 
            text_color="#404040")
        self.add_button.grid(row=0, column=0, padx=0, pady=0)

        self.delete_button = ctk.CTkButton(
            master=self, 
            width=50, 
            text="DELETE", 
            fg_color="Red", 
            text_color="#404040")
        self.delete_button.grid(row=0, column=1, padx=0, pady=0)
