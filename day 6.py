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


