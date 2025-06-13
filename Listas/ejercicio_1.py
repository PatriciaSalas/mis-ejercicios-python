#escribir una línea de código que solicite al usuario que reemplace 
# el número central en la lista con un número entero ingresado por el usuario (Paso 1)
#escribir una línea de código que elimine el último elemento de la lista (Paso 2)
#escribir una línea de código que imprima la longitud de la lista existente (Paso 3).

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("lista", hat_list)

central = int(input("Reemplace el elemnto central: "))
hat_list[2] = central

del hat_list[4]
print("Se realizaron modificaciones en la lista, eliminando el ultimo elemento \ny remplazando el elemento central")
print("La nueva longitud de la lista es", len(hat_list))

print(hat_list)