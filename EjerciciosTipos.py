import re

""""
EJERCICIO 1
nombre = "Hola Juan Perez"

balance = 53.44

print ("%s Tu balance es de %f $." % (nombre, balance))
"""




"""
EJERCICIO 2
a=1
b=float(a)

e=True
f=str(e)


print (b,f)
"""


"""
EJERCICIO 3

#SoyUnEntero= 100
SoyUnString="Hola Juanvi"
#SoyUnFloat=100.200

#entero=len(SoyUnEntero)
string=len(SoyUnString)
#float=len(SoyUnFloat)

print(string)
#Aparentemente len solo vale para string, o arraylist o directorios.
"""

"""
EJERCICIO 4

StringStrip = "     Resident Evil     "
x = StringStrip.strip()
print("De todos los juegos", x, "es mi saga favorita")


StringSplit = "Nos encanta python"
y = StringSplit.split()
print(y)


StringLower= "ESTAMOS PROBANDO METODOS EN PYTHON"
z=StringLower.lower()
print(z)

StringUppper= "estamos probando metodos en python"
h=StringUppper.upper()
print(h)

StringFind="Realiza un ejemplo de utilización de los métodos de string strip, split, lower, upper, find, index y startswith"
n=StringFind.find("utilización")
print(n)


StringIndex="Estamos probando diferentes metodos en python, esto es genial"
m=StringIndex.index("diferentes")
print(m)

StringStartsWith="Bueno vamos a comprobar si esto de verdad comprueba por que palabra empieza esta frase"
l=StringStartsWith.startswith("Bueno")
print(l)
"""



"""
EJERCICIO 5

ElQuijote="En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
encontrado = re.findall("a",  ElQuijote)
print(len(encontrado))
"""

