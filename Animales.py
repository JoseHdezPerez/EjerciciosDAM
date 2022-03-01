"""animal module"""
class Animal:
    """Animal class"""
    def __init__(self, color, patas):
        self.color = color
        self.patas = patas
        self.especie = self.__class__.__name__

    def __str__(self):
        return f"""{self.especie} con {self.patas} patas y de color {self.color}"""

class Lobo(Animal):
    """ Clase lobo """
    def __init__(self, color):
        super().__init__(color, patas = 4)

class Oveja(Animal):
    """ Oveja. Por defecto la oveja es blanca """
    def __init__(self):
        super().__init__(patas = 4, color = "blanco")

    @staticmethod
    def get_oveja_negra():
        oveja = Oveja()
        oveja.color = "negro"
        return oveja

class Serpiente(Animal):
    """ Serpiente """
    def __init__(self):
        super().__init__(color = "verde", patas = 0)

class Loro(Animal):
    """ Loro """
    def __init__(self, patas):
        super().__init__(color = "multicolor", patas = patas)

class Caja:
    id_global = 0
    """ Caja para meter animales"""
    def __init__(self):
        self.id = Caja.id_global
        self.animales = []
        Caja.id_global += 1

    def meter(self, *animales):
        self.animales.extend(animales)

    def __str__(self):
        ret = f"Caja [{self.id}] con los siguientes animales: "
        for a in self.animales:
            ret += a.__str__()
            ret += " "
        return ret

    def animales_por_patas(self, patas):
        return [a for a in self.animales if a.patas == patas]

lobo = Lobo(color = "gris")
loro = Loro(patas = 2)
serp = Serpiente()
oveja = Oveja.get_oveja_negra()

caja = Caja()
caja.meter(lobo, loro, serp, oveja)

print("Los animales que hay en la caja con 0 patas son:")
for a in caja.animales_por_patas(0):
    print(a)

print(caja)

caja2 = Caja()
caja2.meter(serp, oveja)

print(caja2)