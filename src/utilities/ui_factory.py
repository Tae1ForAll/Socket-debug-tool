import customtkinter as ctk
import configure
import theme_config as theme

def buttonBorderGreen(master, text, size: configure.Size, callback):
    return ctk.CTkButton(
            master=master, 
            width=size.width,
            height=size.height, 
            text=text,
            font=ctk.CTkFont('Helvetica',size=12, weight='bold'), 
            text_color="White",
            fg_color="#343638",
            border_width=2,
            hover_color=theme.btn_color_green,
            border_color=theme.btn_color_green,
            command=callback)

def buttonBorderRed(master, text, size: configure.Size, callback):
    return ctk.CTkButton(
            master=master, 
            width=size.width,
            height=size.height, 
            text=text,
            font=ctk.CTkFont('Helvetica',size=12, weight='bold'), 
            text_color="White",
            fg_color="#343638",
            border_width=2,
            hover_color=theme.btn_color_red,
            border_color=theme.btn_color_red,
            command=callback)

def dropdownBox():
    # todo : implement
    return None
