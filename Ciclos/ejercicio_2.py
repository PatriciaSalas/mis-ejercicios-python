#Calcular el producto de una serie de enteros hasta que se introduzca un cero.
acumulador = 1
num = 1 
while(num!=0):
    num = int(input("Ingrese un número y 0 es para salir: "))
    if(num!=0):
        acumulador *= num
#fuera del ciclo
print("El valor es: ", str(acumulador))