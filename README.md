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
