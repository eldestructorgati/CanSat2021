# .init (inicializar modulo radio)
# .close (vaciar pantalla antes de cerrar programa)

import time
# Libreria protocolos serie
import busio
# GPIO
from digitalio import DigitalInOut, Direction, Pull
import board
# Pantalla OLED
import adafruit_ssd1306
# Modulo radio
import adafruit_rfm69

display = None
rfm69 = None

def init():
	global display
	global rfm69

	# I2C
	i2c = busio.I2C(board.SCL, board.SDA)

	# OLED Display
	reset_pin = DigitalInOut(board.D4)
	display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)

	#Vaciar display
	display.fill(0)
	display.show()
	width = display.width
	height = display.height

	#Modulo radio
	CS = DigitalInOut(board.CE1)
	RESET = DigitalInOut(board.D25)
	spi =busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
	rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 433.0)
	prev_packet = None
	rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

def close():
	display.fill(0)
	display.show()
