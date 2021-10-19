""" Ejercicio 2:
Concatenar dos listas por índice

Dado:
lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]

Resultado esperado:
['Mi nombre es Chema'] """

lista1 = ["M", "nom", "e", "Che", "ajajajaja"]
lista2 = ["i", "bre", "s", "ma"]
lista3 = list(zip(lista1, lista2))
cadena = ""

for i in range(len(lista3)):
    for j in range(len(lista3[i])):
        cadena = cadena+lista3[i][j]
    cadena += " "

if(len(lista1) < len(lista2)):
    for i in range(len(lista1), len(lista2)):
        cadena = cadena+" "+lista2[i]
    corta = 1
else:
    for i in range(len(lista2), len(lista1)):
        cadena = cadena+lista1[i]+" "
    corta = 2

print(cadena)
