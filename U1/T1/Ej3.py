"""Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, 
el medio y el último carácter de cada cadena de entrada


Dado :

s1 = "Chema"
s2 = "Duran"

Resultado:

CDeran"""

s1 = input("Introduzca una cadena: ")
s2 = input("Introduzca otra cadena: ")

inicio = s1[:1]+s2[:1]
medio = s1[int(len(s1)/2):int(len(s1)/2+1)] + \
    s2[int(len(s2)/2):int(len(s2)/2+1)]
final = s1[len(s1)-1:len(s1)]+s2[len(s2)-1:len(s2)]

print(inicio+medio+final)
