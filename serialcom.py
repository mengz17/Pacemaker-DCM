import serial
import struct
import tkinter.messagebox
from checkConnect import checkConnect


def writePara(mode=6, Lower_Rate=60, MSR=120, AV_Delay=100, ATR_Amplitude=70, VENT_Amplitude=75, ATR_Width=1,VENT_Width=2,VENT_Refractory=350, ATR_Refractory=250, Activity_Threshold=1.7,Reaction_Time=5, Response_Factor=1000,Recovery_Time=5):
    if checkConnect() == 3:
        ser = serial.Serial(port="COM3", baudrate=115200)
    elif checkConnect() == 4:
        ser = serial.Serial(port="COM4", baudrate=115200)
    elif checkConnect() == 5:
        ser = serial.Serial(port="COM5", baudrate=115200)
    Header = '<3B10H1d2H'
    Buffer1 = 40
    spk = struct.pack(Header,0x16,0x55,mode,Lower_Rate,ATR_Amplitude,VENT_Amplitude,ATR_Width,VENT_Width,
                      ATR_Refractory,VENT_Refractory,MSR,Reaction_Time,
                      Recovery_Time,Activity_Threshold,AV_Delay,Response_Factor)
    ser.write(spk)
    serialdata=ser.read(49)
    modeV=serialdata[0]
    LRLV=struct.unpack('H',serialdata[1:3])
    ATR_AMPV=struct.unpack('H',serialdata[3:5])
    VENT_AMPV=struct.unpack('H',serialdata[5:7])
    A_WidthV=struct.unpack('H',serialdata[7:9])
    V_WidthV=struct.unpack('H',serialdata[9:11])
    VRPV=struct.unpack('H',serialdata[11:13])
    ARPV=struct.unpack('H',serialdata[13:15])
    MSRV=struct.unpack('H',serialdata[15:17])
    ReactionTV=struct.unpack('H',serialdata[17:19])
    RecoveryTV=struct.unpack('H',serialdata[19:21])
    ThresholdV=struct.unpack('d',serialdata[21:29])
    AVdV=struct.unpack('H',serialdata[29:31])
    RCV=struct.unpack('H',serialdata[31:33])
    print(LRLV[0])
    if ((modeV==mode)&(LRLV[0]==Lower_Rate)&(ATR_AMPV[0]==ATR_Amplitude)&(VENT_AMPV[0]==VENT_Amplitude)
        &(A_WidthV[0]==ATR_Width)&(V_WidthV[0]==VENT_Width)&(VRPV[0]==VENT_Refractory)&(ARPV[0]==ATR_Refractory)
        &(MSRV[0]==MSR)&(ReactionTV[0]==Reaction_Time)&(RecoveryTV[0]==Recovery_Time)&(ThresholdV[0]==Activity_Threshold)
        &(AVdV[0]==AV_Delay)&(RCV[0]==Response_Factor)):

        ve=1
        tkinter.messagebox.showinfo('Great','Parameters all set')
    else:

        ve=2
        tkinter.messagebox.showwarning('Pleas Note','Parameters have been sent, however some/all parameters in Pacemaker do not match with DCM')

    VSIGN=struct.unpack('d',serialdata[33:41])
    ASIGN=struct.unpack('d',serialdata[41:49])
    print(VSIGN[0])
    print(ASIGN[0])
    ser.close()

if __name__ == '__main__':
    writePara()
    #egram()
