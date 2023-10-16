from tkinter import *
import customtkinter 

# theme configuration
customtkinter.set_appearance_mode("dark");
# customtkinter.set_default_color_theme("dark-blue");

# Create object
gui = customtkinter.CTk()
# Set up title
gui.title("MR.RED - Socket debugger tool")
# Set up min size
gui.minsize(width=720, height=720)
# Set up background color
gui.configure(bg="#262626")

entry_connect_socket = customtkinter.CTkEntry(master=gui, width=320, placeholder_text="URL")
entry_connect_socket.place(x=10, y=10);

#ff9900
button_connect_socket = customtkinter.CTkButton(
    master=gui, 
    width=100, 
    text="CONNECT", 
    fg_color="#91e391", 
    text_color="#404040")
button_connect_socket.place(x=335, y=10);

scrollable_frame_event = customtkinter.CTkScrollableFrame(gui, width=300, height=600)
scrollable_frame_event.place(x=10, y=100)

scrollable_frame_request_body = customtkinter.CTkScrollableFrame(gui, width=900, height=290)
scrollable_frame_request_body.place(x=340, y=100);

scrollable_frame_response_body = customtkinter.CTkScrollableFrame(gui, width=900, height=290)
scrollable_frame_response_body.place(x=340, y=410);

entry_event_name = customtkinter.CTkEntry(master=gui, width=300, placeholder_text="Event name")
entry_event_name.place(x=340, y=65);

button_emit_request = customtkinter.CTkButton(
    master=gui, 
    width=50, 
    text="RUN", 
    fg_color="#91e391", 
    text_color="#404040")
button_emit_request.place(x=650, y=65);

optionmenu = customtkinter.CTkOptionMenu(gui, values=["no environment", "option 2"])
optionmenu.set("no environment")
optionmenu.place(x=445, y=10)

gui.mainloop()