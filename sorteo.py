from random import randint

#Sorteo para 5 personas
participantes = ["pepito", "Nemo", "Rodri", "Dino", "Shits"]
#print(participantes[randint(0,4)])


#Sorteo para 5 personas, hay 3 premios
#Ojo: una persona no puede ganar dos veces

from random import randint
participantes = ["pepito", "Nemo", "Rodri", "Dino", "Shits"]

def sorteo(participantes):    # funcion (def) -> nombre de la funcion (argumentos/elementos de la lista)
    lista_aux = []                  #lista vacia
    for sorteo_final in participantes:   #bucle (for) -> for nombre _del _bucle ->in -> Lista
        lista_aux.append(participantes)     # agrega los resultados de la variable a la lista vacia
    return lista_aux                # repite el proceso de la lista_aux y acumula los resultados
    cantidad = len(lista_aux)
    lista.pop(lista_aux[randint(0,4)])

for a in range(3):
    print(participantes[randint(0,4)])
