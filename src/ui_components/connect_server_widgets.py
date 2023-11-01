import customtkinter as ctk
import configure as cfg
import manager.server_manager as server

class ConnectSocket_Widgets(ctk.CTkFrame):
    command_button_connect = None
    
    def connectToServer(self):
        server_url = self.entry_connect_socket.get();
        server.connect_server(server_url=server_url);
    
    def __init__(self, parent: ctk.CTk, place: cfg.Position):
        super().__init__(parent, height=50, fg_color="Orange", bg_color="Orange")
        self.place(x=place.x, y=place.y)
        self.entry_connect_socket = ctk.CTkEntry(master=self, width=320, placeholder_text="URL")
        self.entry_connect_socket.grid(row=0, column=0, padx=10, pady=10)

        self.button_connect_socket = ctk.CTkButton(
            master=self, 
            width=100, 
            text="CONNECT", 
            fg_color="#91e391", 
            command=self.connectToServer,
            text_color="#404040")
        self.button_connect_socket.grid(row=0, column=1)


