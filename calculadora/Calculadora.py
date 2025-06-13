opcion = 999
while(True):
    print("CALCULADORA")
    print("Presiona 1 para SUMAR")
    print("Presiona 2 para RESTAR")
    print("Presiona 3 para MULTIPLICAR")
    print("Presiona 4 para DIVIDIR")
    print("Presiona 0 para SALIR")
    opcion = int(input("DIGITO: "))
    if (opcion == 0):
        print(f"FIN DEL PROGRAMA")
        break
    else:
        n1 = int(input("Ingrese primer número: "))
        n2 = int(input("Ingrese segundo número: "))
    if (opcion == 1):
        print(f"SUMANDO {n1} + {n2} = {n1 + n2}")
    elif (opcion == 2):
        print(f"RESTANDO {n1} - {n2} = {n1 - n2}")
    elif (opcion == 3):
        print(f"MULTIPLICANDO {n1} * {n2} = {n1 * n2}")
    elif (opcion == 4):
        print(f"DIVIDIENDO {n1} / {n2} = {n1 / n2}")
#con el while(true) y break, al general la terminar y probar el programa, instantaneamente,
#vuelve al codigo sin necesidad de reanudar el programa