import serial
import struct

def checkConnect():
    try:
        ser = serial.Serial(port="COM3", baudrate=115200)
        return 3
    except:
        try:
            ser = serial.Serial(port="COM5", baudrate=115200)
            return 5
        except:
            try:
                ser = serial.Serial(port="COM4", baudrate=115200)
                return 4
            except:
                return 6
