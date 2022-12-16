import serial.tools.list_ports
from time import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print('\nSelected Port:')
        print(portList[x])
        print(f'Colecting data from {portVar}...\n')
    else:
        print('Access Denied')

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

t_wait = 10

RPM = []

# 1135133 = 201 dados coletados, faça uma regra de 3 para saber quual o numero que deve ser colocado em stop
stop = 1135133; start = 0

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n'))
        RPM.append(packet)
    start += 1