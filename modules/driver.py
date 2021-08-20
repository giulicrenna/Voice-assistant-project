import serial, time
from modules import ex_handler

try:
    try:
        serial_port = serial.Serial('COM3', 9600)
        time.sleep(2)
    except Exception as e:
        ex_handler.error_log(e)
        pass


    def controller(input_):
        if input_ == 'ON1':
            serial_port.write(b'a')
        elif input_ == 'ON2':
            serial_port.write(b'b')
        elif input_ == 'ON3':
            serial_port.write(b'c')
        elif input_ == 'ON4':
            serial_port.write(b'd')
        elif input_ == 'ON5':
            serial_port.write(b'e')
        elif input_ == 'ON6':
            serial_port.write(b'f')
        elif input_ == 'ON7':
            serial_port.write(b'g')
        elif input_ == 'ON8':
            serial_port.write(b'h')

        elif input_ == 'OFF1':
            serial_port.write(b'i')
        elif input_ == 'OFF2':
            serial_port.write(b'j')
        elif input_ == 'OFF3':
            serial_port.write(b'k')
        elif input_ == 'OFF4':
            serial_port.write(b'l')
        elif input_ == 'OFF5':
            serial_port.write(b'm')
        elif input_ == 'OFF6':
            serial_port.write(b'n')
        elif input_ == 'OFF7':
            serial_port.write(b'o')
        elif input_ == 'OFF8':
            serial_port.write(b'p')


    controller('OFF1')

except Exception as e:
    ex_handler.error_log(e)

