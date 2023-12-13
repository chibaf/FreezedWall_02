import serial, sys

strPort = sys.argv[1]

ser=serial.Serial(strPort, sys.argv[2])

print("connected to: " + ser.portstr)

while True:
  line = ser.readline()
  line2=line.decode('utf-8')
  print(line2)
