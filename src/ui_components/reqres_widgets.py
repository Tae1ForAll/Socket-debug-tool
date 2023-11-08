import customtkinter as ctk
import utilities.ui_factory as ui_factory
import configure
import json
import manager.server_manager as server
import msgpack

class ReqRes_Widgets():
    def __init__(self, parent: ctk.CTkFrame):
        #callback
        self.on_emit_callback = None

        self.entry_event_name = ctk.CTkEntry(master=parent, width=300, height=30)
        self.entry_event_name.place(x=10, y=10)
        self.button_emit = ui_factory.buttonBorderGreen(parent, "Emit", configure.Size(width=50, height=30), self.onClickEmit)
        self.button_emit.place(x=320, y=10)

        self.layout_grid = ctk.CTkFrame(master=parent)
        self.layout_grid.place(x=0, y=50, relwidth=1, relheight=0.9)
        
        self.layout_grid.grid_rowconfigure(0, weight=1)
        self.layout_grid.grid_columnconfigure(0, weight=1)
        self.layout_grid.grid_columnconfigure(1, weight=1)

        self.scrollable_frame_request_body = ctk.CTkTextbox(master=self.layout_grid, height=290, tabs=('1c', '1c', '1c'))
        self.scrollable_frame_request_body.grid(padx=10, column=0, row=0, sticky="nsew")

        self.scrollable_frame_response_body = ctk.CTkTextbox(master=self.layout_grid, height=290, tabs=('1c', '1c', '1c'))
        self.scrollable_frame_response_body.grid(padx=10, column=1, row=0, sticky="nsew")

        self.button_clear = ui_factory.buttonBorderRed(parent, "Clear", configure.Size(width=30, height=20), self.onClickClearResponseData)
        self.button_clear.pack(padx=10, pady=20, side="top", anchor="ne")

    def setOnEmitCallback(self, callback):
        self.on_emit_callback = callback

    def onClickEmit(self):
        request_body = self.getRequestBody()
        event_name = self.getEventName()
        server.emitReqeust(event_name, request_body, self.updateToResponseBox)
        if self.on_emit_callback is not None:
            self.on_emit_callback(request_body)

    def onClickClearResponseData(self):
        self.scrollable_frame_response_body.delete("0.0", "end");

    def updateToResponseBox(self, response_data: bytes):
        self.cleanDataTypeCannotParse(response_data)
        json_formatted_str = json.dumps(response_data, indent=4)
        self.scrollable_frame_response_body.insert("end", json_formatted_str)
        self.scrollable_frame_response_body.insert("end", "\n===============================================================\n")

    def cleanDataTypeCannotParse(self, response_data, parent_key=""):
        for key, value in response_data.items():
            if parent_key:
                child_key = f"{parent_key}.{key}"
            else:
                child_key = key
            if isinstance(value, msgpack.ext.ExtType):
                # may be undefined or all types that cannot parse to json
                response_data[key] = "undefined"
            if isinstance(value, dict):
                self.cleanDataTypeCannotParse(value, child_key)

    def setEventEntry(self, text: str):
        self.entry_event_name._textvariable = text

    def getRequestBody(self):
        return json.loads(self.scrollable_frame_request_body.get("0.0", "end"))

    def getEventName(self):
        return self.entry_event_name._textvariable.get()