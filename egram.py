import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation
from checkConnect import checkConnect 
import serial
import struct

def egram(mode=7,Lower_Rate=60, MSR=120, AV_Delay=100, ATR_Amplitude=75, VENT_Amplitude=75, ATR_Width=10,VENT_Width=10,VENT_Refractory=250, ATR_Refractory=250, Activity_Threshold=1.1 ,Reaction_Time=5, Response_Factor=100,Recovery_Time=5):
    global atr
    global vent
    global t
    global x
    global com
    com = checkConnect()
    error = 0

    font = {'size'   : 9}
    matplotlib.rc('font', **font)


    f0 = figure(num = 0, figsize = (12, 8))
    f0.suptitle("Electrogram", fontsize=18)
    ax01 = subplot2grid((2, 2), (0, 0), rowspan = 1, colspan = 2)
    ax02 = subplot2grid((2, 2), (1, 0), rowspan = 1, colspan = 2)

    ax01.set_title('Atrium Signals', y = 1.0, pad = -14, fontsize = 14)
    ax02.set_title('Ventricle Signals', y = 1.0, pad = -14, fontsize = 14)

    ax01.set_ylim(0.30,0.70)
    ax02.set_ylim(0.30,0.70)

    ax01.set_xlim(0,4000)
    ax02.set_xlim(0,4000)

    ax01.set_xlabel("Time (ms)", fontsize = 10)
    ax01.set_ylabel("Voltage (mV)", fontsize = 10)
    ax02.set_xlabel("Time (ms)", fontsize = 10)
    ax02.set_ylabel("Voltage (mV)", fontsize = 10)

    atr=zeros(0)
    vent=zeros(0)
    t=zeros(0)

    p01, = ax01.plot(t,atr,'b-', label="Atrium")
    p02, = ax02.plot(t,vent,'b-', label="Ventricle")

    xmin = 0.0
    xmax = 4000
    x = 0.0
    #ser = serial.Serial(port="COM5", baudrate=115200)
    #spk = struct.pack('<3B10H1d2H',0x16,0x22,mode,Lower_Rate,ATR_Amplitude,VENT_Amplitude,ATR_Width,VENT_Width,
                      #ATR_Refractory,VENT_Refractory,MSR,Reaction_Time,
                      #Recovery_Time,Activity_Threshold,AV_Delay,Response_Factor)
    #ser.write(spk)
    #ser.close()

    def updateData(self):
        global atr
        global vent
        global t
        global x

        if com== 3:
            ser = serial.Serial(port="COM3", baudrate=115200)
        elif com == 4:
            ser = serial.Serial(port="COM4", baudrate=115200)
        elif com == 5:
            ser = serial.Serial(port="COM5", baudrate=115200)

        spk = struct.pack('<3B10H1d2H',0x16,0x22,mode,Lower_Rate,ATR_Amplitude,VENT_Amplitude,ATR_Width,VENT_Width,
                      ATR_Refractory,VENT_Refractory,MSR,Reaction_Time,
                      Recovery_Time,Activity_Threshold,AV_Delay,Response_Factor)
        ser.write(spk)
        ser.close()
        if com== 3:
            ser = serial.Serial(port="COM3", baudrate=115200)
        elif com == 4:
            ser = serial.Serial(port="COM4", baudrate=115200)
        elif com== 5:
            ser = serial.Serial(port="COM5", baudrate=115200)

        serialdata=ser.read(49)
        VSIGN=struct.unpack('d',serialdata[33:41])
        ASIGN=struct.unpack('d',serialdata[41:49])
        ser.close()

        atrLine = ASIGN[0]
        ventLine = VSIGN[0]
        print(3000*(VSIGN[0]-0.499))
        print(3000*(ASIGN[0]-0.499))

        atr = append(atr, atrLine)
        vent = append(vent, ventLine)
        t = append(t,x)

        x+=10

        p01.set_data(t,atr)
        p02.set_data(t,vent)

        if x >= xmax-200:
            p01.axes.set_xlim(x-xmax+200,x+200)
            p02.axes.set_xlim(x-xmax+200,x+200)

        return p01,p02

    simulation = animation.FuncAnimation(f0, updateData, blit = False, frames = 10000, interval = 10, repeat = False)
    plt.show()

        

#if __name__ == '__main__':
    #egram()
