#Dada una serie de N números ingresados al azar por un usuario, 
# mostrar dichos números, de manera ascendente. 

num = 1
lista = []
while num>0:
    try:
        num = int(input("Ingresa algunos números usa 0 para cerrar el ciclo: "))
        lista.append(num) if num>0 else print("Fin del programa")
    except:
        print("Error al ingresar número")


lista.sort()
print("El orden ascendentes de los números es: ",(lista))