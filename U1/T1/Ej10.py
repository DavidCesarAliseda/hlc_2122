"""Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena

Dado :

str1 = "Apple"

Resultado:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""

str1 = "Apple"
diccionario = {}

for i in str1:
    diccionario[i] = str1.count(i)

print(diccionario)
