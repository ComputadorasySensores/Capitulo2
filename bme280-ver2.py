import time #importa time por el comando sleep
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280

# Inicializa el BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)


while True:
    temperatura = bme280.get_temperature()
    presion = bme280.get_pressure()
    humedad = bme280.get_humidity()
    print('{:05.2f}*C {:05.2f}hPa {:05.2f}%'.format(temperatura, presion, humedad))
    time.sleep(3)
