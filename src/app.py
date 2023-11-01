import customtkinter as ctk
import configure as cfg

from ui_components.add_event_widgets import AddEvent_Widgets
from ui_components.connect_server_widgets import ConnectSocket_Widgets
from ui_components.environment_widgets import Environment_Widgets

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
        super().__init__(parent, height=50, fg_color="Orange", bg_color="Orange")
        self.place(x=0, y=0, relwidth=1)
        
        self.connect_socket_widgets = ConnectSocket_Widgets(self, cfg.Position(0, 0))
        self.environment_widgets = Environment_Widgets(parent=self)


class MainPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTkFrame):
        super().__init__(parent, height=50, fg_color="White", bg_color="White")
        self.place(x=0, y=50, relwidth=1, relheight=1)

        self.event_panel = EventPanel(self)
        self.emit_panel = EmitPanel(self)

class EventPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTk):
        super().__init__(parent, width=250, fg_color="Gray", bg_color="White")
        self.place(x=0, y=0, relheight=1)
        self.add_event_widget = AddEvent_Widgets(self);

        # scrollable_frame_event = ctk.CTkScrollableFrame(self, width=500)
        # scrollable_frame_event.place(x=10, y=50, relheight=1)

class EmitPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTk):
        super().__init__(parent, width=200, fg_color="Gray", bg_color="White")
        self.place(x=260, y=0, relheight=1, relwidth=1)

