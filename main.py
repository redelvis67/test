import serial
import time
ser=serial.Serial(port='COM3',baudrate=9600)
ser.close()

ser.open()
while True:
    print("try")
    time.sleep(10) # делей для конченных, но мне было лень писать прерывание.
    s=ser.read(100) # по 100 байт
    print(s)
ser.close( )