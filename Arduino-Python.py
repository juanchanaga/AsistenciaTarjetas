import datetime
import time
from pyembedded.rfid_module.rfid import RFID

date = datetime.date.today()
arduino = RFID(port='COM3', baud_rate=9600)
time.sleep(2)

with open('C:\Toma_Asistencia\Asistencia' + str(date) +'.txt', 'a+') as f:
    f.write('ID,FECHA,HORA')
    f.write('\n')

print('Está listo para la asistencia\n')

while True:
    output = arduino.rfid_serial_port.readline()
    tiempo = datetime.datetime.now().strftime('%H:%M:%S')
    if output:
        output = output.decode()
        output = output.strip()
        output = str(output)
        output = output + ',' + str(date) + ',' + str(tiempo)
        print(output)

        with open('C:\Toma_Asistencia\Asistencia' + str(date) +'.txt', 'a+') as f:
            f.write(output)
            f.write('\n')