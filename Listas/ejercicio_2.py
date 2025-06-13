# paso 1 crear lista vacía
beatles = []
# paso 2 agregar a miembros de la banda con append 
#Chatgpt dice que se puede añadir a todos juntos con "beatles.extend([])"
beatles.append('John Lennon') 
beatles.append('Paul McCartney') 
beatles.append('George Harrison')
print('PASO 2', beatles)
# paso 3 añadir miembros            
print("Añade a los siguientes miembros: Stu Sutcliffe y Pete Best")
for i in range(2):
    miembros = input("Añadir a Stu, presiona ENTER \nañade PETE, presiona ENTER: ")
    beatles.append(miembros)
print('PASO 3', beatles)
# paso 4 eliminar a miembros. Ojo solo se puede eliminar a un miembro a la vez, osea por separado.
#y recordar que si elimino un elemnto, el otro se movera de posición, por eso se elimina 3 y luego 3.
del beatles[3]
del beatles[3]
print('PASO 4', beatles)
# paso 5
beatles.insert(0, 'Ringo Starr')
print('PASO 5', beatles)
# probando la longitud de la lista
print("Los Fav", len(beatles))