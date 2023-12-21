import matplotlib.pyplot as plt
import serial
import sys

from read_m5_class import m5logger

data0=[0]*10
data=[data0]*100

ser = serial.Serial(sys.argv[2],sys.argv[1])
sport=m5logger()

if len(sys.argv)<4:
  fn="test.csv"
else:
  fn=sys.argv[3]
f=open(fn,'w',encoding="utf-8")

while True:
  try:
    array=sport.read_logger(ser)
    if len(array)==10:
      data.pop(-1)
      data.insert(0,array)
      rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
      x=range(0, 100, 1)
      plt.clf()
      plt.ylim(0,60)
      line1,=plt.plot(x,rez[0],label="L1")
      line2,=plt.plot(x,rez[1],label="L2")
      line3,=plt.plot(x,rez[2],label="L3")
      line4,=plt.plot(x,rez[3],label="L4")
      line5,=plt.plot(x,rez[4],label="L5")
      line6,=plt.plot(x,rez[5],label="L6")
      line7,=plt.plot(x,rez[6],label="L7")
      line8,=plt.plot(x,rez[7],label="L8")
      line9,=plt.plot(x,rez[8],label="9")
      line10,=plt.plot(x,rez[9],label="L10")
      plt.legend(handles=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10])
      plt.pause(0.1)
      if len(array)==10:
        strg=str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9])
        f.write(strg+"\n")
      else:
        f.write(str(array)+"\n")
  except KeyboardInterrupt:
    print ('exiting')
    f.close()
    break
ser.close()
f.close()
exit()
