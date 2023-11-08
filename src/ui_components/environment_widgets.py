import customtkinter as ctk
import theme_config as theme
import utilities.ui_factory as ui_factory
import configure

class Environment_Widgets(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, envList: list):
        super().__init__(parent, height=50, fg_color="#212121", bg_color="#212121")
        self.pack(side="right")

        self.callbackWhenChoosedEnvironment = None
        self.callbackSave = None

        self.environment_menu = ctk.CTkOptionMenu(
            master=self, 
            values=["no environment"],
            command=self.onClickEnvironment)
        self.environment_menu.set("no environment")
        self.environment_menu.grid(row=0, column=0, pady=10)

        self.save_button = ui_factory.buttonBorderGreen(self, "Save", configure.Size(30, 30), self.onClickSave)
        self.save_button.grid(row=0, column=1, padx=10, pady=10)

        self.updateEnvironment(envList)

    def onClickEnvironment(self, current_value):
        if self.callbackWhenChoosedEnvironment is not None:
            self.callbackWhenChoosedEnvironment(current_value)

    def setCallbackEnvironment(self, callback):
        self.callbackWhenChoosedEnvironment = callback

    def onClickSave(self):
        if self.callbackSave is not None:
            self.callbackSave()

    def setCallbackSave(self, callback):
        self.callbackSave = callback

    def updateEnvironment(self, envList: list):
        current_value = self.environment_menu._values
        for i in envList:
            current_value.append(i);
        self.environment_menu.configure(values=current_value)  
