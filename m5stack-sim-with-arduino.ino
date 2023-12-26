// analog-plot
// 
// Read analog values from A0 and A1 and print them to serial port.
//
// electronut.in
#include "Arduino.h"
 
void setup()
{
  // initialize serial comms
  Serial.begin(19200); 
}

int i=0;
float x;
float pi=3.1415927;
float ttime=0.0;

void loop()
{
  if (i==99) i=0;
  x=pi*float(i)/50.0;
  float val1 = (50)*abs(sin(x));
  float val2 = (50)*abs(sin(pi/9.0+x));
  float val3 = (50)*abs(sin(2*pi/9.0+x));
  float val4 = (50)*abs(sin(3.0*pi/9.0+x));
  float val5 = (50)*abs(sin(4.0*pi/9.0+x));
  float val6 = (75)*abs(sin(5.0*pi/9.0+x));
  float val7 = (80)*abs(sin(2.0*pi/3.0+x));
  float val8 = (70)*abs(sin(7.0*pi/9.0+x));
  float val9 = (10)*abs(sin(8.0*pi/9.0+x));
  float val10 = random(10)*abs(sin(x))+1.0;
  i=i+1;
// print to serial
  Serial.print("YYYY:MM:DD:hh:mm:ss.ss,");
  Serial.print(ttime);
  Serial.print(",");
  Serial.print(val1);
  Serial.print(",");
  Serial.print(val2);
  Serial.print(",");
  Serial.print(val3);
  Serial.print(",");
  Serial.print(val4);
  Serial.print(",");
  Serial.print(val5);
  Serial.print(",");
  Serial.print(val6);
  Serial.print(",");
  Serial.print(val7);
  Serial.print(",");
  Serial.print(val8);
  Serial.print(",");
  Serial.print(val9);
  Serial.print(",");
  Serial.print(val10);
  Serial.print("\n");
  ttime=ttime+0.1; 
  delay(100);
}
