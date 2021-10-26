""" Compruebe si todos los elementos de la siguiente tupla son iguales

tupla = (45, 45, 45, 45)

Resultado:

True """

tupla = (45, 45, 45, 45)
iguales = True
for i in range(len(tupla)):
    if(tupla[0] != tupla[i]):
        iguales = False
        break

print(iguales)

print(all(i == tupla[0] for i in tupla))
