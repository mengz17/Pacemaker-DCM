import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def DOOR_window(upper_tk=None):

    global root_DOOR
    global lrlLabel
    global urlLabel
    global delayLabel
    global aaLabel
    global vaLabel
    global apwLabel
    global vpwLabel
    global msrLabel
    global atLabel
    global reacLabel
    global rfLabel
    global recoLabel

    global connectLable
    
    index = 0
    
    try:
        with open("parameterDOOR.txt","r") as parameterFile:
                read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterDOOR.txt","w") as parameterFile:
                while(index < 12):
                        parameterFile.write("N/A\n")
                        index += 1
                index = 0
        with open("parameterDOOR.txt","r") as parameterFile:
            read = parameterFile.readlines()

    root_DOOR = tk.Toplevel()
    root_DOOR.title('DOOR')
    root_DOOR.geometry('500x650')

    label = tk.Label(root_DOOR, text="Current Mode:   DOOR",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_DOOR, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_DOOR, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=120)
    label = tk.Label(root_DOOR, text="Atrial Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=160)
    label = tk.Label(root_DOOR, text="Ventricular Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=200)
    label = tk.Label(root_DOOR, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=240)
    label = tk.Label(root_DOOR, text="Ventricular Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=280)
    label = tk.Label(root_DOOR, text="Fixed AV Delay (ms):", font=("Times New Roman",14)).place(x=10,y=320)
    label = tk.Label(root_DOOR, text="Maximum Sensor Rate (ppm):", font=("Times New Roman",14)).place(x=10,y=360)
    label = tk.Label(root_DOOR, text="Activity Threshold:", font=("Times New Roman",14)).place(x=10,y=400)
    label = tk.Label(root_DOOR, text="Reaction Time (sec):", font=("Times New Roman",14)).place(x=10,y=440)
    label = tk.Label(root_DOOR, text="Response Factor:", font=("Times New Roman",14)).place(x=10,y=480)
    label = tk.Label(root_DOOR, text="Recovery Time (min):", font=("Times New Roman",14)).place(x=10,y=520)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_DOOR, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_DOOR, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
    
    lrlLabel = tk.StringVar()
    lrlLabel.set(read[0].strip("\n")) #lrlValue is input from user
    label = tk.Label(root_DOOR, textvariable = lrlLabel, font=("Times New Roman",14)).place(x = 320, y = 80)

    urlLabel = tk.StringVar()
    urlLabel.set(read[1].strip("\n")) #urlValue is input from user
    label = tk.Label(root_DOOR, textvariable = urlLabel, font=("Times New Roman",14)).place(x = 320, y = 120)

    aaLabel = tk.StringVar()
    aaLabel.set(read[2].strip("\n")) #aaValue is input from user
    label = tk.Label(root_DOOR, textvariable = aaLabel, font=("Times New Roman",14)).place(x = 320, y = 160)

    vaLabel = tk.StringVar()
    vaLabel.set(read[3].strip("\n")) 
    label = tk.Label(root_DOOR, textvariable = vaLabel, font=("Times New Roman",14)).place(x = 320, y = 200)

    apwLabel = tk.StringVar()
    apwLabel.set(read[4].strip("\n")) #apwValue is input from user
    label = tk.Label(root_DOOR, textvariable = apwLabel, font=("Times New Roman",14)).place(x = 320, y = 240)

    vpwLabel = tk.StringVar()
    vpwLabel.set(read[5].strip("\n")) #apwValue is input from user
    label = tk.Label(root_DOOR, textvariable = vpwLabel, font=("Times New Roman",14)).place(x = 320, y = 280)

    delayLabel = tk.StringVar()
    delayLabel.set(read[6].strip("\n")) #apwValue is input from user
    label = tk.Label(root_DOOR, textvariable = delayLabel, font=("Times New Roman",14)).place(x = 320, y = 320)

    msrLabel = tk.StringVar()
    msrLabel.set(read[7].strip("\n")) 
    label = tk.Label(root_DOOR, textvariable = msrLabel, font=("Times New Roman",14)).place(x = 320, y = 360)

    atLabel = tk.StringVar()
    atLabel.set(read[8].strip("\n")) 
    label = tk.Label(root_DOOR, textvariable = atLabel, font=("Times New Roman",14)).place(x = 320, y = 400)

    reacLabel = tk.StringVar()
    reacLabel.set(read[9].strip("\n")) 
    label = tk.Label(root_DOOR, textvariable = reacLabel, font=("Times New Roman",14)).place(x = 320, y = 440)

    rfLabel = tk.StringVar()
    rfLabel.set(read[10].strip("\n")) 
    label = tk.Label(root_DOOR, textvariable = rfLabel, font=("Times New Roman",14)).place(x = 320, y = 480)

    recoLabel = tk.StringVar()
    recoLabel.set(read[11].strip("\n")) 
    label = tk.Label(root_DOOR, textvariable = recoLabel, font=("Times New Roman",14)).place(x = 320, y = 520)



    #modeWindowButton = tk.Button(root_DOOR, text = "Change Mode", command = lambda:[root_DOOR.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_DOOR, text = "Change Parameter", command = DOOR_ParameterWindow, width = 20, height = 2).place(x = 200, y = 570)


def DOOR_ParameterWindow():

    with open("parameterDOOR.txt","r") as parameterFile:
        readpara = parameterFile.readlines()


    global paraWindow
    
    paraWindow = tk.Toplevel()
    paraWindow.title('DOOR Parameter Setting')
    paraWindow.geometry('500x650')
    label = tk.Label(paraWindow, text="Current Mode   DOOR",font=("Times New Roman",14)).place(x=10,y=10)

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

        
    label = tk.Label(paraWindow, text="Maximum Sensor Rate (ppm):", font=("Times New Roman",14)).place(x=10,y=360)

    MSR_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    MSR_roll['values'] = URL_data
    MSR_roll.place(x=320, y=360)
    if readpara[7]!='N/A\n':
        MSR_roll.set(readpara[7].strip("\n"))
    else:
        MSR_roll.current(0)


    label = tk.Label(paraWindow, text="Activity Threshold:", font=("Times New Roman",14)).place(x=10,y=400)
    AT_data = ['V-Low', 'Low', 'Med-Low', 'Med','Med-High', 'High', 'V-High']
    AT_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    AT_roll['values'] = AT_data
    AT_roll.place(x=320, y=400)
    if readpara[8]!='N/A\n':
        AT_roll.set(readpara[8].strip("\n"))
    else:
        AT_roll.current(0)
        

    label = tk.Label(paraWindow, text="Reaction Time (sec)", font=("Times New Roman",14)).place(x=10,y=440)
    REAC_data = ['5(Test)','10','20','30','40','50']

    REAC_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    REAC_roll['values'] = REAC_data
    REAC_roll.place(x=320, y=440)
    if readpara[9]!='N/A\n':
        REAC_roll.set(readpara[9].strip("\n"))
    else:
        REAC_roll.current(1)



    label = tk.Label(paraWindow, text="Response Factor:", font=("Times New Roman",14)).place(x=10,y=480)
    RF_data = []
    for p in range (1,17):
        RF_data.append(p)
    RF_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RF_roll['values'] = RF_data
    RF_roll.place(x=320, y=480)
    if readpara[10]!='N/A\n':
        RF_roll.set(readpara[10].strip("\n"))
    else:
        RF_roll.current(0)

    label = tk.Label(paraWindow, text="Recovery Time (min):", font=("Times New Roman",14)).place(x=10,y=520)
    RECO_data = ['0.1(Test)']
    for q in range (2,17):
        RECO_data.append(q)
    RECO_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RECO_roll['values'] = RECO_data
    RECO_roll.place(x=320, y=520)
    if readpara[11]!='N/A\n':
        RECO_roll.set(readpara[11].strip("\n"))
    else:
        RECO_roll.current(1)

    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(paraWindow, textvariable=connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

    def changePara():
        write = ['N/A'] *12
        d=0

        write[0] = LRL_roll.get()
        write[1] = URL_roll.get()
        if int(write[0]) > int(write[1]):
            tkinter.messagebox.showerror('Error', 'Lower Rate Limit cannot be bigger than Upper Rate Limit')
        else:
            write[2] = AA_roll.get()
            door_aa_p = AA_roll.get()
            if door_aa_p == 'OFF':
                door_aa_p = 0
            else:
                door_aa_p = int(100*float(door_aa_p))
            write[3] = VA_roll.get()
            door_va_p = VA_roll.get()
            if door_va_p == 'OFF':
                door_va_p = 0
            else:
                door_va_p = int(100*float(door_va_p))
            write[4] = APW_roll.get()
            write[5] = VPW_roll.get()
            write[6] = DELAY_roll.get()
            write[7] = MSR_roll.get()
            write[8] = AT_roll.get()
            door_at_p = AT_roll.get()
            if door_at_p == 'V-Low':
                door_at_p = 0.5
            elif door_at_p == 'Low':
                door_at_p = 1.0
            elif door_at_p == 'Med-Low':
                door_at_p = 1.5
            elif door_at_p == 'Med':
                door_at_p = 1.75
            elif door_at_p == 'Med-High':
                door_at_p = 2.0
            elif door_at_p == 'High':
                door_at_p = 2.5
            elif door_at_p == 'V_High':
                door_at_p = 3.0
            write[9] = REAC_roll.get()
            door_reac_p = REAC_roll.get()
            if door_reac_p == '5(Test)':
                door_reac_p = 5
            write[10] = RF_roll.get()
            write[11] = RECO_roll.get()
            door_reco_p = RECO_roll.get()
            if door_reco_p == '0.1(Test)':
                door_reco_p = 6
            else:
                door_reco_p = 60 * int(door_reco_p)

            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_DOOR, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_DOOR, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

                writePara(mode = 10, Lower_Rate = int(LRL_roll.get()), MSR = int(MSR_roll.get()), AV_Delay = int(DELAY_roll.get()), ATR_Amplitude = int(door_aa_p), \
                    VENT_Amplitude = int(door_va_p),  ATR_Width = int(APW_roll.get()), VENT_Width = int(VPW_roll.get()), Activity_Threshold = door_at_p, \
                    Reaction_Time = int(door_reac_p), Response_Factor = int(RF_roll.get()), Recovery_Time = int(door_reco_p))


                with open("parameterDOOR.txt","w") as parameterFile:
                    while (d < 12):
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
                msrLabel.set(write[7])
                atLabel.set(write[8])
                reacLabel.set(write[9])
                rfLabel.set(write[10])
                recoLabel.set(write[11])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 570)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 570)

