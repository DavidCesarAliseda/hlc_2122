"""Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, 
ignorando todos los demás caracteres.


Dado :

str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"

Resultado:

la suma es 294
el promedio es 73.5"""

str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
array = str1.split(" ")
suma = 0
contador = 0

for i in array:
    if(i.isdigit()):
        suma += int(i)
        contador += 1

print("la suma es  ", suma)
print("la media es  ", suma/contador)
