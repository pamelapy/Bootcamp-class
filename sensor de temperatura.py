from time import sleep
import Adafruit_DHT as dht			#renombramos la librería como dht
import RPi.GPIO as gpio				#libreria para utilizar los puertos de ....
gpio.setmode(gpio.BCM)				#Modo BCM de la raspberry Pi
def DHT11_data():
	#leemos los datos del sensor, la humedad y la tempratura
	humi, temp = dht.read_retry(dht.DHT11, 18)		#pin data conectado
	return humi, temp

while True:
	try:
		humedad, temperatura=DHT11_data()
		if humedad is not None and temperatura is not None:
			print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperatura,humedad))
		else:
			print("Error en la lectura del sensor")
			#
			
		sleep(20)
	except KeyboardInterrupt:
		gpio.cleanup()
		print("Programa terminado")
		break
