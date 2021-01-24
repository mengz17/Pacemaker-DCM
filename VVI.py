import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def VVI_window(upper_tk=None):

    global root_VVI
    global lrlLabel
    global urlLabel
    global vaLabel
    global vpwLabel
    global vsLabel
    global vrpLabel
    global rsLabel

    global connectLable
    
    index = 0
    
    try:
        with open("parameterVVI.txt","r") as parameterFile:
                read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterVVI.txt","w") as parameterFile:
                while(index < 7):
                        parameterFile.write("N/A\n")
                        index += 1
                index = 0
        with open("parameterVVI.txt","r") as parameterFile:
            read = parameterFile.readlines()

    #if upper_tk == None:
     #   root_AOO = tk.Tk()
    #else:
    root_VVI = tk.Toplevel()
    root_VVI.title('VVI')
    root_VVI.geometry('500x500')

    label = tk.Label(root_VVI, text="Current Mode:   VVI",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_VVI, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_VVI, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=120)
    label = tk.Label(root_VVI, text="Ventricular Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=160)
    label = tk.Label(root_VVI, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=200)
    label = tk.Label(root_VVI, text="Ventricular Sensitivity (V):", font=("Times New Roman",14)).place(x=10,y=240)
    label = tk.Label(root_VVI, text="Ventricular Refractory Period (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    label = tk.Label(root_VVI, text="Rate Smoothing (%):", font=("Times New Roman",14)).place(x=10,y=320)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_VVI, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_VVI, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

    lrlLabel = tk.StringVar()
    lrlLabel.set(read[0].strip("\n")) #lrlValue is input from user
    label = tk.Label(root_VVI, textvariable = lrlLabel, font=("Times New Roman",14)).place(x = 320, y = 80)

    urlLabel = tk.StringVar()
    urlLabel.set(read[1].strip("\n")) #urlValue is input from user
    label = tk.Label(root_VVI, textvariable = urlLabel, font=("Times New Roman",14)).place(x = 320, y = 120)

    vaLabel = tk.StringVar()
    vaLabel.set(read[2].strip("\n")) #aaValue is input from user
    label = tk.Label(root_VVI, textvariable = vaLabel, font=("Times New Roman",14)).place(x = 320, y = 160)

    vpwLabel = tk.StringVar()
    vpwLabel.set(read[3].strip("\n")) #apwValue is input from user
    label = tk.Label(root_VVI, textvariable = vpwLabel, font=("Times New Roman",14)).place(x = 320, y = 200)

    vsLabel = tk.StringVar()
    vsLabel.set(read[4].strip("\n")) #apwValue is input from user
    label = tk.Label(root_VVI, textvariable = vsLabel, font=("Times New Roman",14)).place(x = 320, y = 240)

    vrpLabel = tk.StringVar()
    vrpLabel.set(read[5].strip("\n")) #apwValue is input from user
    label = tk.Label(root_VVI, textvariable = vrpLabel, font=("Times New Roman",14)).place(x = 320, y = 280)

    rsLabel = tk.StringVar()
    rsLabel.set(read[6].strip("\n")) #apwValue is input from user
    label = tk.Label(root_VVI, textvariable = rsLabel, font=("Times New Roman",14)).place(x = 320, y = 320)


    #modeWindowButton = tk.Button(root_VVI, text = "Change Mode", command = lambda:[root_VVI.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_VVI, text = "Change Parameter", command = VVI_ParameterWindow, width = 20, height = 2).place(x = 200, y = 400)


def VVI_ParameterWindow():

    with open("parameterVVI.txt","r") as parameterFile:
        readpara = parameterFile.readlines()

    global paraWindow

    paraWindow = tk.Toplevel()
    paraWindow.title('VVI Parameter Setting')
    paraWindow.geometry('500x500')

    label = tk.Label(paraWindow, text="Current Mode   VVI",font=("Times New Roman",14)).place(x=10,y=10)
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


    label = tk.Label(paraWindow, text="Ventricular Amplitude (V):",font=("Times New Roman",14)).place(x=10,y=160)
    VA_data = ['OFF']
    for a in range (1,51):
        VA_data.append(float(a/10))


    VA_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VA_roll['values'] = VA_data
    VA_roll.place(x=320, y=160)
    if readpara[2]!='N/A\n':
        VA_roll.set(readpara[2].strip("\n"))
    else:
        VA_roll.current(0)

    label = tk.Label(paraWindow, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=200)
    VPW_data = []
    for b in range (1,31):
        VPW_data.append(b)

    VPW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VPW_roll['values'] = VPW_data
    VPW_roll.place(x=320, y=200)
    if readpara[3]!='N/A\n':
        VPW_roll.set(readpara[3].strip("\n"))
    else:
        VPW_roll.current(0)

    

    label = tk.Label(paraWindow, text="Ventricular Sensitivity (V):", font=("Times New Roman",14)).place(x=10,y=240)
    VS_data = ['0']
    for c in range (1,51):
        VS_data.append(float(c/10))

    VS_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VS_roll['values'] = VS_data
    VS_roll.place(x=320, y=240)
    if readpara[4]!='N/A\n':
        VS_roll.set(readpara[4].strip("\n"))
    else:
        VS_roll.current(0)


    label = tk.Label(paraWindow, text="Ventricular Refractory Period (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    VRP_data = []
    for p in range (15,51):
        VRP_data.append(p)

    VRP_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    VRP_roll['values'] = VRP_data
    VRP_roll.place(x=320, y=280)
    if readpara[5]!='N/A\n':
        VRP_roll.set(readpara[5].strip("\n"))
    else:
        VRP_roll.current(0)
    

    label = tk.Label(paraWindow, text="Rate Smoothing (%):", font=("Times New Roman",14)).place(x=10,y=320)
    RS_data = ['OFF','3','6','9','12','15','18','21','25']

    RS_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RS_roll['values'] = RS_data
    RS_roll.place(x=320, y=320)
    if readpara[6]!='N/A\n':
        RS_roll.set(readpara[6].strip("\n"))
    else:
        RS_roll.current(0)
    
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
            write[2] = VA_roll.get()
            vvi_va_p = VA_roll.get()
            if vvi_va_p == 'OFF':
                vvi_va_p = 0
            else:
                vvi_va_p = int(100*float(vvi_va_p))
            write[3] = VPW_roll.get()
            write[4] = VS_roll.get()
            write[5] = VRP_roll.get()
            write[6] = RS_roll.get()

            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_VVI, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_VVI, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

                writePara(mode = 4, Lower_Rate = int(LRL_roll.get()), VENT_Amplitude = int(vvi_va_p), VENT_Width = int(VPW_roll.get()), VENT_Refractory = int(VRP_roll.get()))


                with open("parameterVVI.txt","w") as parameterFile:
                    while (d < 7):
                        parameterFile.write(write[d]+"\n") #Write every index of list write[] into file
                        d += 1
                    d = 0

                lrlLabel.set(write[0])
                urlLabel.set(write[1])
                vaLabel.set(write[2])
                vpwLabel.set(write[3])
                vsLabel.set(write[4])
                vrpLabel.set(write[5])
                rsLabel.set(write[6])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 400)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 400)

#VVI_window()
