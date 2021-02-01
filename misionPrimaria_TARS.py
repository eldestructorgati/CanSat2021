import radio
import time


def main():
	radio.init()
	startTime = 0
	outputLog = open('dataTARS.txt', 'a')

	while True:
		packet = radio.rfm69.receive()
		if packet is None:
			pass
		else:
			dataLine = packet.decode()
			fields = dataLine.split (' ')
			timeStamp = float(fields[0])

			if startTime == 0:
				startTime = timeStamp

			temperature = float(fields[1])
			humedad = float(fields[2])
			presion = float(fields[3])
			altitud = float(fields[4])
			outputLog.write("%f %f %f %f %f\n" % (timeStamp, temperature, humedad, presion, altitud))
			print("\nTime: %0.2f s" % (timeStamp - startTime))
			print("Temperature: %0.1f C" % temperature)
			print("Humedad: %0.1f %%" % humedad)
			print("Presión: %0.1f hPa" % presion)
			print("Altitud: %0.2f meters" % altitud)


	radio.close()




try:
	main()

except KeyboardInterrupt:
	radio.close()
	print("Out")
