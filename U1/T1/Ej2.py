"""Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1


Dado :

s1 = "Hola"
s2 = "Adios"

Resultado:

HoAdiosla"""

s1 = input("Introduzca una cadena: ")
s2 = input("Introduzca otra cadena: ")

mitad = int(len(s1)/2)

string = s1[:mitad]+s2+s1[len(s1)-mitad:len(s1)]
print(string)
