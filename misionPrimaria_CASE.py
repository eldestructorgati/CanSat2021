import radio
import sensor
import time


def main():
	radio.init()
	sensor.init()

	while True:
		sensor.writeLogLine()
		packet = bytes(sensor.line(), "utf-8")
		radio.rfm69.send(packet)
		time.sleep(1)

	radio.close()
	sensor.close()




try:
	main()

except KeyboardInterrupt:
	radio.close()
	sensor.close()
	print("Out")
