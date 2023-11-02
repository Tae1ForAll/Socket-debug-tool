import customtkinter as ctk
import configure

class ScrollEventList_Widgets(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTkFrame, position: configure.Position):
        super().__init__(parent, width=250, height=50, fg_color="#212121")
        self.place(x=position.x, y=position.y, relheight=1)
        self.on_focus_button: ctk.CTkButton = None
        self.event_list = [];
        self.list_event = ctk.CTkScrollableFrame(master=self, fg_color="#212121")
        self.list_event.place(x=0, y=0, relheight=1, relwidth=1)
        
    def focus_on_button(self, button):
        if (self.on_focus_button is not None):
            self.on_focus_button.configure(fg_color="#212121")
        button.configure(fg_color="#343439")
        self.on_focus_button = button;

    def addToEventList(self, text: str):
        id = str(len(self.event_list))
        button = ctk.CTkButton(self.list_event, text=text, textvariable=id, fg_color="#212121", command=lambda:self.focus_on_button(button))
        button.pack(fill="both");
        self.event_list.append(id)

    def deleteEvent(self):
        self.list_event.pack_slaves().remove(self.on_focus_button);
        self.on_focus_button.destroy();
        self.on_focus_button = None;
