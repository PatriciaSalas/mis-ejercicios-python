#Programa importado a traves de pypi.org llamado "Chilean Rut" para añadir un codigo ya hecho por otro

import chilean_rut
from getpass4 import getpass
while(True):
    rut = input("Ingresa tu rut: ")
    clave = getpass("Ingresa tu clave: ", "*")
    if(chilean_rut.is_valid(rut)):
        print("Rut válido")
        print("Fin del programa")
        break
    else: 
        print("Rut no válido")
#Actividad: Crear un programa en donde login sea el rut de una persona y la clave sea
# 1234 cuando ingrese la contraseña edbe aparecer * en la pantalla. buscar en pypi.org