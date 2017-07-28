//////////////////////////////////
// LASERQUEST 4.2.15, 17.10.15 ///
//     mongoq@hotmail.com      ///
//////////////////////////////////

#include <Servo.h>

int servox_pos = 0;
int servoy_pos = 0;
int laser_state = 0;

char character;
char svx[4]="60"; //Initial position
char svy[4]="65";  // "         "
char l;
int idx_a = 0;
int idx_b = 0;

Servo servox;
Servo servoy;

void setup() {
  servox.attach(2); // Servo X
  servoy.attach(3); // Servo Y
  pinMode(4, OUTPUT); // Laser

//  while (Serial.available()<0){
//    __asm__("nop\n\t");    
//  }
  
  Serial.begin(9600);
  Serial.println("Booting Laserquest ...");
  Serial.println("Usage: x,y,l;\n");
  
  Serial.setTimeout(360000);
  //memset(svx, 0, 4);
  //memset(svy, 0, 4);
}

void set_servox(int x) {
  servox.write(x);
}

void set_servoy(int y) {
  servoy.write(y);
}

void set_laser(bool l) {
  digitalWrite(4, l);
}

void loop() {

  idx_a = 0;
  idx_b = 0;

  String command="";

  while (Serial.available()){
    command = Serial.readStringUntil(';');
  }
  command+=";"; 

  for (int i=0;i<=command.length();i++)
  {
      character=command[i];   
      if (((character > 47) && (character < 58)) && (idx_a == 0)) {
        svx[idx_b++] = character;
      }
      else if (((character > 47) && (character < 58)) && (idx_a == 1)) {
        svy[idx_b++] = character;
      }
      else if (((character == '0') || (character == '1')) && (idx_a == 2)) {
        l = character;
      }
      else if (character == ',') {
        idx_a++;
        idx_b = 0;
      }
        if (atoi(svx) > 180) svx[2]=' ';
        if (atoi(svy) > 180) svy[2]=' ';
        if ((atoi(svx) >= 0) && (atoi(svx) <= 180)) servox_pos = atoi(svx); 
        if ((atoi(svy) >= 0) && (atoi(svy) <= 100)) servoy_pos = atoi(svy);
        if (l == '0') laser_state = 0;
        else if (l == '1') laser_state = 1;
  }
  Serial.println("Status: " + String(servox_pos) + " " +  String(servoy_pos) + " " + String(laser_state));

  set_servox(servox_pos);
  set_servoy(servoy_pos);
  set_laser(laser_state);
  
  /*  for(servo1_pos = 60; servo1_pos <= 180; servo1_pos += 1) // goes from 0 degrees to 180 degrees
    {                                  // in steps of 1 degree
      set_servo1(servo1_pos);              // tell servo to go to position in variable 'pos'
      delay(500);                       // waits 15ms for the servo to reach the position
    }
    for(servo1_pos = 180; servo1_pos>=0; servo1_pos-=1)     // goes from 180 degrees to 0 degrees
    {
      set_servo1(servo1_pos);              // tell servo to go to position in variable 'pos'
      delay(500);                       // waits 15ms for the servo to reach the position
    }
  */
}



