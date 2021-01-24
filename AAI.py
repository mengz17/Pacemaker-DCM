import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def AAI_window(upper_tk=None):

    global root_AAI
    global lrlLabel
    global urlLabel
    global aaLabel
    global apwLabel
    global asLabel
    global arpLabel
    global pvarpLabel
    global rsLabel

    global connectLable
    
    index = 0
    
    try:
        with open("parameterAAI.txt","r") as parameterFile:
                read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterAAI.txt","w") as parameterFile:
                while(index < 8):
                        parameterFile.write("N/A\n")
                        index += 1
                index = 0
        with open("parameterAAI.txt","r") as parameterFile:
            read = parameterFile.readlines()

    root_AAI = tk.Toplevel()
    root_AAI.title('AAI')
    root_AAI.geometry('500x500')

    label = tk.Label(root_AAI, text="Current Mode:   AAI",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_AAI, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_AAI, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=120)
    label = tk.Label(root_AAI, text="Atrial Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=160)
    label = tk.Label(root_AAI, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=200)
    label = tk.Label(root_AAI, text="Atrial Sensitivity (V):", font=("Times New Roman",14)).place(x=10,y=240)
    label = tk.Label(root_AAI, text="Atrial Refractory Period (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    label = tk.Label(root_AAI, text="PVARP (ms):", font=("Times New Roman",14)).place(x=10,y=320)
    label = tk.Label(root_AAI, text="Rate Smoothing (%):", font=("Times New Roman",14)).place(x=10,y=360)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_AAI, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_AAI, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
    
    lrlLabel = tk.StringVar()
    lrlLabel.set(read[0].strip("\n")) #lrlValue is input from user
    label = tk.Label(root_AAI, textvariable = lrlLabel, font=("Times New Roman",14)).place(x = 320, y = 80)

    urlLabel = tk.StringVar()
    urlLabel.set(read[1].strip("\n")) #urlValue is input from user
    label = tk.Label(root_AAI, textvariable = urlLabel, font=("Times New Roman",14)).place(x = 320, y = 120)

    aaLabel = tk.StringVar()
    aaLabel.set(read[2].strip("\n")) #aaValue is input from user
    label = tk.Label(root_AAI, textvariable = aaLabel, font=("Times New Roman",14)).place(x = 320, y = 160)

    apwLabel = tk.StringVar()
    apwLabel.set(read[3].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAI, textvariable = apwLabel, font=("Times New Roman",14)).place(x = 320, y = 200)

    asLabel = tk.StringVar()
    asLabel.set(read[4].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAI, textvariable = asLabel, font=("Times New Roman",14)).place(x = 320, y = 240)

    arpLabel = tk.StringVar()
    arpLabel.set(read[5].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAI, textvariable = arpLabel, font=("Times New Roman",14)).place(x = 320, y = 280)

    pvarpLabel = tk.StringVar()
    pvarpLabel.set(read[6].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAI, textvariable = pvarpLabel, font=("Times New Roman",14)).place(x = 320, y = 320)

    rsLabel = tk.StringVar()
    rsLabel.set(read[7].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAI, textvariable = rsLabel, font=("Times New Roman",14)).place(x = 320, y = 360)

    #modeWindowButton = tk.Button(root_AAI, text = "Change Mode", command = lambda:[root_AAIR.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_AAI, text = "Change Parameter", command = AAI_ParameterWindow, width = 20, height = 2).place(x = 200, y = 410)


def AAI_ParameterWindow():

    with open("parameterAAI.txt","r") as parameterFile:
        readpara = parameterFile.readlines()

    global paraWindow
    
    paraWindow = tk.Toplevel()
    paraWindow.title('AAI Parameter Setting')
    paraWindow.geometry('500x500')
    label = tk.Label(paraWindow, text="Current Mode   AAI",font=("Times New Roman",14)).place(x=10,y=10)
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

    label = tk.Label(paraWindow, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=200)
    APW_data = []
    for b in range (1,31):
        APW_data.append(b)

    APW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    APW_roll['values'] = APW_data
    APW_roll.place(x=320, y=200)
    if readpara[3]!='N/A\n':
        APW_roll.set(readpara[3].strip("\n"))
    else:
        APW_roll.current(0)

    

    label = tk.Label(paraWindow, text="Atrial Sensitivity (V):", font=("Times New Roman",14)).place(x=10,y=240)
    AS_data = ['0']
    for c in range (1,51):
        AS_data.append(float(c/10))

    AS_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    AS_roll['values'] = AS_data
    AS_roll.place(x=320, y=240)
    if readpara[4]!='N/A\n':
        AS_roll.set(readpara[4].strip("\n"))
    else:
        AS_roll.current(0)


    label = tk.Label(paraWindow, text="Atrial Refractory Period (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    ARP_data = []
    for p in range (15,51):
        ARP_data.append(p)

    ARP_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    ARP_roll['values'] = ARP_data
    ARP_roll.place(x=320, y=280)
    if readpara[5]!='N/A\n':
        ARP_roll.set(readpara[5].strip("\n"))
    else:
        ARP_roll.current(0)

    label = tk.Label(paraWindow, text="PVARP (ms):", font=("Times New Roman",14)).place(x=10,y=320)
    PVARP_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    PVARP_roll['values'] = ARP_data
    PVARP_roll.place(x=320, y=320)
    if readpara[6]!='N/A\n':
        PVARP_roll.set(readpara[6].strip("\n"))
    else:
        PVARP_roll.current(0)

    label = tk.Label(paraWindow, text="Rate Smoothing (%):", font=("Times New Roman",14)).place(x=10,y=360)
    RS_data = ['OFF','3','6','9','12','15','18','21','25']

    RS_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RS_roll['values'] = RS_data
    RS_roll.place(x=320, y=360)
    if readpara[7]!='N/A\n':
        RS_roll.set(readpara[7].strip("\n"))
    else:
        RS_roll.current(0)

    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
    
    

    def changePara():
        write = ['N/A'] *8
        d=0

        write[0] = LRL_roll.get()
        write[1] = URL_roll.get()
        if int(write[0]) > int(write[1]):
            tkinter.messagebox.showerror('Error', 'Lower Rate Limit cannot be bigger than Upper Rate Limit')
        else:
            write[2] = AA_roll.get()
            aai_aa_p = AA_roll.get()
            if aai_aa_p == 'OFF':
                aai_aa_p = 0
            else:
                aai_aa_p = int(100*float(aai_aa_p))
            write[3] = APW_roll.get()
            write[4] = AS_roll.get()
            write[5] = ARP_roll.get()
            write[6] = PVARP_roll.get()
            write[7] = RS_roll.get()


            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_AAI, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_AAI, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                writePara(mode = 3, Lower_Rate = int(LRL_roll.get()), ATR_Amplitude = int(aai_aa_p), ATR_Width = int(APW_roll.get()), ATR_Refractory = int(ARP_roll.get()))
                
                with open("parameterAAI.txt","w") as parameterFile:
                    while (d < 8):
                        parameterFile.write(write[d]+"\n") #Write every index of list write[] into file
                        d += 1
                    d = 0

                lrlLabel.set(write[0])
                urlLabel.set(write[1])
                aaLabel.set(write[2])
                apwLabel.set(write[3])
                asLabel.set(write[4])
                arpLabel.set(write[5])
                pvarpLabel.set(write[6])
                rsLabel.set(write[7])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 410)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 410)

