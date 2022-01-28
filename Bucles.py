"""
#EJERCICIO 1
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    notas.append(nota)
    
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado un" + notas[i])
    
"""
"""
# EJERCICIO 2
awarded = []
for i in range(3):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))

"""
"""
#EJERCICIO 3
asignaturas = ["Matematicas", "Fisica", "Quimica","Historia","Lengua"]
pendientes = asignaturas.copy()



notas = {
    'Matematicas': 0,
    'Fisica': 0,
    'Quimica': 0
}


for a in asignaturas:
    print("Que nota has sacado en %s?" % a)
   # notas[a] = int(input(">"))
    nota = int(input(">"))
    # if(notas[a] >= 5):

    if(nota >= 5):
        pendientes.remove(a)


for a in pendientes:
    print(a)
"""
"""
# EJERCICIO 4
palabra = input("Introduce una palabra: ")
palabra_alreves = palabra
palabra = list(palabra)
palabra_alreves = list(palabra_alreves)
palabra_alreves.reverse()
if palabra == palabra_alreves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
"""

"""
# EJERCICIO 5
def contar_vocales(palabrA):
    contador = 0
    for vocal in palabrA:
        if vocal.lower() in "aeiou":
            contador += 1
    return contador


palabra = input("Introduce una palabra o frase:")
cantidad = contar_vocales(palabra)
print(f"En la palabra o frase  '{palabra}'' hay {cantidad} vocales")
"""
# EJERCICIO 6
diccionario = {}
palabras = input(
    "Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
        
        
