# # Testing Purpose --------------------------------
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from sys import exit, argv
# # Testing Purpose --------------------------------

# Modules ---------------------------------------- 
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt as QtCoreQtClass

class ChannelWidget(QWidget):

    def __init__(self, title="CHANNEL", num=0):
        super().__init__()
        self.title = f'<h3> {title} {num}</h3>'
        
        self.initUi()

    
    def initUi(self):

        # Configure Layout
        self.layout_model = QGridLayout()
        self.setLayout( self.layout_model )

        # Figure title is 1x3 (row x col) excel cell
        self.TITLE = QLabel(text=self.title)
        #self.TITLE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.TITLE.setAlignment(QtCoreQtClass.AlignCenter)
        self.layout_model.addWidget(self.TITLE, 0, 0, 1, 2)

        # Max Voltage
        self.max_voltage = QLabel(text="<h4>Max Volt.</h4>")
        self.max_voltage_num = QLabel(" V")
        self.layout_model.addWidget(self.max_voltage, 1, 0)
        self.layout_model.addWidget(self.max_voltage_num, 1, 1, 1, 2)

        # Min Voltage
        self.min_voltage = QLabel(text="<h4>Min Volt.</h4>")
        self.min_voltage_num = QLabel(" V")
        self.layout_model.addWidget(self.min_voltage, 2, 0, 1, 1)
        self.layout_model.addWidget(self.min_voltage_num, 2, 1, 1, 2)
        
        # Average Voltage
        self.avg_voltage = QLabel(text="<h4>Avg Volt.</h4>")
        self.avg_voltage_num = QLabel(" V")
        self.layout_model.addWidget(self.avg_voltage, 3, 0, 1, 1)
        self.layout_model.addWidget(self.avg_voltage_num, 3, 1)


if __name__ == '__main__':
    app = QApplication(argv)

    try_channel_widget = ChannelWidget()
    try_channel_widget.show()


    exit(app.exec_())
