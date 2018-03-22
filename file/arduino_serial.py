import serial
import time


s=serial.Serial('/dev/ttyACM0', 9600,timeout=5)
time.sleep(5) # wait a couple seconds
l = ['hello','this','is','stan','bye']
for i in range(5) :
    a = l[i].encode('ascii')
    s.write(a)
    c = s.readline()
    print(c.decode('utf-8'))

s.close()
