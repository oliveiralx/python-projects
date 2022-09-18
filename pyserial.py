import serial.tools.list_ports

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

"""
 -> A sugestion is find a way to better make sure if the user choose 
    a wrong COM the program will return and ask again for the user 
    about the right COM. The changes can be in the lines 14-19.

 -> Maybe that'll be possible to solve the problem using a while condition.
    If while the user don't choose a available COM, the program
    will return to the begin and ask again for the user.
"""

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n'))

"""
 -> Now in the lines 31-34, we can change about how to stop the
    program. Or we can do something to read a number of datas that
    need to be colected and then, finish the program.

 -> I prefer specify a comand to stop, but for read a number we
    can integrate the code with a GUI to make the code mor friendlier.
"""