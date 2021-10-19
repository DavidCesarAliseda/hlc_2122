""" Ejercicio 2:
Concatenar dos listas por índice

Dado:
lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]

Resultado esperado:
['Mi nombre es Chema'] """

lista1 = ["M", "nom", "e", "Che", "ajajajaja"]
lista2 = ["i", "bre", "s", "ma"]
lista3 = zip(lista1, lista2)
cadena = ""
if(len(lista1) < len(lista2)):
    corta = 1
else:
    corta = 2

""" for i in range(len(lista3)):
    for j in range(len(lista3[i])):
        cadena = cadena+lista3[i][j]
    cadena+" " """

print(len(lista3))
