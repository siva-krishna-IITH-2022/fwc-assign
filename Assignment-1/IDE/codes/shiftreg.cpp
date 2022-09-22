#include <Arduino.h>
int x;
int D1=1,D2=0,D3=1,D4=1;
void setup() {
  pinMode(13,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
}
void disp(int x){
	digitalWrite(2,x);
	digitalWrite(13,1);
	delay(3000);
	digitalWrite(13,0);
	delay(3000);
}
void loop(){
disp(D4);
disp(D3);
disp(D2);
disp(D1);
disp(0);
disp(0);
disp(0);
disp(0);

}

