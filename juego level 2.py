# Ejercicio
# Crear juego de adivinar el numero (1 al 100) y dar
# pistas al usuario si el número a adivinar es mayor o menor
# que la apuesta del usuario


from random import randint

number = randint (1, 100)           # generamos un numero aleatorio
no_adivino = False
intento = 0
while 1 == 1 and intento < 7:
    numero_introducido = input("¡Cual es el numero secreto? Ingresa tu respuesta: ")
    if int(numero_introducido) == number:
        print("Adivinaste! :)")
        no_adivino = True
    else:
        print("Perdiste! Intentalo de nuevo ;(")
        if int(numero_introducido) >  number:
            print("El numero ingresado es mayor al numero secreto")
        elif int(numero_introducido) < number:
            print("El numero ingresado es menor al numero secreto")
    intento = intento + 1
if intento > 7:
    print("Superaste la cantidad de intentos :(")
elif no_adivino == True:
    print("Felicidades, sos un crack!")
print("Fin")


