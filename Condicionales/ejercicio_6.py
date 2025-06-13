# Determina si un año es bisiesto
#(divisible entre 4, pero no entre 100, a menos que sea divisible entre 400).

#ENTRADA
print("Este programa sirve para determinar si un año es bisiesto")
ab = int(input("Ingresa un año: "))


#PROCESO
if (ab % 4 == 0 and ab % 100 != 0) or ab % 400 == 0:
    print('El año' ,ab, 'es bisiesto')
else:
    print('El año' ,ab, 'no es bisiesto')