# User Module ---------------------------------------------
from FigureWidget import *
from ChannelWidget import *

# Pre defined Module --------------------------------------
from sys import exit, argv
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtCore import QTimer
import serial
# import time


class WindowUtama(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initSerial()
        self.initUi()
        self.showMaximized()
        self.setTimer()

    def initSerial(self):
        pass

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
        for n in range(4):
            self.plot_n = FigureWidget(title=f"Figure {n+1}", color=20*n)
            self.List_of_Plots.append(self.plot_n)

        # INIT CHANNEL INFO ------------------------------------------


        # ADD WIDGETS TO LAYOUT --------------------------------------
        self.MainWidgetLayout.addWidget(self.List_of_Plots[0], 0, 0)
        self.MainWidgetLayout.addWidget(self.List_of_Plots[1], 0, 1)
        self.MainWidgetLayout.addWidget(self.List_of_Plots[2], 1, 0)
        self.MainWidgetLayout.addWidget(self.List_of_Plots[3], 1, 1)
        
    
    def setTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateAll)
        self.timer.start(0)
    
    def updateAll(self):
        self.x_data = np.arange(0, 2, 1/10000)
        self.y_data = np.random.normal(loc=2.0, size=np.size(self.x_data))

        for plot_n in self.List_of_Plots:
            plot_n.PlotData(self.x_data, self.y_data)


if __name__ == '__main__':
    app = QApplication(argv)

    main = WindowUtama()

    exit(app.exec_())