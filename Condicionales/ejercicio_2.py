# Determinar si un número entero es impar utilizando %

#ENTRADA
print("Ingresa un número")

#PROCESO
numero = int(input())
if numero % 2 == 0:
    print("El número es par")
    potencia = numero ** 2
    print("Su valor elevado al cuadrado es: ", potencia)
else:
    print("El número es impar")
    potencia = numero ** 3
    print("Su valor elevado al cubo es: ", potencia)