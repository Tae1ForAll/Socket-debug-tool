from tkinter import *
import customtkinter
import app
import configure
import manager.server_manager as server
import asyncio

# theme configuration
customtkinter.set_appearance_mode("dark");
# customtkinter.set_default_color_theme("dark-blue");

application = app.App(
    title="MR.RED - Socket debugger tool", 
    min_size=configure.Size(width=1280, height=720),
    max_size=None,
    bg_color="#262626"
    );


    


#####
scrollable_frame_request_body = customtkinter.CTkScrollableFrame(application, width=900, height=290)
scrollable_frame_request_body.place(x=340, y=100);

scrollable_frame_response_body = customtkinter.CTkScrollableFrame(application, width=900, height=290)
scrollable_frame_response_body.place(x=340, y=410);

entry_event_name = customtkinter.CTkEntry(master=application, width=300, placeholder_text="Event name")
entry_event_name.place(x=340, y=65);

button_emit_request = customtkinter.CTkButton(
    master=application, 
    width=50, 
    text="RUN", 
    fg_color="#91e391", 
    text_color="#404040")
button_emit_request.place(x=650, y=65);



application.mainloop()