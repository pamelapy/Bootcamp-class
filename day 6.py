class Dino:
    patas = 4
    nombre = None
    def __init__(self, canti_patas, un_nombre):
        self.patas = canti_patas
        self.nombre = un_nombre
        print("Hola soy un dinosaurio","me llamo", self.nombre, " y tengo", self.patas, "patas.")
    def get_patas(self):
        return self.patas

    def set_patas(self, cantidad):
        self.patas = cantidad

pepito = Dino(4, "Pepito")

#En el archivo persona.py, crear una clase persona con atributo nombre
#despues instanciar un objeto de tipo persona

class Persona:
        nomb_persona = None

        def __init__(self, un_nombre):
            self.nomb_persona = un_nombre
            print("Hola me llamo", self.nomb_persona,)

yo = Persona("Pepito")


#Modificar la clase de persona
#Agregarle un atributo edad y un metodo cumple años
#Inicializar/ crear un objeto tipo persona y hacerle cumplir años

class Person:
    age = None
    name = None
    def __init__(self, age_years, a_name):
        self.age = age_years
        self.name = a_name
        print("Hola mi nombre es", self.name, "y tengo", self.age, "años.")
    def get_age(self):
        return self.age

    def set_age(self, years):
        self.age = years

Fulanito = Person(5, "Fulanito")

