"""Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada


Dado :

str1 = "C@#he26ma^&Du5ran"

Resultado esperado :

Recuentos totales de caracteres, dígitos y símbolos 

Caracteres = 10 
Dígitos = 3 
Símbolo = 4"""

str1 = "C@#he26ma^&Du5ran"
caracteres = 0
digitos = 0
simbolos = 0

for i in str1:
    if(i.isdigit()):
        digitos += 1
    elif(i.isalpha()):
        caracteres += 1
    else:
        simbolos += 1

print("Caracteres: ", caracteres)
print("Digitos: ", digitos)
print("Simbolos: ", simbolos)
