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
application.mainloop()