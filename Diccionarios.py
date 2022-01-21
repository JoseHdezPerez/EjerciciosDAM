"""
EJERCICIO 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car1["year"] = 2020

car2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car2["color"] = "red"

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

"""

"""
EJERCICIO 2

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")

if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")

"""

"""
EJERCICIO 3
Nombre = input('¿Cómo te llamas? ')
Edad = input('¿Cuántos años tienes? ')
Dir = input('¿Cuál es tu dirección? ')
Tlfn = input('¿Cuál es tu número de teléfono? ')

ObjetoPersona = {'nombre': Nombre, 'edad': Edad, 'direccion': Dir, 'telefono': Tlfn}

print(ObjetoPersona['nombre'], 'tiene', ObjetoPersona['edad'], 'años, vive en', ObjetoPersona['direccion'], 'y su número de teléfono es', ObjetoPersona['telefono'])

"""


"""
EJERCICIO 4
precios = {"manzana": 2, "naranja": 1.5, "platano": 4}
while True:
    print("\nDisponemos de 3 tipos de fruta: manzana, naranja y platano.")
    fruta = input("Dime la fruta que has vendido:")
    if fruta not in precios:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * precios[fruta]))
"""
