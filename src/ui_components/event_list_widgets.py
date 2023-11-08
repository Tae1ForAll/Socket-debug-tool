import datetime
from uuid import uuid4
import customtkinter as ctk
import configure
from manager.data_manager import EventModel
import utilities.helper as helper;

class ScrollEventList_Widgets(ctk.CTkFrame):

    def __init__(self: ctk.CTkFrame, parent: ctk.CTkFrame, position: configure.Position):
        super().__init__(parent, fg_color="#212121")
        self.place(x=position.x, y=position.y, relheight=0.9, relwidth=1);
        self.on_focus_button: ctk.CTkButton = None
        self.on_focus_callback = None
        self.event_dict: dict = {};
        self.list_event = ctk.CTkScrollableFrame(master=self, fg_color="#212121")
        self.list_event.place(x=0, y=0, relheight=1, relwidth=1)

    def saveRequestParameters(self, request_body):
        event_id = self.on_focus_button.getvar()
        self.event_dict[event_id]["request_body"] = request_body
        
    def commandEventButon(self, button, event_id):
        if (self.on_focus_button is not None):
            self.on_focus_button.configure(fg_color="#212121")
        button.configure(fg_color="#343439")
        self.on_focus_button = button
        if self.on_focus_callback is not None:
            self.on_focus_callback(button, event_id)
    
    def setOnFocusEvent(self, callback):
        self.on_focus_callback = callback

    def addToEventList(self, text: str, event_id: str = None):
        if event_id is None:
            event_id = datetime.time().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        button = ctk.CTkButton(self.list_event, text=text, fg_color="#212121", command=lambda:self.commandEventButon(button, event_id))
        button.pack(fill="both")
        self.event_dict[event_id] = {"button": button, "request_body": ""}

    def deleteEvent(self):
        self.list_event.pack_slaves().remove(self.on_focus_button)
        
        if self.on_focus_button is not None:
            self.on_focus_button.destroy()
            self.on_focus_button = None

    def deleteAllEvents(self):
        for key, value in self.event_dict.items():
            button: ctk.CTkButton = value["button"]
            self.list_event.pack_slaves().remove(button)
            button.destroy();
            
        if self.on_focus_button is not None:
            self.on_focus_button.destroy()
            self.on_focus_button = None

    def getCurrentFocusEventDict(self) -> dict:
        return self.event_dict[self.on_focus_button._textvariable]