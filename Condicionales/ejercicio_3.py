# Calcular el máximo entre 3 números

#ENTRADA
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un número: "))
num3 = int(input("Ingresa un número: "))

#PROCESO
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2:
        if num1 > num3:
            print('El número mayor es: ' ,num1)
        else:
            print('El número mayor es: ' ,num3)    
    else:
        if num2 > num3:
            print('El número mayor es: ',num2)
        else: 
            print('El número mayor es: ',num3)        
else:
    print("¡¡¡¡ERROR!!!! Ingrese 3 números distintos")    
    
print("FIN DEL PROGRAMA")    