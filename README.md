# Elektro - Data PYSualization

- Language: Python 3
- Main Modules: PySerial, PyQt5, pyqtgraph, numpy, scipy.signal, scipy.fft  

&nbsp;  

### Progress (28 March 2021) :
![image](https://user-images.githubusercontent.com/55247343/112740133-a32d5e00-8fa4-11eb-9978-13330dc8b172.png)  

- Created ```Figure()``` class, you can pass in the plot title, plot color (default red), or y-axis range (default -2 , 6)
- Each Figure object only contains 1 plotted line to avoid confusion while looking at the live plotted data
- Figure object has a method ```PlotData()``` to update the data, parameter: (x_data, y_data)
- The Figure x-axis will automatically adjust to the x_data passed into the ```PlotData()``` method, if you want static x-axis, pass in:
```py
import numpy as np

y_data = # wherever you want to grab the data from
x_data = np.arange(0, np.size(y_data))
```
  
&nbsp;
### Progress (25 May 2021) :

- Now user can plot data using 2 ways: TCP socket or Serial at 230400 baud.
- Maximum throughput of TCP: 40 data / s
- Maximum throughput of serial: 400 data / s @230400 baud, 200 data / s @115200 baud
- Added frequency domain plot for serial only, since there's no frequency that is
interesting to look at < 40 Hz for TCP througput.

&nbsp;  
#### How to use Serial Plotter:
- Open the arduino sketch "DataLogger.ino" using ArduinoIDE and upload it to your
Arduino Board
- Change the PORT from "main_SerialVersion.py" to suit your Arduino PORT.
- Run the "main_SerialVersion.py" python script.
- If you still have any issues, either check the BAUDRATE, PORT.
- Tested on Linux Pop-OS 20.04

&nbsp;  
#### Pictures:  
![image](https://user-images.githubusercontent.com/55247343/119500799-63130d80-bd92-11eb-8fc5-7e7ec7322045.png)  
