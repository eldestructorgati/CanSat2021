# .init (inicializar)
# .line (datos)
# .writeLogLine (escribir datos a fichero)
# .altitud (altitud)

import time
import board
import busio
import adafruit_bme280

outputLog = None
bme280 = None

def init():
	global outputLog
	global bme280

	i2c = busio.I2C(board.SCL, board.SDA)
	bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
	bme280.sea_level_pressure = 1013.25
	outputLog = open ('data.txt', 'a')

def altitud():
	return bme280.altitude

def line():
        return "%f %f %f %f %f\n" % (time.time(), bme280.temperature, bme280.humidity, bme280.pressure, bme280.altitude)

def writeLogLine():
        outputLog.write(line())
        outputLog.flush()

def close():
	outputLog.close()
