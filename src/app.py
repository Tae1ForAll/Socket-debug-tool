import customtkinter as ctk
import configure as cfg
from manager.data_manager import DataManager, EnvironmentModel, EventModel

from ui_components.add_event_widgets import AddEvent_Widgets
from ui_components.connect_server_widgets import ConnectSocket_Widgets
from ui_components.environment_widgets import Environment_Widgets
from ui_components.reqres_widgets import ReqRes_Widgets
from ui_components.event_list_widgets import ScrollEventList_Widgets

import theme_config as theme

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

        # Init data
        self.data = DataManager()
        self.data.loadData()

        # Init Menu
        self.top_menu = TopPanel(parent=self)
        self.middle_panel = MainPanel(parent=self)

    def getServerURL(self):
        return self.top_menu.connect_socket_widgets.getServerURL()

    def setBTNConnectEvent(self, func):
        self.top_menu.connect_socket_widgets.setBTNConnectEvent(func)
        
    def onChoosedEnvironment(self, current_environment):
        # Sync to another environment
        self.updateCurrentEnvironment(current_environment)
        self.syncEnvironment(current_environment)
        pass

    def syncEnvironment(self, current_environment):
        self.data.current_env = current_environment
        data = self.data.getDataByName(current_environment)
        self.top_menu.connect_socket_widgets.syncServerUrl(data.server_url)
        self.middle_panel.syncEvents(data)
        pass

    def updateCurrentEnvironment(self, current_environment):
        pass

    def onClickSaveEnv(self):
        print("environment: ", self.data)
    

class TopPanel(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(parent, height=50, fg_color="#212121")
        self.place(x=0, y=0, relwidth=1)  
        self.connect_socket_widgets = ConnectSocket_Widgets(self, cfg.Position(0, 0), "#212121")
        self.environment_widgets = Environment_Widgets(parent=self, envList=parent.data.getEnvList())
        self.environment_widgets.setCallbackEnvironment(parent.onChoosedEnvironment)

class MainPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: App):
        super().__init__(parent, fg_color="#282B2E", border_width=0)
        print(parent._current_height);
        self.place(x=0, y=50, relwidth=1, relheight=0.93)
        self.my_parent = parent
        self.event_panel = EventPanel(self)
        self.emit_panel = EmitPanel(self)

    def onTypingEntryEvent(self):
        self.event_panel.syncEventName(self.emit_panel.getEntryText())
        
    def onTypingEntryRequestBody(self):
        self.event_panel.saveToEventPanel(self.emit_panel.getRequestBodyText())

    def onFocusEvent(self, button: ctk.CTkButton, event_id: str):
        text = ctk.StringVar(value=button._text)
        text.trace("w", lambda name, index,mode, var=text: self.onTypingEntryEvent())
        self.emit_panel.setEntryText(text)
        event = self.my_parent.data.getCurrentData().getEventByKey(event_id)
        self.emit_panel.setRequestBodyText(event.request_body)

    def syncEvents(self, data: EnvironmentModel):
        self.event_panel.deleteAllEvents()
        for event_id in data.events:
            event = data.getEventByKey(event_id)
            self.event_panel.addEvent(event.name, event_id);
            print(event.name)
            print(event.request_body)

class EventPanel(ctk.CTkFrame):
    def addEvent(self, text="New Event", event_id: str = None):
        self.event_list_panel.addToEventList(text, event_id)
    
    def deleteEvent(self):
        self.event_list_panel.deleteEvent();
    
    def deleteAllEvents(self):
        self.event_list_panel.deleteAllEvents();
    
    def syncEventName(self, text):
        self.event_list_panel.on_focus_button.configure(text=text)

    def saveToEventPanel(self, text):
        self.event_list_panel.getCurrentFocusEventDict()["request_body"] = text
    
    def getCurrentFocusEvent(self):
        return self.event_list_panel.getCurrentFocusEventDict()

    def __init__(self, parent: MainPanel):
        super().__init__(parent, fg_color="#282B2E", border_width=0, border_color="white")
        self.pack(padx=10, pady=0, side="left", fill="y")
        # self.on_add_event = callback
        self.add_event_widget = AddEvent_Widgets(self);
        self.add_event_widget.setCallbackAddBTN(self.addEvent)
        self.add_event_widget.setCallbackDeleteBTN(self.deleteEvent)
        self.event_list_panel = ScrollEventList_Widgets(self, cfg.Position(0, 50));
        self.event_list_panel.setOnFocusEvent(parent.onFocusEvent);

# request && response panel
class EmitPanel(ctk.CTkFrame):
    def __init__(self: ctk.CTkFrame, parent: ctk.CTk):
        super().__init__(parent, fg_color="#282B2E", border_color="red", border_width=0)
        self.place(x=210, y=0, relheight=1, relwidth=0.83)
        self.req_res_widget = ReqRes_Widgets(self)

    def setEntryText(self, text):
        self.req_res_widget.entry_event_name.configure(textvariable=text)

    def getEntryText(self):
        return self.req_res_widget.entry_event_name._textvariable.get()
    
    def setRequestBodyText(self, text):
        print("my text :", text)
        self.req_res_widget.scrollable_frame_request_body.insert("0.0", text=text)

    def getRequestBodyText(self, text):
        return self.req_res_widget.scrollable_frame_request_body.get()


