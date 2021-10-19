""" Concatenar dos listas en el siguiente orden

Dado:

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]

Resultado:

['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']
 """


lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
lista = []


for i in range(len(lista1)):
    for j in range(len(lista2)):
        cadena = lista1[i]+lista2[j]
        lista.append(cadena)

print(lista)
