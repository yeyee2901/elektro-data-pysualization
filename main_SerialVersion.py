#!/usr/bin/python3

'''
Change-able:
- PORT: specify the communication port
- BAUDRATE: specify the data rate, default is 115200 for max logging rate
- FIRST_MESSAGE: used to detect the first valid message. This is needed because
                 in UART, the first few datas received will be garbage values.
                 You can change this, but don't forget to change what's in
                 the Arduino sketch too
- DATA_LENGTH: display of how many datas in the graph. default is 2048 samples
- Y_LIMIT: Y-axis limit
'''

# SERIAL VERSION
# User Module ---------------------------------------------
from FigureWidget import *
from ChannelWidget import *
from SerialPort import *


# Pre defined Module --------------------------------------
from sys import exit, argv
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtCore import QTimer
import scipy.fft as FFTmodule
import serial
import time


# GLOBAL VARS ---------------------------------------------
PORT = "/dev/ttyACM0"
BAUDRATE = 230400
SAMPLE_RATE = 400
SAMPLE_INTERVAL = 1 / SAMPLE_RATE
FIRST_MESSAGE = "Test"
DATA_LENGTH = 2 ** 11
Y_LIMIT = [-1, 5]


# MAIN CLASS ----------------------------------------------

class WindowUtama(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__serverSuccessFlag = False
        self.__firstmessagefound = False
        self.__printfirstmessage = False
        self.pause = False
        self.count = 0
        self.x_data = np.arange(DATA_LENGTH)
        self.freqs = FFTmodule.fftfreq(DATA_LENGTH, SAMPLE_INTERVAL)[:DATA_LENGTH//2]
        self.magnitude = [0] * len(self.freqs)
        self.y_data = [0] * np.size(self.x_data)

        self.initServer()

        if self.__serverSuccessFlag:
            print(f"Server at {PORT}, {BAUDRATE} bps")
            self.initUi()
            self.resize(1000, 700)
            self.show()
            self.setTimer()
        else:
            exit(1)

    def initServer(self):
        self.UART = SerialPort(PORT, BAUDRATE)
        if self.UART.SUCCESS_OPEN:
            self.__serverSuccessFlag = True
        else:
            self.__serverSuccessFlag = False

    def initUi(self):
        self.setWindowTitle("Elektro - (Serial) Data Pysualization")

        # config main widget
        self.MainWidget = QWidget()
        self.MainWidgetLayout = QGridLayout()
        self.MainWidget.setLayout(self.MainWidgetLayout)

        # place the main widget in main window
        self.setCentralWidget(self.MainWidget)

        # INIT PLOTS -------------------------------------------------
        self.List_of_Plots = []
        self.TimePlot = FigureWidget(title=f"Time Domain", color=20, yRange=Y_LIMIT)
        self.FreqPlot = FigureWidget(title=f"Frequency Domain", color=40, yRange=[-20, 120])
        self.List_of_Plots.append(self.TimePlot)
        self.List_of_Plots.append(self.FreqPlot)

        # INIT CHANNEL INFO ------------------------------------------
        self.List_of_channels = []
        #for n in range(2):
        #    self.channel_n = ChannelWidget(title="Channel", num=n+1)
        #    self.List_of_channels.append(self.channel_n)


        # ADD WIDGETS TO LAYOUT --------------------------------------
        self.MainWidgetLayout.addWidget(self.List_of_Plots[0], 0, 0)
        self.MainWidgetLayout.addWidget(self.List_of_Plots[1], 1, 0)

        #self.MainWidgetLayout.addWidget(self.List_of_channels[0], 0, 2)
        #self.MainWidgetLayout.addWidget(self.List_of_channels[1], 1, 2)
        
    
    def setTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateAll)
        self.timer.start(0)
    
    def updateAll(self):
        #self.start_time = time.time()

        try:
            data = self.UART.getNewData()
            if data.find(FIRST_MESSAGE):
                self.__firstmessagefound = True
                if not self.__printfirstmessage:
                    print("Found first message!")
                    self.__printfirstmessage = True

            if self.__firstmessagefound:
                data = float(data) * 5 / 1024
                self.y_data.append(data)
                self.y_data.pop(0)

                self.magnitude = FFTmodule.fft(self.y_data)
                self.magnitude = 20 * np.log(np.abs(self.magnitude[:DATA_LENGTH//2]))

                if not self.pause:
                    self.List_of_Plots[0].PlotData(self.x_data, self.y_data)
                    self.List_of_Plots[1].PlotData(self.freqs, self.magnitude)

                else:
                    print("Paused!")


        except KeyboardInterrupt:
            print("\nKeyboard Interrupted!")
            try:
                self.UART.close()
            except:
                print("Serial port already closed")
            exit(1)

        except ValueError:
            pass


if __name__ == '__main__':
    app = QApplication(argv)

    main = WindowUtama()

    exit(app.exec_())
