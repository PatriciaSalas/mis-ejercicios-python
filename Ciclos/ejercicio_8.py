secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
num = int(input("Ingresa un número: "))
while num != 0:
    if  num == secret_number:  
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
                                                                          
    else: 
        print("¡Ja ja, ¡Estás atrapado en mi bucle!")
        print("Ingresa otro número")