// 4 Legger Gait and Pose
// by Daniel Wirick

#include <Servo.h>
 
Servo leg1_hip;  //servo instances
Servo leg1_knee;
Servo leg2_hip;
Servo leg2_knee;
Servo leg3_hip;
Servo leg3_knee;
Servo leg4_hip;
Servo leg4_knee;
 
void setup()
{
  Serial.begin (115200);
  while (!Serial){;} //Wait for serial port to connect.
  intro();
  //Reconfigure as needed
  leg1_hip.attach(12);  //connects each servo to a digital pin
  leg1_knee.attach(11);
  leg2_hip.attach(10);
  leg2_knee.attach(9);
  leg3_hip.attach(8);
  leg3_knee.attach(7);
  leg4_hip.attach(6);
  leg4_knee.attach(5);
  
  leg1_hip.write(90);
  leg1_knee.write(90);
  leg2_hip.write(90);
  leg2_knee.write(90);
  leg3_hip.write(90);
  leg3_knee.write(90);
  leg4_hip.write(90);
  leg4_knee.write(90);
}
 
void loop()
{
  //servo write can be between 0 and 180
  //set all servos to center
  if (Serial.available () > 0) {
    int commandByte = Serial.read ();
    if (commandByte == 's'){
      leg1_hip.write(Serial.parseInt());
      leg1_knee.write(Serial.parseInt());
      leg2_hip.write(Serial.parseInt());
      leg2_knee.write(Serial.parseInt());
      leg3_hip.write(Serial.parseInt());
      leg3_knee.write(Serial.parseInt());
      leg4_hip.write(Serial.parseInt());
      leg4_knee.write(Serial.parseInt());
      Serial.println ("Servos Set");
      //delay(15);                           // waits for the servo to get there
    }
  }
  waitForCommand ();
}

void intro ()
{
    byte i = 4;
    if (Serial.available () <=0)
    {
        Serial.print ("Booting ");
    }
    while (Serial.available () <= 0 && i > 0)
    {
        Serial.print ("...");
        delay (500);
        i = i-1;
    }
    if (Serial.available() <= 0) 
    {
       delay (2000);
       Serial.println ("");
       Serial.println ("4 Legged Robot v0.2");
       Serial.println ("Written by Daniel Wirick 9-28-14");
       Serial.println ("To set servo position, send csv file in the format:");
       Serial.println ("s,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8");
       
    }
}

void waitForCommand ()
{
   byte i = 1;
   while (Serial.available () <= 0)
   {
       if (i > 0)
       {
           Serial.println ("Waiting for Command");
           i = i-1;
       }
       delay (100);
   }
}
