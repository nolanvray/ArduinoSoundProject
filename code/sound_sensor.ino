/*
Code to collect sound data through an Arduino.

The red led will turn on when detected sound is above the set threshold,
otherwise the green led will be on. 
These leds function more for fun, both leds and threshold can be omitted without consequence.
*/

const int led1=11; //red led
const int led2=9;  //green led
const int soundpin=A2; 
const int threshold=208;// Threshold can be set to what works for you, I found that 208 worked best for my debugging purposes. 
bool label= true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(soundpin, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int soundsens=analogRead(soundpin);
   
    if(soundsens>=threshold){
      Serial.println(soundsens);
      digitalWrite(led1, HIGH); //Controls led functioning. Same with lines 31, 36, & 37
      digitalWrite(led2, LOW);
      delay(1000);
    }
    else{
      Serial.println(soundsens);
      digitalWrite(led2, HIGH);
      digitalWrite(led1, LOW);
      delay(1000);
    }
  
}
