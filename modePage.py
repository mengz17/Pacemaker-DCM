import tkinter as tk
import tkinter.messagebox
from VOO import VOO_window
from AOO import AOO_window
from VVI import VVI_window
from AAI import AAI_window
from VOOR import VOOR_window
from AOOR import AOOR_window
from VVIR import VVIR_window
from AAIR import AAIR_window
from DOO import DOO_window
from DOOR import DOOR_window
from egram import egram
from checkConnect import checkConnect

def Ui_ModeWindow(upper_tk=None):


        if upper_tk == None:
                modeWindow = tk.Tk()
        else:
                modeWindow = tk.Toplevel()
        modeWindow.title("Mode Selection")
        modeWindow.geometry("400x250")

        background = tk.Canvas(modeWindow, width = 400, height = 400, bg = "white")
        background.pack(side = "top")

        #Mode Selection Buttons
        aooButton = tk.Button(modeWindow, text = "AOO", command = AOO_window, width = 10, height = 2).place(x = 10, y = 25)
        vooButton = tk.Button(modeWindow, text = "VOO", command = VOO_window, width = 10, height = 2).place(x = 110, y = 25)
        aaiButton = tk.Button(modeWindow, text = "AAI", command = AAI_window, width = 10, height = 2).place(x = 210, y = 25)
        vviButton = tk.Button(modeWindow, text = "VVI", command = VVI_window, width = 10, height = 2).place(x = 310, y = 25)

        aoorButton = tk.Button(modeWindow, text = "AOOR", command = AOOR_window, width = 10, height = 2).place(x = 10, y = 100)
        voorButton = tk.Button(modeWindow, text = "VOOR", command = VOOR_window, width = 10, height = 2).place(x = 110, y = 100)
        aairButton = tk.Button(modeWindow, text = "AAIR", command = AAIR_window, width = 10, height = 2).place(x = 210, y = 100)
        vvirButton = tk.Button(modeWindow, text = "VVIR", command = VVIR_window, width = 10, height = 2).place(x = 310, y = 100)

        dooButton = tk.Button(modeWindow, text = "DOO", command = DOO_window, width = 10, height = 2).place(x = 10, y = 175)
        doorButton = tk.Button(modeWindow, text = "DOOR", command = DOOR_window, width = 10, height = 2).place(x = 110, y = 175)
        egramButton = tk.Button(modeWindow, text = "Electrocardiogram", command = egramCheck, width = 24, height = 2).place(x = 210, y = 175)

def egramCheck():
        if checkConnect() == 6:
                        tkinter.messagebox.showerror("Error","Failed to connect to Pacemaker")
        else:
                egram()

#Ui_ModeWindow()
