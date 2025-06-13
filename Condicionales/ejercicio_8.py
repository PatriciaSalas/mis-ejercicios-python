# Calcular el costo de un billete de tren según la edad:
#	Menores de 5: gratis.
#	Entre 5 y 12: 50% descuento.
#	Mayores de 60: 30% descuento.
#	Resto: precio completo.
#round = redondear

edad = int(input("Ingrese su edad: "))
boleto = 2000
if (edad < 5):
    print("La entrada es gratis")
elif (edad >= 5 and edad <= 12):
    print("El valor del boleto tiene un 50% de descuento. El total a pagar es:",boleto - (round(2000*(50/100))))
elif (edad >= 60):
    print("El valor del boleto tiene un 30% de descuento. El total a pagar es:",boleto - (round(2000*(30/100))))
else:
    print("Precio general:",boleto)