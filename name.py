print("hello")
print("cualquier cosa")
3+3
100/2
print("Hello world")
saludo = "Hello world"
print(saludo)
saludo = "Bye world"
print(saludo)
nombre = "Pamela"
edad = "26"
print(nombre)
print(edad)
print("Hola mi nombre es" , nombre)
print("Hola mi nombre es " + nombre)

# Ejercicio 1:
# Crear una variable nombre y una variable edad
# e imprimir el mensaje "Hola mi nombre es [nombre] y tengo [edad] años"
print("Hola mi nombre es" , nombre , "y tengo" , edad , "años")
num1 = 5
num2 = 3
print(num1 + num2)
resultado = num1 + num2
print(resultado)

# Ejercicio 2
# Crear dos variables numéricas, guardar el resultado de su
# multiplicación en una tercera variable e imprimir esa variable

num3 = 5
num4 = 2
resultado = num3 * num4
print(resultado)

# Ejercicio 3
# Crear una variable de texto [nombre] y una variable numérica 
# [veces], asignar valores a esas variables
#  e imprimir la multiplicación de esas variables

nombre = "Pamela"
veces = 10
resultado = nombre * veces
print(resultado)

# what was expected
nombre = "Pamela"
veces = 10
print(nombre*veces)

Lista = []
print(Lista)
Lista = ["Pam", 26, "teacher"]
print(Lista)

Lista.append ("gris")
print(Lista)
pasatiempo = "Listen to music"
Lista.append(pasatiempo)
print(Lista)
Lista.pop(pasatiempo)
print(Lista[3])
print(Lista[1])

# Ejercicio 4
# Crear variables [nombre], [edad], crear lista [persona]
# Con estas variables e imprimir la lista [color]
# e imprimir la lista de nuevo

nombre = "Pame."
edad = 26
Persona = [nombre, edad]
print(Persona)
color = "black"
Persona.append (color)
print(Persona)

# Ejercicio 5
# Utilizando la lista [Persona] imprimir el siguiente mensaje
# "Mi nombre es" y tengo años y soy ___ accediendo a los elementos de [Persona]

print("My name is", Persona[0], "I'm", Persona[1], "years old.", "My favorite color is", Persona[2]

print(Persona)
Persona.pop(2)
print(Persona)


# Ejercicio 6
# Crear una lista con x elementos e imprimir el último elemento
# Sin saber la cantidad de elementos que contiene
# Pista 1: Usar len()
# Pista 2: ...
# Pista 3: Lista[indice_ultimo]

Colors = ["Red", "Blue", "Yellow", "Green", "White", "Black", "Purple", "Brown"]
cantidad = len(Colors)
print(cantidad)
ultimo = cantidad - 1
print(Colors[ultimo])
print(Colors[len (Colors) - 1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.insert(0)
print(numbers)
numbers.remove(1)
print(numbers)


# Bucles / Loops

Lista_temas = ["variables", "tipos", "listas"]

for concepto in Lista_temas:
    print(concepto)


for num in [1, 2, 3, 4, 5, 6, 7, 8,]:
    print(num)

for concepto in Lista_temas:
    print("Hoy aprendí: ")
    print(concepto)
print("Que gusto!")

# Notes
# range (10) genera números de 0 al 9
# range (1,10)genera números del 1 al 9
# range (1,11) genera números del 1 al 10

# Ejercicio 7
# Crear una lista con varios elementos, recorrerla con un bucle
# for e imprimir el valor de cada elemento
# Lista_elementos = [_,_,_,_]

lista_super = ["pan", "leche", "galletitas", "queso", "jamon", "carne"]

numbers = [1, 2, 3, 4, 5, 6]

# Acumulador / Sumador
lista_numeros = [1, 3, 5, 7, 11, 13, 15, 17, 19, 23, 29]
suma = 0
for numero in lista_numeros:
    print("la variable suma = ", suma)
    print("la variable de for numero = ",  numero)
    suma = suma + numero
    print("-----")
print(suma)

#Ejercicio
# Crear una lista de números, recorrerla y acumular
# la multiplicación de sus elementos

producto = 1
for numero in lista_numeros:
    print("La variable producto = ", producto)
    print("La variable de for no = ", numero)
    producto = producto * numero
    print("-----")
print(producto)

# Funciones
def saludo (nombre):
    return nombre

name = saludo ("Pame")
print(name)


lista_numeritos = [3, 5, 7]
resultado = 0
for numeros in lista_numeritos:
    resultado = suma(resultado, pepito)
print(resultado)

# Ejercicio 8
# Crear una función que divida dos números y retorne el valor
# División, después imprimir ese resultado (fuera de la función)

def division (num1,num4):
    división = num1 / num4
    return división

resultado = division
print(resultado)


# Ejercicio 9
# Crear una función que reciba una lista de números como argumento
# Y retorne la suma de los numeros. Imprimir el resultado.

Lista_num = [1, 4, 6, 8]

def suma (n1):
    s = 0
    for resultado in n1:
        s = s + resultado
    return s

result = suma (Lista_num)
print(result)


Lista_num = [100, 40]

def resta (n1):
    r = n1
    for resultado in n1:
        r = n1 - r
    return r

result = resta (Lista_num)
print(result)



# DAY "2"



lista_mentores = ["Lore", "Yumi", "Willi"]

for silla in lista_mentores:
    print(silla)


school_objects = ["pen", "pencil", "book", "notebook"]

for objects in school_objects:
    print(objects)

# Notes
print( list(    range(15)   )   )
print( list(    range(5,15) )   )
print( list(    range(0,15,4)   )   )

lista_a = ['a','b','c','d']
Lista_b = [10, 99, 304956]

for variable_for_a in lista_a:
    print("Esto es el valor de lista_a")
    for variable_for_b in Lista_b:
        print("Esto es el valor de lista_b")
        print(variable_for_a, variable_for_b)


def seba(saludar_a):
    print("Hola", saludar_a)
seba("enzo")
seba("yumilda")
seba("mauricio")

def funcion_suma_yani (argumento_papel1, argumento_papel2):
    return argumento_papel1 + argumento_papel2

funcion_suma_yani(3,5)
silla = funcion_suma_yani(8,9)
print(silla)




def golpe():
    print("golpe")

def aplauso():
    print("clap")

def tararear():
    print("tarara")

def rock_you(mesa,veces):
    for vez in range(veces):
        golpe()
        golpe()
        aplauso()
    tararear()
rock_you(2,3)


def ahora_todos(argumento_lista_mesa):
    for mesa in argumento_lista_mesa:
        rock_you(mesa,3)

lista_mesas = [5,1,5,5,1,5,5,1,5,5]
ahora_todos(lista_mesas)


# Ejercicio
# Crear una funcion que reciba una lista de números como argumento
# y retorne la suma de los numeros. Imprimir el resultado.

lista_numeros_1 = [10, 20, 30, 40, 50, 60, 70]

def funcion_lista(argumento_lista):
    # Argumento y parámetros con sinonimos.
    suma = 0
    for numero in argumento_lista:
           suma = suma + numero
            # suma += numero (opcion valida)

    return suma

resultado = funcion_lista(lista_numeros_1)
print(resultado)


# Crear una función cuadrado_lista que reciba como parametro
# una lista de numeros y que retorne una lista 
# con el cuadrado de cada numero

cuadrado_lista = [4, 9, 5, 6]  #lista

def square(cuadrado_lista):    # funcion (def) -> nombre de la funcion (argumentos/elementos de la lista)
    lista_aux = []                  #lista vacia
    for square2 in cuadrado_lista:   #bucle (for) -> for nombre _del _bucle ->in -> Lista
        cuadrado = square2 * square2  # variable (cuadrado) =  num * num
        lista_aux.append(cuadrado)     # agrega los resultados de la variable a la lista vacia
        print(cuadrado)
    
    return lista_aux                # repite el proceso de la lista_aux y acumula los resultados

resultado = square(cuadrado_lista)   
print(resultado)



#ejemplo

lista_x = [2, 2, 4]
def lista_al_cuadrado(lista_x):
    lista_vacia = []
    for numero in lista_x:
        elevado = numero * numero
        lista_vacia.append(elevado)
    return lista_vacia

resultado = lista_al_cuadrado(lista_x)
print(resultado)


# Ejercicio
# Crear una función que suma_cuadrado reciba como argumento
# una lista de numeros y retorne la suma del cuadrado
# de cada numero
# [2, 2, 5] ----->  4+4+25 -----> 33

lista_b = [3, 3, 2]

def suma_cuadrado(lista_b):
    Lista_vacia_a = []
    for square3 in lista_b:
        cuadrado = square3 * square3
        Lista_vacia_a.append(cuadrado)
    suma = 0
    for square3 in Lista_vacia_a:
         suma = suma + square3
    return suma

resultado = (suma_cuadrado(lista_b))
print(resultado)


# Condicionales

a = 5

if a > 10:
    print("Es mayor")

else:
    print("Es menor o igual")


edad = 20

if edad >= 18:
    print("pue
    de tomar")
else: 
    print("No podes tomar")

for num in range(15):
    if num>10:
        print(num, "Es mayor a 10")
    else:
        print(num, "Es menor o igual a 10")


# Ejercicio
# Dada una variable nota_examen imprimir "Aprobado"
#  Si la nota es mayor o igual que 70
# sino imprimir aplazado

a = 70
if a >= 70:
    print("Aprobado")
else:
    print("Aplazado")



def paso_examen(nota):
if nota >= 70:
return True
else:
return False

if paso_examen(80)==True:
print("Aprobado")
else:
print("Aplazado")

# no saleeeeee
edad = 16

if edad>18:
    print("puede tomar")
elif edad<16:
    print("Callado nomás")
else edad<14: 
    print("No podes tomar")




for num in range(15):
    if num>10:
        print(num, "Es mayor a 10")
    else:
        print(num, "Es menor o igual a 10")


Edad = 8
for edad in range(10,110):
print("Tenes", edad)
if edad > 100:
    print("Podes pero creo que no deberias")
elif edad >= 18:
    print("Podes tomar")
elif edad >= 16:
    print("Callado nomás")
elif edad < 14:
    print("No podés tomar")


# Ejercicio
# Crear una función estudiente que reciba una edad y que retorne
# si segun esa edad el estudiente deberia estar en el prescolar
# primaria, secuandaria o universidad


def estudiante(edad):
    if edad >= 4 and edad < 6:
        print("Corresponde al Nivel inicial")
    elif edad >= 6 and edad < 14:
        print("Corresponde a la EEB")
    elif edad >= 15 and edad < 18:
        print("Corresponde a la Educación Secundaria")
    elif edad > 19:
        print("Corresponde al Nivel Universitario")
    else:
        print("No esta en edad escolar")

#estudiante(4)

for edad in range(25)
print(estudiante(edad))

saludo = "Hola Mundo"       # asignar un valor a la variable
print(saludo == "Hola Mundo")     #usar los dos == para preguntar si es T or F


#Ejemplo


def es_estudiante(argumento_nombre):
    lista_estudiantes = ["Mauricio", "Enrique", "Nidia"]
    for estudiante in lista_estudiantes:
        if argumento_nombre == estudiante:
            return True
    return False

es_estudiante("Nidia")
es_estudiante("Enrique")
es_estudiante("Mauricio")

#ejemplo

lista_nombres = ["Nidia", "Marce", "Enrique", "Bjorn"]

for nombre in lista_nombres:
    if es_estudiante(nombre) == True:
        print(nombre, "es estudiante")
    else:
        print(nombre, "no es estudiante")



# ejemplo


def es_estudiante2(argumento_nombre):
    lista_estudiantes = ["Mauricio", "Enrique", "Nidia"]
    for estudiante in lista_estudiantes:
        if argumento_nombre == estudiante:
            return True
    return False


# Ejercicio
# Dada esta lista
# recorrerla e imprimir si existe este animal en casa de nomadas


#solucion 1
lista_animales = ["perro", "gato", "canguro", "jirafa", "pinguino"]
#lista_animales_2 = ["perro", "gato", "pinguino"]

for animal in lista_animales:
    if animal == "perro":
        print(animal, "vive en casa nomadas")
    elif animal == "gato":
        print(animal, "vive en casa nomadas")
    elif animal == "pinguino":
        print(animal, "vive en casa nomadas")
    else:
        print(animal, "no vive n casa nomadas")

# solucion 2

lista_animales = ["perro", "gato", "canguro", "jirafa", "pinguino"]

def si_animal(animal):
    lista_animales_2 = ["perro", "gato", "pinguino"]
    for animales in lista_animales_2:
        if animal == animales:
            print("Existe un", animal, "en casa de nomadas")

for animal in lista_animales:
    si_animal(animal)




    for lista_animales_2 in lista_animales:
    if es_estudiante(nombre) == True:
        print(nombre, "si existe")
    else:
        print(nombre, "no existe")


print(animals(lista_animales))






