import customtkinter as ctk
import theme_config as theme

def getFillRelativeSize(masterSize, selfSize):
    if masterSize == 0:
        return "A cannot be 0"
    
    X = (selfSize * 1) / masterSize
    return X