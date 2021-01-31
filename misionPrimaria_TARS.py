import radio
import time


def main():
	radio.init()

	while True:
		packet = radio.rfm69.receive()
		if packet is None:
			print("No packet")
		else:
			print(packet)
		time.sleep(1)

	radio.close()




try:
	main()

except KeyboardInterrupt:
	radio.close()
	print("Out")
