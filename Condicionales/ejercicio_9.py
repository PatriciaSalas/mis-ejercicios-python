#Determinar si un triángulo es equilátero, isósceles o escaleno 
#todos los lados iguales = equilatero
#dos lados iguales y uno distinto = isoseles
#tres lados distintos = escaleno

print("Conoce si el Triángulo es Equilátero, Isósceles o Escaleno")
print("Ingresa la medida de sus tres lados")
a = input("Ingresa la medida lado 1: ")
b = input("ingresa la medida lado 2: ")
c = input("ingresa la medida lado 3: ")

if a == b and b == c:
    print("Es un Triangulo Equilátero")
    
elif a == b and a != c:
    print("Es un Triángulo Isósceles")
elif a != b and a == c: 
    print("Es un Triángulo Isósceles")
elif b == c and a != b:
    print("Es un Triángulo Isósceles")

else:
    print("Es un Triángulo Escaleno") 