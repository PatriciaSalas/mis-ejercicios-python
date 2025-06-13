# Dados dos números, verificar si uno es múltiplo del otro (asumir que el primero es mayor).

#ENTRADA
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))


#PROCESO
def calcular(num1,num2):
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}")
    elif num2 % num1 == 0:
        print(f"{num2} es múltiplo de {num1}")
    else: 
        print("Los números no son múltiplos")
calcular (num1,num2) # este calcular no puede ir en la entrada, funciona mejor al final del proceso
# sin este calcular, no toma la condicion para hacerlo. 