import customtkinter as ctk
import theme_config as theme
import utilities.ui_factory as ui_factory
import configure

class AddEvent_Widgets(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame):
        super().__init__(parent, width=250, height=50, border_color="white")
        self.place(x=0, y=10)

        self.add_button = ui_factory.buttonBorderGreen(master=self, text="Add", size=configure.Size(30, 30), callback=None);
        self.add_button.grid(row=0, column=0, padx=0, pady=0)

        self.delete_button = ui_factory.buttonBorderRed(master=self, text="Delete", size=configure.Size(50, 30), callback=None)
        self.delete_button.grid(row=0, column=1, padx=0, pady=0)


    def setCallbackAddBTN(self, callback):
        self.add_button._command = callback
    
    def setCallbackDeleteBTN(self, callback):
        self.delete_button._command = callback