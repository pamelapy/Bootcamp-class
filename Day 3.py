#Dia 3

lista_factores = [2, 3, 4]   #sacamos la tabla de multiplicar de estos numeros
lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for a in lista_factores:
    print("La tabla del:", a)
    for i in lista_numeros:
        print(a*i)  #multiplicamos
print("Finalizado")



lista_nombres = ["Cesar", "Pame", "Sandra", "Jessi"]
lista_saludos = ["Hello", "Bonjour", "Oi", "Hallo", "Mba'eichapa", "Ha upei"]

for b in lista_saludos:
    for c in lista_nombres:
        print(b, c)



ph = 8
condicion = 8

if ph < condicion :
    print("Es acido")
elif ph == condicion :
    print("Es  neutro")
else:   # Es el caso donde ph es mayor a 7
    print("Es básico")


edad = 5
# entre 10 y 20
if 20 >= edad >= 10:
    print("Adolescente")
else:
    print("Fuera del rango de adolescencia")


#Ejercicio
# sus datos
# ej: sexo = m o f

edad = 26
sexo = "Femenino"

if sexo == "Femenino":
    print("Usted es de sexo femenino y su edad es", edad)
elif sexo == "Masculino":
    print("Usted es de sexo masculino y su edad es", edad)


edad = 29

if edad > 10 and edad < 20:   #se deben cumplir ambas condiciones
    print("estas en el rango")
else:
    print("estas fuera del rango")



#Ejercicio
#crear la variable sexo y edad e imprimir sus datos
# ejemplo: sexo=m o sexo=f o sexo=o
#entre 12 y 19 años sos adolescente
#salida: sos adolescente, de sexo femenino con 15 años
# salida : No sos adolescente, sos de sexo masculino con 9 años

edad = 30
sexo = "masculino"

if edad > 12 and edad < 19 and sexo == "femenino":
    print("Sos adolescente, tu sexo es femenino, y tu edad es", edad, "años")
elif edad > 12 and edad < 19 and sexo == "masculino":
    print("Sos adolescente, tu sexo es masculino, y tu edad es", edad, "años")
elif edad > 19 and sexo == "femenino":
    print("No sos adolescente, tu sexo es femenino, y tu edad es", edad, "años")
elif edad > 19 and sexo == "masculino":
    print("No sos adolescente, tu sexo es masculino, y tu edad es", edad, "años")


condicion = 0

while condicion < 10:
    print(condicion)
    condicion = condicion + 1
    print(condicion < 10) #evaluar la condición
    #ejecuta todo lo que esta dentro del while
print("Finalizado")


# Ejercicio
# Realizar la tabla de multiplicar del 6, 7, 8
# Salida: numero*factores = resultado
# Salida: 6*0 = 0
# Salida: 6*1 = 0


factor = 6

while factor < 9:       #factor a multiplicar menor al ultimo numero ( en este caso fue 8)
    a = 0               # el numero por el que se multiplicará
    while a < 10:       # mientras la condicion (a) sea menor a 10, osea del 0 hasta el 10
        a = a + 1
        resultado = factor * a
        print(factor, "x", a, "=", resultado)
    factor = factor + 1
print("Finalizado")





