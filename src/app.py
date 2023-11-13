from tkinter import PhotoImage
import customtkinter as ctk
import configure as cfg
from manager.data_manager import DataManager, EnvironmentModel, EventModel
from PIL import ImageTk, Image

from ui_components.add_event_widgets import AddEvent_Widgets
from ui_components.connect_server_widgets import ConnectSocket_Widgets
from ui_components.environment_widgets import Environment_Widgets
from ui_components.reqres_widgets import ReqRes_Widgets
from ui_components.event_list_widgets import ScrollEventList_Widgets

import theme_config as theme
import utilities.ui_factory as ui_factory

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
        # im = Image.open("D:\work\site-project\Socket-debug-tool\src\icon\jarn_daeng_edit.png")
        # photo = ImageTk.PhotoImage(im)
        # self.wm_iconphoto(True, photo)

        self.popup = None
        self.environment_name_popup = None

        # Init data
        self.data = DataManager()
        self.data.loadData()

        # Init Menu
        self.top_menu = TopPanel(parent=self)
        self.middle_panel = MainPanel(parent=self)
        self.top_menu.environment_widgets.setCallbackSave(self.onClickSaveEnv);

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

    def updateCurrentEnvironment(self, current_environment):
        pass

    
    def onClickSaveEnv(self):
        obj_event = self.middle_panel.getCurrentlyData()
        server_url = self.top_menu.connect_socket_widgets.getServerUrl()
        env = self.top_menu.environment_widgets.getEnvironmentName()
        print("server url : ", server_url)
        if env == "no environment":
            self.open_popup()
        else:
            self.data.saveData(obj_event, server_url, env)

    def onSaveNoEnvironment(self, new_environment):
        self.popup.destroy()
        self.popup = None
        obj_event = self.middle_panel.getCurrentlyData()
        server_url = self.top_menu.connect_socket_widgets.getServerUrl()
        self.data.saveData(obj_event, server_url, new_environment)
        self.top_menu.environment_widgets.updateEnvironment(self.data.getEnvList())
        self.syncEnvironment(new_environment) 


    def open_popup(self):
        if self.popup == None:
            self.popup=ctk.CTkToplevel(self)
            self.popup.geometry("340x100")
            self.popup.title("save environment")
            self.popup.focus()
            self.popup.attributes('-topmost', 'true')
            entry_env = ctk.CTkEntry(master=self.popup, width=320, placeholder_text="enter new environment")
            entry_env.grid(row=0, column=0, padx=10, pady=10)
            button_save: ctk.CTkButton = ctk.CTkButton(self.popup, width=320, text="Save", command=lambda: self.onSaveNoEnvironment(entry_env.get()))
            button_save.grid(row=1, column=0, padx=10)
        else:
            self.popup.focus()

class TopPanel(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(parent, height=50, fg_color="#212121")
        self.place(x=0, y=0, relwidth=1)  
        self.connect_socket_widgets = ConnectSocket_Widgets(self, cfg.Position(0, 0), "#212121")
        self.environment_widgets = Environment_Widgets(parent=self, envList=parent.data.getEnvList())
        self.environment_widgets.setCallbackEnvironment(parent.onChoosedEnvironment)
        self.environment_widgets.setCallbackSave(parent.onClickSaveEnv)

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

    def onFocusEvent(self, button: ctk.CTkButton, event_id: str, lastest_request_id: str):
        text = ctk.StringVar(value=button._text)
        text.trace("w", lambda name, index,mode, var=text: self.onTypingEntryEvent())
        self.emit_panel.setEntryText(text)
 
        event_dict = self.event_panel.event_list_panel.event_dict
        if lastest_request_id is not None :
            if lastest_request_id in event_dict:
                lastest_event = event_dict[lastest_request_id]
                lastest_event['request_body'] = self.emit_panel.getRequestBodyText().replace("\n", "")

       
        event = event_dict[event_id]
        self.emit_panel.setRequestBodyText(event['request_body'])

    def getCurrentlyData(self) -> dict:
        event_dict = self.event_panel.getCurrentList()
        obj_dict = {}
        for key, value in event_dict.items():
            button: ctk.CTkButton = value['button']
            obj_dict[key] = {
                "name": button._text,
                "request_body": value['request_body']
            }
        return obj_dict

    def syncEvents(self, data: EnvironmentModel):
        self.event_panel.deleteAllEvents()
        for event_id in data.events:
            event = data.getEventByKey(event_id)
            self.event_panel.addEvent(event.name, event_id, event.request_body);

class EventPanel(ctk.CTkFrame):
    def addEvent(self, text="New Event", event_id: str = None, request_body: str = ""):
        self.event_list_panel.addToEventList(text, event_id, request_body)
    
    def deleteEvent(self):
        self.event_list_panel.deleteEvent()
    
    def deleteAllEvents(self):
        self.event_list_panel.deleteAllEvents()
    
    def syncEventName(self, text):
        self.event_list_panel.on_focus_button.configure(text=text)

    def getCurrentList(self) -> dict:
        return self.event_list_panel.event_dict

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
        self.req_res_widget.scrollable_frame_request_body.delete("0.0", "end");
        self.req_res_widget.scrollable_frame_request_body.insert("end", text=text)

    def getRequestBodyText(self):
        return self.req_res_widget.scrollable_frame_request_body.get("0.0", "end")


