# Determinar si un número es divisible entre 3 y 5 simultáneamente.

numero = int(input("ingresa un numero: "))
if (numero % 3 == 0 and numero % 5 == 0):
    print("el numero es divisible entre 3 y 5")
elif (numero % 3 == 0 and numero % 5 != 0):
    print("el numero solo es divisible por 3")
elif (numero % 3 != 0 and numero % 5 == 0):
    print("el numero solo es divisible por 5")
else:
    print("el numero no es divisible entre 3 y 5")