import serial as ser

PORT = "/dev/ttyACM0"
BAUDRATE = 230400
TIMEOUT = 1

class SerialPort:

    def __init__(self, PORT="/dev/ttyACM0", BAUD=9600, timeout_secs=TIMEOUT):
        self.SUCCESS_OPEN = False
        try:
            self.serialObj = ser.Serial(PORT, BAUD, timeout=timeout_secs)
            self.SUCCESS_OPEN = True

        except ser.SerialException as e:
            print("Cannot open serial port, try again")
            print(f"Cause: {e}")

        self.x_data_buffer = None
        self.y_data_buffer = None

    def getNewData(self):
        try:
            data = str(self.serialObj.readline()).strip("b''")
            data = data[0 : data.find("\\")]
            return data

        except:
            exit(1)



if __name__ == '__main__':
    UART = SerialPort(PORT, BAUDRATE)
    flagFound = False

    if UART.SUCCESS_OPEN:
        print("Serial port successfully open!")
        print(f"{PORT}, {BAUDRATE} bps")
    
    while True:
        data = UART.getNewData()
        if data.find("Test", 0):
            flagFound = True

        if flagFound:
            print(data)
