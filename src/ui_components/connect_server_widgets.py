import customtkinter as ctk
import configure as cfg
import manager.server_manager as server
import theme_config as theme
import utilities.ui_factory as ui_factory

class ConnectSocket_Widgets(ctk.CTkFrame):
    command_button_connect = None
    
    def connectToServer(self):
        server_url = self.entry_connect_socket.get();
        server.connect_server(server_url=server_url);
    
    # Initialize Widgets
    def __init__(self, parent: ctk.CTk, place: cfg.Position, all_color: str):
        super().__init__(parent, height=50, fg_color=all_color, bg_color=all_color)
        self.place(x=place.x, y=place.y)
        self.entry_connect_socket = ctk.CTkEntry(master=self, width=320)
        self.entry_connect_socket.grid(row=0, column=0, padx=10, pady=10)

        self.button_connect_socket = ui_factory.buttonBorderGreen(self, "Connect", cfg.Size(width=80, height=30), self.connectToServer);
        self.button_connect_socket.grid(row=0, column=1)

    def syncServerUrl(self, url: str):
        text = ctk.StringVar(value=url)
        text.trace("w", callback=None)
        self.entry_connect_socket.configure(textvariable = text);

