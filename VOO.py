import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def VOO_window(upper_tk=None):

    global root_VOO
    global voo_lrlLabel
    global voo_urlLabel
    global voo_vaLabel
    global voo_vpwLabel

    global connectLable
    index = 0
    
    try:
        with open("parameterVOO.txt","r") as parameterFile:
            read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterVOO.txt","w") as parameterFile:
            while(index < 4):
                    parameterFile.write("N/A\n")
                    index += 1
            index = 0
        with open("parameterVOO.txt","r") as parameterFile:
            read = parameterFile.readlines()

    #if upper_tk == None:
     #   root_VOO = tk.Tk()
    #else:
    root_VOO = tk.Toplevel()
    root_VOO.title('VOO')
    root_VOO.geometry('500x400')

    label = tk.Label(root_VOO, text="Current Mode:   VOO",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_VOO, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_VOO, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=130)
    label = tk.Label(root_VOO, text="Ventricular Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=180)
    label = tk.Label(root_VOO, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=230)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_VOO, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_VOO, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
    
    voo_lrlLabel = tk.StringVar()
    voo_lrlLabel.set(read[0].strip("\n")) 
    label = tk.Label(root_VOO, textvariable = voo_lrlLabel, font=("Times New Roman",14)).place(x = 250, y = 80)

    voo_urlLabel = tk.StringVar()
    voo_urlLabel.set(read[1].strip("\n")) 
    label = tk.Label(root_VOO, textvariable = voo_urlLabel, font=("Times New Roman",14)).place(x = 250, y = 130)

    voo_vaLabel = tk.StringVar()
    voo_vaLabel.set(read[2].strip("\n")) 
    label = tk.Label(root_VOO, textvariable = voo_vaLabel, font=("Times New Roman",14)).place(x = 250, y = 180)

    voo_vpwLabel = tk.StringVar()
    voo_vpwLabel.set(read[3].strip("\n")) 
    label = tk.Label(root_VOO, textvariable = voo_vpwLabel, font=("Times New Roman",14)).place(x = 250, y = 230)

    #modeWindowButton = tk.Button(root_VOO, text = "Change Mode", command = lambda:[root_VOO.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_VOO, text = "Change Parameter", command = Ui_ParameterWindow, width = 20, height = 2).place(x = 200, y = 300)


def Ui_ParameterWindow():

    with open("parameterVOO.txt","r") as parameterFile:
        readpara = parameterFile.readlines()

    global paraWindow

    paraWindow = tk.Toplevel()
    paraWindow.title('VOO Parameter Setting')
    paraWindow.geometry('500x400')
    label = tk.Label(paraWindow, text="Current Mode   VOO",font=("Times New Roman",14)).place(x=10,y=10)
    label = tk.Label(paraWindow, text="Lower Rate Limit (ppm):",font=("Times New Roman",14)).place(x=10,y=80)
    LRL_data = ['30','35','40','45']
    for i in range (50,90):
        LRL_data.append(i)
    for j in range (90,180):
        if j%5 == 0:
            LRL_data.append(j)
    LRL_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    LRL_roll['values'] = LRL_data
    LRL_roll.place(x=250, y=80)
    if readpara[0]!='N/A\n':  #Secret
        LRL_roll.set(readpara[0].strip("\n"))
    else:
        LRL_roll.current(0)



    label = tk.Label(paraWindow, text="Upper Rate Limit (ppm):",font=("Times New Roman",14)).place(x=10,y=130)
    URL_data = []
    for k in range (50,180):
        if k%5 == 0:
            URL_data.append(k)

    URL_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    URL_roll['values'] = URL_data
    URL_roll.place(x=250, y=130)
    if readpara[1]!='N/A\n':
        URL_roll.set(readpara[1].strip("\n"))
    else:
        URL_roll.current(0)


    label = tk.Label(paraWindow, text="Ventricular Amplitude (V):",font=("Times New Roman",14)).place(x=10,y=180)
    VA_data = ['OFF']
    for a in range (1,51):
        VA_data.append(float(a/10))


    VA_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VA_roll['values'] = VA_data
    VA_roll.place(x=250, y=180)
    if readpara[2]!='N/A\n':
        VA_roll.set(readpara[2].strip("\n"))
    else:
        VA_roll.current(0)

    label = tk.Label(paraWindow, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=230)
    VPW_data = []
    for c in range (1,31):
        VPW_data.append(c)

    VPW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VPW_roll['values'] = VPW_data
    VPW_roll.place(x=250, y=230)
    if readpara[3]!='N/A\n':
        VPW_roll.set(readpara[3].strip("\n"))
    else:
        VPW_roll.current(0)

    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)       

    def changePara():
        write = ['N/A'] *4
        d=0

        write[0] = LRL_roll.get()
        write[1] = URL_roll.get()
        if int(write[0]) > int(write[1]):
            tkinter.messagebox.showerror('Error', 'Lower Rate Limit cannot be bigger than Upper Rate Limit')
        else:
            write[2] = VA_roll.get()
            voo_va_p = VA_roll.get()
            if voo_va_p == 'OFF':
                voo_va_p = 0
            else:
                voo_va_p = int(100*float(voo_va_p))
            write[3] = VPW_roll.get()
            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_VOO, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_VOO, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

                writePara(mode = 2, Lower_Rate = int(LRL_roll.get()), VENT_Amplitude = int(voo_va_p), VENT_Width = int(VPW_roll.get()))


                with open("parameterVOO.txt","w") as parameterFile:
                    while (d < 4):
                        parameterFile.write(write[d]+"\n") #Write every index of list write[] into file
                        d += 1
                    d = 0

                voo_lrlLabel.set(write[0])
                voo_urlLabel.set(write[1])
                voo_vaLabel.set(write[2])
                voo_vpwLabel.set(write[3])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 300)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 300)

#VOO_window()

