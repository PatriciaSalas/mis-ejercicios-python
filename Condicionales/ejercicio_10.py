# Calcular el máximo entre 2 números dados

#ENTRADA
print("Ingresa dos números y compara cual es el mayor")
numero1 = int(input("Digite un valor "))

numero2 = int(input("Digite otro valor "))

#PROCESO
if (numero1 < numero2):
    print('El número' ,numero2, 'es mayor que el número' ,numero1)
 
elif (numero1 == numero2):
    print('El número' ,numero1, 'y el número' ,numero2, 'son iguales')    
    
else:
    print('El número' ,numero1, 'es mayor que el número' ,numero2)   

print("FIN DEL PROGRAMA")