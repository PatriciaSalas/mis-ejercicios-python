# Contar cuantos enteros positivos introduce el usuario. 
# Indicación: leer los números mientras sean positivos, 
# usando una variable contadora que se va incrementando en uno cada vez que se lee un número; 
# elresultado será el valor de esa variable contadora.

contador = 0
num = 1
while(num>0):
    num = int(input("Ingrese un número: "))
    if(num>0):
        contador += num
        print("El valor es: ", str(contador))
    else:
        print("Los números negativos no se contaran en la suma")
        print("INGRESE SOLO NÚMEROS POSITIVOS")