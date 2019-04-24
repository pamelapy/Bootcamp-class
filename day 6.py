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
        nombre_persona = None
        edad_persona = None

        def __init__(self, un_nombre, edad_persona):
            self.nombre_persona = un_nombre
            print("Hola me llamo", self.nombre_persona, ", y tengo", edad_persona, "años")

yo = Persona("Pepito, 25")


