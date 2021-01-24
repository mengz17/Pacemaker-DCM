import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def AAIR_window(upper_tk=None):

    global root_AAIR
    global lrlLabel
    global urlLabel
    global aaLabel
    global apwLabel
    global msrLabel
    global atLabel
    global reacLabel
    global rfLabel
    global recoLabel
    global asLabel
    global arpLabel
    global pvarpLabel
    global rsLabel

    global connectLable

    index = 0
    
    try:
        with open("parameterAAIR.txt","r") as parameterFile:
            read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterAAIR.txt","w") as parameterFile:
            while(index < 13):
                    parameterFile.write("N/A\n")
                    index += 1
            index = 0
        with open("parameterAAIR.txt","r") as parameterFile:
            read = parameterFile.readlines()

    root_AAIR = tk.Toplevel()
    root_AAIR.title('AAIR')
    root_AAIR.geometry('500x650')

    label = tk.Label(root_AAIR, text="Current Mode:   AAIR",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_AAIR, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_AAIR, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=120)
    label = tk.Label(root_AAIR, text="Atrial Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=160)
    label = tk.Label(root_AAIR, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=200)
    label = tk.Label(root_AAIR, text="Maximum Sensor Rate (ppm):", font=("Times New Roman",14)).place(x=10,y=240)
    label = tk.Label(root_AAIR, text="Activity Threshold:", font=("Times New Roman",14)).place(x=10,y=280)
    label = tk.Label(root_AAIR, text="Reaction Time (sec):", font=("Times New Roman",14)).place(x=10,y=320)
    label = tk.Label(root_AAIR, text="Response Factor:", font=("Times New Roman",14)).place(x=10,y=360)
    label = tk.Label(root_AAIR, text="Recovery Time (min):", font=("Times New Roman",14)).place(x=10,y=400)
    label = tk.Label(root_AAIR, text="Atrial Sensitivity (V):", font=("Times New Roman",14)).place(x=10,y=440)
    label = tk.Label(root_AAIR, text="Atrial Refractory Period (ms):", font=("Times New Roman",14)).place(x=10,y=480)
    label = tk.Label(root_AAIR, text="PVARP (ms):", font=("Times New Roman",14)).place(x=10,y=520)
    label = tk.Label(root_AAIR, text="Rate Smoothing (%):", font=("Times New Roman",14)).place(x=10,y=560)

    
    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_AAIR, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_AAIR, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

    lrlLabel = tk.StringVar()
    lrlLabel.set(read[0].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = lrlLabel, font=("Times New Roman",14)).place(x = 320, y = 80)

    urlLabel = tk.StringVar()
    urlLabel.set(read[1].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = urlLabel, font=("Times New Roman",14)).place(x = 320, y = 120)

    aaLabel = tk.StringVar()
    aaLabel.set(read[2].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = aaLabel, font=("Times New Roman",14)).place(x = 320, y = 160)

    apwLabel = tk.StringVar()
    apwLabel.set(read[3].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = apwLabel, font=("Times New Roman",14)).place(x = 320, y = 200)

    msrLabel = tk.StringVar()
    msrLabel.set(read[4].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = msrLabel, font=("Times New Roman",14)).place(x = 320, y = 240)

    atLabel = tk.StringVar()
    atLabel.set(read[5].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = atLabel, font=("Times New Roman",14)).place(x = 320, y = 280)

    reacLabel = tk.StringVar()
    reacLabel.set(read[6].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = reacLabel, font=("Times New Roman",14)).place(x = 320, y = 320)

    rfLabel = tk.StringVar()
    rfLabel.set(read[7].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = rfLabel, font=("Times New Roman",14)).place(x = 320, y = 360)

    recoLabel = tk.StringVar()
    recoLabel.set(read[8].strip("\n")) 
    label = tk.Label(root_AAIR, textvariable = recoLabel, font=("Times New Roman",14)).place(x = 320, y = 400)

    asLabel = tk.StringVar()
    asLabel.set(read[9].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAIR, textvariable = asLabel, font=("Times New Roman",14)).place(x = 320, y = 440)

    arpLabel = tk.StringVar()
    arpLabel.set(read[10].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAIR, textvariable = arpLabel, font=("Times New Roman",14)).place(x = 320, y = 480)

    pvarpLabel = tk.StringVar()
    pvarpLabel.set(read[6].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAIR, textvariable = pvarpLabel, font=("Times New Roman",14)).place(x = 320, y = 520)

    rsLabel = tk.StringVar()
    rsLabel.set(read[11].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AAIR, textvariable = rsLabel, font=("Times New Roman",14)).place(x = 320, y = 560)
    

    #modeWindowButton = tk.Button(root_AAIR, text = "Change Mode", command = lambda:[root_AAIR.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_AAIR, text = "Change Parameter", command = AAIR_ParameterWindow, width = 20, height = 1).place(x = 200, y = 600)


def AAIR_ParameterWindow():

    with open("parameterAAIR.txt","r") as parameterFile:
        readpara = parameterFile.readlines()

    global paraWindow

    paraWindow = tk.Toplevel()
    paraWindow.title('AAIR Parameter Setting')
    paraWindow.geometry('500x650')
    label = tk.Label(paraWindow, text="Current Mode   AAIR",font=("Times New Roman",14)).place(x=10,y=10)
    
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
    for c in range (1,31):
        APW_data.append(c)

    APW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    APW_roll['values'] = APW_data
    APW_roll.place(x=320, y=200)
    if readpara[3]!='N/A\n':
        APW_roll.set(readpara[3].strip("\n"))
    else:
        APW_roll.current(0)

    
    label = tk.Label(paraWindow, text="Maximum Sensor Rate (ppm):", font=("Times New Roman",14)).place(x=10,y=240)

    MSR_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    MSR_roll['values'] = URL_data
    MSR_roll.place(x=320, y=240)
    if readpara[4]!='N/A\n':
        MSR_roll.set(readpara[4].strip("\n"))
    else:
        MSR_roll.current(0)


    label = tk.Label(paraWindow, text="Activity Threshold:", font=("Times New Roman",14)).place(x=10,y=280)
    AT_data = ['V-Low', 'Low', 'Med-Low', 'Med','Med-High', 'High', 'V-High']

    AT_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    AT_roll['values'] = AT_data
    AT_roll.place(x=320, y=280)
    if readpara[5]!='N/A\n':
        AT_roll.set(readpara[5].strip("\n"))
    else:
        AT_roll.current(0)
        

    label = tk.Label(paraWindow, text="Reaction Time (sec)", font=("Times New Roman",14)).place(x=10,y=320)
    REAC_data = ['5(Test)','10','20','30','40','50']

    REAC_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    REAC_roll['values'] = REAC_data
    REAC_roll.place(x=320, y=320)
    if readpara[6]!='N/A\n':
        REAC_roll.set(readpara[6].strip("\n"))
    else:
        REAC_roll.current(1)



    label = tk.Label(paraWindow, text="Response Factor:", font=("Times New Roman",14)).place(x=10,y=360)
    RF_data = []
    for a in range (1,17):
        RF_data.append(a)
    RF_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RF_roll['values'] = RF_data
    RF_roll.place(x=320, y=360)
    if readpara[7]!='N/A\n':
        RF_roll.set(readpara[7].strip("\n"))
    else:
        RF_roll.current(0)

    label = tk.Label(paraWindow, text="Recovery Time (min):", font=("Times New Roman",14)).place(x=10,y=400)
    RECO_data = ['0.1(Test)']
    for a in range (2,17):
        RECO_data.append(a)
    RECO_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RECO_roll['values'] = RECO_data
    RECO_roll.place(x=320, y=400)
    if readpara[8]!='N/A\n':
        RECO_roll.set(readpara[8].strip("\n"))
    else:
        RECO_roll.current(1)

    
    label = tk.Label(paraWindow, text="Atrial Sensitivity (V):", font=("Times New Roman",14)).place(x=10,y=440)
    AS_data = ['0']
    for c in range (1,51):
        AS_data.append(float(c/10))

    AS_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    AS_roll['values'] = AS_data
    AS_roll.place(x=320, y=440)
    if readpara[9]!='N/A\n':
        AS_roll.set(readpara[9].strip("\n"))
    else:
        AS_roll.current(0)


    label = tk.Label(paraWindow, text="Atrial Refractory Period (ms):", font=("Times New Roman",14)).place(x=10,y=480)
    ARP_data = []
    for p in range (15,51):
        ARP_data.append(p)

    ARP_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    ARP_roll['values'] = ARP_data
    ARP_roll.place(x=320, y=480)
    if readpara[10]!='N/A\n':
        ARP_roll.set(readpara[10].strip("\n"))
    else:
        ARP_roll.current(0)

    label = tk.Label(paraWindow, text="PVARP (ms):", font=("Times New Roman",14)).place(x=10,y=520)
    PVARP_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    PVARP_roll['values'] = ARP_data
    PVARP_roll.place(x=320, y=520)
    if readpara[11]!='N/A\n':
        PVARP_roll.set(readpara[11].strip("\n"))
    else:
        PVARP_roll.current(0)
    

    label = tk.Label(paraWindow, text="Rate Smoothing (%):", font=("Times New Roman",14)).place(x=10,y=560)
    RS_data = ['OFF','3','6','9','12','15','18','21','25']

    RS_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    RS_roll['values'] = RS_data
    RS_roll.place(x=320, y=560)
    if readpara[12]!='N/A\n':
        RS_roll.set(readpara[12].strip("\n"))
    else:
        RS_roll.current(0)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
        
    def changePara():
        write = ['N/A'] *13
        p=0

        write[0] = LRL_roll.get()
        write[1] = URL_roll.get()
        if int(write[0]) > int(write[1]):
            tkinter.messagebox.showerror('Error', 'Lower Rate Limit cannot be bigger than Upper Rate Limit')
        else:
            write[2] = AA_roll.get()
            aair_aa_p = AA_roll.get()
            if aair_aa_p == 'OFF':
                aair_aa_p = 0
            else:
                aair_aa_p = int(100*float(aair_aa_p))
            write[3] = APW_roll.get()
            write[4] = MSR_roll.get()
            write[5] = AT_roll.get()
            aair_at_p = AT_roll.get()
            if aair_at_p == 'V-Low':
                aair_at_p = 0.5
            elif aair_at_p == 'Low':
                aair_at_p = 1.0
            elif aair_at_p == 'Med-Low':
                aair_at_p = 1.5
            elif aair_at_p == 'Med':
                aair_at_p = 1.75
            elif aair_at_p == 'Med-High':
                aair_at_p = 2.0
            elif aair_at_p == 'High':
                aair_at_p = 2.5
            elif aair_at_p == 'V_High':
                aair_at_p = 3.0
            write[6] = REAC_roll.get()
            aair_reac_p = REAC_roll.get()
            if aair_reac_p == '5(Test)':
                aair_reac_p = 5
            write[7] = RF_roll.get()
            write[8] = RECO_roll.get()
            aair_reco_p = RECO_roll.get()
            if aair_reco_p == '0.1(Test)':
                aair_reco_p = 6
            else:
                aair_reco_p  = 60 * int(aair_reco_p)
            write[9] = AS_roll.get()
            write[10] = ARP_roll.get()
            write[11] = PVARP_roll.get()
            write[12] = RS_roll.get()

            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_AAIR, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_AAIR, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)

                writePara(mode = 9, Lower_Rate = int(LRL_roll.get()), MSR = int(MSR_roll.get()), ATR_Amplitude = int(aair_aa_p), ATR_Width = int(APW_roll.get()), \
                    ATR_Refractory = int(ARP_roll.get()), Activity_Threshold = aair_at_p, Reaction_Time = int(aair_reac_p), Response_Factor = int(RF_roll.get()), \
                    Recovery_Time = int(aair_reco_p))


                with open("parameterAAIR.txt","w") as parameterFile:
                    while (p < 13):
                        parameterFile.write(write[p]+"\n") #Write every index of list write[] into file
                        p += 1
                    p = 0

                lrlLabel.set(write[0])
                urlLabel.set(write[1])
                aaLabel.set(write[2])
                apwLabel.set(write[3])
                msrLabel.set(write[4])
                atLabel.set(write[5])
                reacLabel.set(write[6])
                rfLabel.set(write[7])
                recoLabel.set(write[8])
                asLabel.set(write[9])
                arpLabel.set(write[10])
                pvarpLabel.set(write[11])
                rsLabel.set(write[12])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 600)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 600)


