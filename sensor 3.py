from time import sleep
import Adafruit_DHT as dht
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
def DHT11_data():
	humi, temp = dht.read_retry(dht.DHT11, 18)
	return humi, temp

while True:
	try:
		humedad, temperatura=DHT11_data()
		if humedad is not None and temperatura is not None:
			print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperatura,humedad))
			if temperatura >=24:
				print("Que calor! Oh Eh Oh")
			if temperatura <=20:
				print("Ponete un sweater!")
		else:
			print("Error en la lectura del sensor")
			
		sleep(20)
	except KeyboardInterrupt:
		gpio.cleanup()
		print("Programa terminado")
		break

