import serial
import time


s=serial.Serial("/dev/ttyACM0", 9600, timeout=5)

time.sleep(5) # wait a couple seconds

while True :
	a = input("please:\n")
	if a=='stop' :
		s.write(b'0')
		break
	else :
		a = a.encode('utf-8')
		s.write(a)
s.close()
