import random
import math
from random import randint

for x in range(50):
    print(randint(15, 57))


num = randint (1, 5)    #generamos un numero aleatorio
adivino = False         #inicializamos la bandera como False
while 1 == 1:
    pepito = input("Cual es el numero secreto? ingresa tu respuesta: ")

    if int(pepito) == num:      #comparamos la apuesta del usuario
        print("Adivinaste! :)") 
        adivino = True         #si adivino, cambiamos la bandera
    else:                        #para salir del bucle while
        print("Perdiste! ;(")   # loser

print("Fin")


# Ejercicio
# Crear juego de adivinar el numero (1 al 100) y dar
# pistas al usuario si el número a adivinar es mayor o menor
# que la apuesta del usuario

