#4. Calcular la suma de los pares del 1 al 20. Indicación: parecido al ejercicio 2; 
# cambia el incremento del valor a sumar y la condición del bucle ‘while’.
#resultado = 110

contador = 2
acumulador = 0
while (contador < 21):

    for number in range (1,21):
        if (number) % 2 == 0:
            acumulador += int(number)
            contador += 2

print("La suma total de los números pares del 1 al 20 es: ",acumulador)

print("------------> FIN DEL PROGRAMA <-------------")
print("---------------------------------------------")