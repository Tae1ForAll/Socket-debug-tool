import customtkinter as ctk
import configure as cfg

from ui_components.add_event_widgets import AddEvent_Widgets
from ui_components.connect_server_widgets import ConnectSocket_Widgets
from ui_components.environment_widgets import Environment_Widgets

import theme_config as theme
from ui_components.event_list_widgets import ScrollEventList_Widgets

class App(ctk.CTk):    
    def __init__(
            self: ctk.CTk, 
            title, 
            bg_color: str, 
            min_size: cfg.Size | None, 
            max_size: cfg.Size | None):
        
        super().__init__()

        # Init Configurations
        self.wm_title(title)
        if min_size is not None:
            self.minsize(min_size.width, min_size.height)
        if max_size is not None:
            self.maxsize(max_size.width, max_size.height)
        self.configure(bg=bg_color)

        # Init Menu
        self.top_menu = TopPanel(parent=self)
        self.middle_panel = MainPanel(parent=self)

    def getServerURL(self):
        return self.top_menu.connect_socket_widgets.getServerURL()

    def setBTNConnectEvent(self, func):
        self.top_menu.connect_socket_widgets.setBTNConnectEvent(func)
    

class TopPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTk):
        super().__init__(parent, height=50, fg_color="#212121")
        self.place(x=0, y=0, relwidth=1)
        
        self.connect_socket_widgets = ConnectSocket_Widgets(self, cfg.Position(0, 0), "#212121")
        self.environment_widgets = Environment_Widgets(parent=self)


class MainPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTkFrame):
        super().__init__(parent, height=50, fg_color="#282B2E")
        self.place(x=0, y=50, relwidth=1, relheight=1)

        self.event_panel = EventPanel(self)
        self.emit_panel = EmitPanel(self)

    # def onAddEvent(event: str):
        

class EventPanel(ctk.CTkFrame):
    def addEvent(self):
        self.event_list_panel.addToEventList("New Event")
        # self.on_add_event("New Event")
    
    def deleteEvent(self):
        self.event_list_panel.deleteEvent();

    def __init__(self, parent: ctk.CTk):
        super().__init__(parent, width=250)
        self.place(x=10, y=0, relheight=0.9)

        # self.on_add_event = callback
        self.add_event_widget = AddEvent_Widgets(self);
        self.add_event_widget.setCallbackAddBTN(self.addEvent)
        self.add_event_widget.setCallbackDeleteBTN(self.deleteEvent)
        self.event_list_panel = ScrollEventList_Widgets(self, cfg.Position(0, 30));

class EmitPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTk):
        super().__init__(parent, width=200, fg_color="#343439")
        self.place(x=260, y=0, relheight=1, relwidth=1)

