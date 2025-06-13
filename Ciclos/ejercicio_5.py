# Calcular el factorial de un entero positivo. 
# Igual que el ejercicio 4 pero la condición de fin del bucle será que el valor a multiplicar 
# sea menor o igual que el valor del entero positivo dado para calcular su factorial. 
# formula de factoria es n! = n × (n - 1) x (n - 2) x ..... 
# EJ: factorial de 5!= 5 x 4 x 3 x 2 x 1 = 120

number = int(input("Ingresa un número: "))
factorial = 1
if (number > 0):
    for i in range (1, number+1):
        factorial *= i 
    print("El factorial de" ,number, "es: ",factorial)
    
else:
    print("ERROR ... INGRESE UN NÚMERO POSITIVO")