""" Ejercicio 1:
Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena formada por los tres caracteres del medio de una cadena determinada

Dado :
Caso 1

str1 = "ChemTioaDur"

Resultado

Tio

Caso 2

str2 = "ChQueem"

Resultado

Que """

cadena = input("Introduzca una cadena con mas de 7 digitos: ")
mitad = int(len(cadena)/2)-1

print(cadena[mitad:mitad+3])
