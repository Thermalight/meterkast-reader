import serial

# environment variables can be set in .env file by using the following format:
# VARIABLE_NAME=VARIABLE_VALUE
# example:
# port=/tes/tport123
# baudrate=123456

# # read all environment variables from .env file
environment_variables = {}
with open('.env') as f:
    for line in f:
        if line[0] != '#':
            key, value = line.split('=')
            environment_variables[key] = value.strip()
            
class Reader:
    port = None
    baudrate = None
    ser = None
    
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate)

    # read a full datastream from the serial port
    def read(self):
        started = False
        ended = False
        data = []
        
        while not started and not ended:
            line = self.ser.readline().decode().strip()
            
            if line.startswith('/'):
                started = True
            elif line.startswith('!'):
                ended = True
            else:
                # filter out empty lines
                if line != '':
                    data.append(line)
                
        return data