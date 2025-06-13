#Calcular digito verificador:
#para calcular digito verificador, primero hay que invertir la cifra
#INGRESA EL RUT
#PASO 1: INVIERTE LA CIFRA SIN DV
#PASO 2: LA SERIE NUMERICA VA DESDE EL 2 AL 7 Y LUEGO SE REPITE EN BUCLE. 
#PASO 3: SE SUMA LA CIFRA DEL RUT INVERTIDA + LA SERIE NUMERICA 
#PASO 4: SUMAR TODOS LOS RESULTADOS DEL PASO 3
#PASO 5: OBTEN EL RESTO DEL PASO 4 CON EL NUMERO 11
#PASO 6: DV ES LA RESTA ENTRE EL 11 - RESULTADO DEL PASO 5. SI EL VALOR ES 10, SE REEMPLAZA POR K


Rut = input("Ingresa tu rut: ")
contador = 2 #contador vuelve a 2
acumulador = 0 #acumulador = 0
residuo = 11 #residuo = 11

for digito in reversed (Rut): #sirve para poner el rut al reves
    #print (digito, " ", contador) #una vez comprobaddo ya no es necesario este print
    acumulador += int(digito)*contador #colocamos el acumulador para sumar y multiplicar el DV y el contador
   
    contador += 1  #va sumando de a 1
    if (contador > 7): #si contador es mayor a 7 entonces 
        contador = 2 #contador vuelve a  2 
DV = (11-(acumulador % 11)) #creamos una nueva variable en este caso (DV), para terminar la operación
if DV == 10: #colocamos la condicional if para determinar si es igual a 10, el print sera K
    print("Su digito verificador es: K")
    
else: # y el else para solo imprimir el DV (variable dv)
    print("Su digito verificador es: ",DV)
    
    print("--------> FIN DEL PROGRAMA <--------")