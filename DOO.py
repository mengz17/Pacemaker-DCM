import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def DOO_window(upper_tk=None):

    global root_DOO
    global lrlLabel
    global urlLabel
    global delayLabel
    global aaLabel
    global vaLabel
    global apwLabel
    global vpwLabel

    global connectLable
    
    index = 0
    
    try:
        with open("parameterDOO.txt","r") as parameterFile:
                read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterDOO.txt","w") as parameterFile:
                while(index < 7):
                        parameterFile.write("N/A\n")
                        index += 1
                index = 0
        with open("parameterDOO.txt","r") as parameterFile:
            read = parameterFile.readlines()

    root_DOO = tk.Toplevel()
    root_DOO.title('DOO')
    root_DOO.geometry('500x450')

    label = tk.Label(root_DOO, text="Current Mode:   DOO",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_DOO, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_DOO, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=120)
    label = tk.Label(root_DOO, text="Atrial Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=160)
    label = tk.Label(root_DOO, text="Ventricular Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=200)
    label = tk.Label(root_DOO, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=240)
    label = tk.Label(root_DOO, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    label = tk.Label(root_DOO, text="Fixed AV Delay (ms):", font=("Times New Roman",14)).place(x=10,y=320)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_DOO, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_DOO, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
    
    lrlLabel = tk.StringVar()
    lrlLabel.set(read[0].strip("\n")) #lrlValue is input from user
    label = tk.Label(root_DOO, textvariable = lrlLabel, font=("Times New Roman",14)).place(x = 320, y = 80)

    urlLabel = tk.StringVar()
    urlLabel.set(read[1].strip("\n")) #urlValue is input from user
    label = tk.Label(root_DOO, textvariable = urlLabel, font=("Times New Roman",14)).place(x = 320, y = 120)

    aaLabel = tk.StringVar()
    aaLabel.set(read[2].strip("\n")) #aaValue is input from user
    label = tk.Label(root_DOO, textvariable = aaLabel, font=("Times New Roman",14)).place(x = 320, y = 160)

    vaLabel = tk.StringVar()
    vaLabel.set(read[3].strip("\n")) 
    label = tk.Label(root_DOO, textvariable = vaLabel, font=("Times New Roman",14)).place(x = 320, y = 200)

    apwLabel = tk.StringVar()
    apwLabel.set(read[4].strip("\n")) #apwValue is input from user
    label = tk.Label(root_DOO, textvariable = apwLabel, font=("Times New Roman",14)).place(x = 320, y = 240)

    vpwLabel = tk.StringVar()
    vpwLabel.set(read[5].strip("\n")) #apwValue is input from user
    label = tk.Label(root_DOO, textvariable = vpwLabel, font=("Times New Roman",14)).place(x = 320, y = 280)

    delayLabel = tk.StringVar()
    delayLabel.set(read[6].strip("\n")) #apwValue is input from user
    label = tk.Label(root_DOO, textvariable = delayLabel, font=("Times New Roman",14)).place(x = 320, y = 320)


    #modeWindowButton = tk.Button(root_DOO, text = "Change Mode", command = lambda:[root_DOO.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_DOO, text = "Change Parameter", command = DOO_ParameterWindow, width = 20, height = 2).place(x = 200, y = 380)


def DOO_ParameterWindow():

    with open("parameterDOO.txt","r") as parameterFile:
        readpara = parameterFile.readlines()


    global paraWindow
    
    paraWindow = tk.Toplevel()
    paraWindow.title('DOO Parameter Setting')
    paraWindow.geometry('500x450')
    label = tk.Label(paraWindow, text="Current Mode   DOO",font=("Times New Roman",14)).place(x=10,y=10)

    label = tk.Label(paraWindow, text="Lower Rate Limit (ppm):",font=("Times New Roman",14)).place(x=10,y=80)
    LRL_data = ['30','35','40','45']
    for i in range (50,90):
        LRL_data.append(i)
    for j in range (90,180):
        if j%5 == 0:
            LRL_data.append(j)
    LRL_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    LRL_roll['values'] = LRL_data
    LRL_roll.place(x=320, y=80)
    if readpara[0]!='N/A\n':  #Secret
        LRL_roll.set(readpara[0].strip("\n"))
    else:
        LRL_roll.current(0)



    label = tk.Label(paraWindow, text="Upper Rate Limit (ppm):",font=("Times New Roman",14)).place(x=10,y=120)
    URL_data = []
    for k in range (50,180):
        if k%5 == 0:
            URL_data.append(k)

    URL_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    URL_roll['values'] = URL_data
    URL_roll.place(x=320, y=120)
    if readpara[1]!='N/A\n':
        URL_roll.set(readpara[1].strip("\n"))
    else:
        URL_roll.current(0)


    label = tk.Label(paraWindow, text="Atrial Amplitude (V):",font=("Times New Roman",14)).place(x=10,y=160)
    AA_data = ['OFF']
    for a in range (1,51):
        AA_data.append(float(a/10))

    AA_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    AA_roll['values'] = AA_data
    AA_roll.place(x=320, y=160)
    if readpara[2]!='N/A\n':
        AA_roll.set(readpara[2].strip("\n"))
    else:
        AA_roll.current(0)


    label = tk.Label(paraWindow, text="Ventricular Amplitude (V):",font=("Times New Roman",14)).place(x=10,y=200)

    VA_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VA_roll['values'] = AA_data
    VA_roll.place(x=320, y=200)
    if readpara[3]!='N/A\n':
        VA_roll.set(readpara[3].strip("\n"))
    else:
        VA_roll.current(0)

    label = tk.Label(paraWindow, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=240)
    APW_data = []
    for c in range (1,31):
        APW_data.append(c)

    APW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    APW_roll['values'] = APW_data
    APW_roll.place(x=320, y=240)
    if readpara[4]!='N/A\n':
        APW_roll.set(readpara[4].strip("\n"))
    else:
        APW_roll.current(0)

    label = tk.Label(paraWindow, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    VPW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VPW_roll['values'] = APW_data
    VPW_roll.place(x=320, y=280)
    if readpara[5]!='N/A\n':
        VPW_roll.set(readpara[5].strip("\n"))
    else:
        VPW_roll.current(0)

    label = tk.Label(paraWindow, text="Fixed AV Delay (ms):", font=("Times New Roman",14)).place(x=10,y=320)
    DELAY_data = []
    for b in range (7,31):
        DELAY_data.append(b*10)
    DELAY_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    DELAY_roll['values'] = DELAY_data
    DELAY_roll.place(x=320, y=320)
    if readpara[6]!='N/A\n':
        DELAY_roll.set(readpara[6].strip("\n"))
    else:
        DELAY_roll.current(0)

    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

    def changePara():
        write = ['N/A'] *7
        d=0

        write[0] = LRL_roll.get()
        write[1] = URL_roll.get()
        if int(write[0]) > int(write[1]):
            tkinter.messagebox.showerror('Error', 'Lower Rate Limit cannot be bigger than Upper Rate Limit')
        else:
            write[2] = AA_roll.get()
            doo_aa_p = AA_roll.get()
            if doo_aa_p == 'OFF':
                doo_aa_p = 0
            else:
                doo_aa_p = int(100*float(doo_aa_p))
            write[3] = VA_roll.get()
            doo_va_p = VA_roll.get()
            if doo_va_p == 'OFF':
                doo_va_p = 0
            else:
                doo_va_p = int(100*float(doo_va_p))
            write[4] = APW_roll.get()
            write[5] = VPW_roll.get()
            write[6] = DELAY_roll.get()

            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_DOO, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_DOO, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

                writePara(mode = 5, Lower_Rate = int(LRL_roll.get()), AV_Delay = int(DELAY_roll.get()), ATR_Amplitude = int(doo_aa_p), VENT_Amplitude = int(doo_va_p), \
                    ATR_Width = int(APW_roll.get()), VENT_Width = int(VPW_roll.get()))


                with open("parameterDOO.txt","w") as parameterFile:
                    while (d < 7):
                        parameterFile.write(write[d]+"\n") #Write every index of list write[] into file
                        d += 1
                    d = 0

                lrlLabel.set(write[0])
                urlLabel.set(write[1])
                aaLabel.set(write[2])
                vaLabel.set(write[3])
                apwLabel.set(write[4])
                vpwLabel.set(write[5])
                delayLabel.set(write[6])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 380)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 380)

