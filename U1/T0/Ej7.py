# Acepte tres cadenas cualquiera de una llamada input().
# Escriba un programa para tomar tres nombres como entrada de un usuario con una única llamada a función input().
l = ""

for i in range(3):
    n = input("Introduzca un nombre: ")
    l = l+n+" "

print(l)
