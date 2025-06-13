#Calcular la multiplicación de los enteros del 1 al 10
#resultado 3.628.800


acumulador = 1
number = [1,10]
for number in range (1,10):
    acumulador += (int(number)*acumulador)
    
print("La multiplicación de los numeros del 1 al 10 es: ",(acumulador))

print("FIN DEL PROGRAMA")