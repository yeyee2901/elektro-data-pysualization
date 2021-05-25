/*
Change able:
- SAMPLE_RATE: defines how fast we sample using ADC
- BAUD_RATE: defines the speed of logging to server

For now, i measured 200 Dps using 115200 baudrate, for a single
data, and 400 Dps using 230400 baudrate for single data. This means,
if you want to log 2 kinds of data at a rate of 200 Dps, you have to use
230400 baudrate.

How to use:
- upload the sketch to your Arduino
- Execute "main_SerialVersion"
- Happy logging!

Additional notes:
- If the server is closed, the Arduino will still continue to send datas
- If the Arduino is disconnected while the server is still running, the
API will close immediately.
- If you reset the Arduino, the API will not close, and can still
continue to plot & display the data, unless your Arduino
takes too long (>1s) to initialize itself after restarting. You can
change this TIMEOUT setting in the API


*/

// max data rate is:
// if BAUDRATE 230400, max data rate = 400
// if BAUDRATE 115200, max data rate = 200
#define MAX_DATA_RATE  3000
#define SAMPLE_RATE    400
#define BAUD_RATE      230400

long int SAMPLING_INTERVAL = 1000000 / SAMPLE_RATE;


void setup()
{
  if(SAMPLE_RATE > MAX_DATA_RATE)
  {
    SAMPLING_INTERVAL = 1000000 / MAX_DATA_RATE;
  }
  
  Serial.begin(BAUD_RATE);
  
  while(!Serial) delay(500);
  
  Serial.println("Test");  
}

void loop()
{
 
  //unsigned long int tic = micros();
  //Serial.print(analogRead(A0)); Serial.print(",");
  //unsigned long int toc = micros();
  //Serial.println(toc - tic);
  
  Serial.println(analogRead(A0));
 
  unsigned long int lastTime = micros();
  
  while(micros() - lastTime < SAMPLING_INTERVAL); 
}
