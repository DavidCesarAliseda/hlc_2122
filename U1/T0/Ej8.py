""" Calcula la multiplicación y la suma de dos números. 
Dados dos números enteros, devuelve su producto sólo si el producto es mayor que 1000, de lo 
contrario, devuelve su suma. """
n1 = input("Introduzca el primer numero: ")
n2 = input("Introduzca el segundo numero: ")
suma = int(n1)+int(n2)
mult = int(n1)*int(n2)
if mult > 1000:
    print("El resultado es ", mult)
else:
    print("El resultado es ", suma)
