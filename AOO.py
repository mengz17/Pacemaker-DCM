import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from serialcom import writePara
from checkConnect import checkConnect

def AOO_window(upper_tk=None):

    global root_AOO
    global lrlLabel
    global urlLabel
    global aaLabel
    global apwLabel

    global connectLable

    index = 0
    
    try:
        with open("parameterAOO.txt","r") as parameterFile:
                read = parameterFile.readlines()

    except FileNotFoundError:
        with open("parameterAOO.txt","w") as parameterFile:
                while(index < 4):
                        parameterFile.write("N/A\n")
                        index += 1
                index = 0
        with open("parameterAOO.txt","r") as parameterFile:
            read = parameterFile.readlines()

    #if upper_tk == None:
     #   root_AOO = tk.Tk()
    #else:
    root_AOO = tk.Toplevel()
    root_AOO.title('AOO')
    root_AOO.geometry('500x400')

    label = tk.Label(root_AOO, text="Current Mode:   AOO",font=("Times New Roman",14)).place(x=10,y=10)
    

    label = tk.Label(root_AOO, text="Lower Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=80)
    label = tk.Label(root_AOO, text="Upper Rate Limit (ppm):", font=("Times New Roman",14)).place(x=10,y=130)
    label = tk.Label(root_AOO, text="Atrial Amplitude (V):", font=("Times New Roman",14)).place(x=10,y=180)
    label = tk.Label(root_AOO, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=230)

    connectLable = tk.StringVar()
    if checkConnect() == 6:
        connectLable.set("No Pacemaker Connected")
        label = tk.Label(root_AOO, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
    else:
        connectLable.set("Pacemaker is Connected")
        label = tk.Label(root_AOO, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
    
    lrlLabel = tk.StringVar()
    lrlLabel.set(read[0].strip("\n")) #lrlValue is input from user
    label = tk.Label(root_AOO, textvariable = lrlLabel, font=("Times New Roman",14)).place(x = 220, y = 80)

    urlLabel = tk.StringVar()
    urlLabel.set(read[1].strip("\n")) #urlValue is input from user
    label = tk.Label(root_AOO, textvariable = urlLabel, font=("Times New Roman",14)).place(x = 220, y = 130)

    aaLabel = tk.StringVar()
    aaLabel.set(read[2].strip("\n")) #aaValue is input from user
    label = tk.Label(root_AOO, textvariable = aaLabel, font=("Times New Roman",14)).place(x = 220, y = 180)

    apwLabel = tk.StringVar()
    apwLabel.set(read[3].strip("\n")) #apwValue is input from user
    label = tk.Label(root_AOO, textvariable = apwLabel, font=("Times New Roman",14)).place(x = 220, y = 230)


    #modeWindowButton = tk.Button(root_AOO, text = "Change Mode", command = lambda:[root_AOO.destroy()], width = 13).place(x = 300, y = 10)
    paraWindowButton = tk.Button(root_AOO, text = "Change Parameter", command = AOO_ParameterWindow, width = 20, height = 2).place(x = 200, y = 300)


def AOO_ParameterWindow():

    with open("parameterAOO.txt","r") as parameterFile:
        aooRead = parameterFile.readlines()


    global paraWindow
    
    paraWindow = tk.Toplevel()
    paraWindow.title('AOO Parameter Setting')
    paraWindow.geometry('500x400')
    label = tk.Label(paraWindow, text="Current Mode   AOO",font=("Times New Roman",14)).place(x=10,y=10)

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
    if aooRead[0]!='N/A\n':  #Secret
        LRL_roll.set(aooRead[0].strip("\n"))
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
    if aooRead[1]!='N/A\n':
        URL_roll.set(aooRead[1].strip("\n"))
    else:
        URL_roll.current(0)


    label = tk.Label(paraWindow, text="Atrial Amplitude (V):",font=("Times New Roman",14)).place(x=10,y=180)
    AA_data = ['OFF']
    for a in range (1,51):
        AA_data.append(float(a/10))

    AA_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    AA_roll['values'] = AA_data
    AA_roll.place(x=250, y=180)
    if aooRead[2]!='N/A\n':
        AA_roll.set(aooRead[2].strip("\n"))
    else:
        AA_roll.current(0)

    label = tk.Label(paraWindow, text="Atrial Pulse Width (ms):", font=("Times New Roman",14)).place(x=10,y=230)
    APW_data = []
    for c in range (1,31):
        APW_data.append(c)

    APW_roll = ttk.Combobox(paraWindow, width=15, height=10, state='readonly')
    APW_roll['values'] = APW_data
    APW_roll.place(x=250, y=230)
    if aooRead[3]!='N/A\n':
        APW_roll.set(aooRead[3].strip("\n"))
    else:
        APW_roll.current(0)

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
            write[2] = AA_roll.get()
            aoo_aa_p = AA_roll.get()
            if aoo_aa_p == 'OFF':
                aoo_aa_p = 0;
            else:
                aoo_aa_p = int(100*float(aoo_aa_p))
            write[3] = APW_roll.get()

            if checkConnect() == 6:
                connectLable.set("No Pacemaker Connected")
                label = tk.Label(root_AOO, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "red").place(x=10,y=40)
                tkinter.messagebox.showerror('Error','Failed to connect to the Pacemaker')
            else:
                connectLable.set("Pacemaker is Connected")
                label = tk.Label(root_AOO, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
                label = tk.Label(paraWindow, textvariable = connectLable, font=("Times New Roman",14), fg = "green").place(x=10,y=40)
            
                writePara(mode = 1, Lower_Rate=int(LRL_roll.get()), ATR_Amplitude=int(aoo_aa_p), ATR_Width=int(APW_roll.get()))


                with open("parameterAOO.txt","w") as parameterFile:
                    while (d < 4):
                        parameterFile.write(write[d]+"\n") #Write every index of list write[] into file
                        d += 1
                    d = 0

                lrlLabel.set(write[0])
                urlLabel.set(write[1])
                aaLabel.set(write[2])
                apwLabel.set(write[3])
                paraWindow.destroy()
        
        


    saveButton = tk.Button(paraWindow, text = "Save", command = changePara, width = 13).place(x = 50, y = 300)
    cancelButton = tk.Button(paraWindow, text = "Cancel", command = lambda:[paraWindow.destroy()], width = 13).place(x = 220, y = 300)

#AOO_window()
