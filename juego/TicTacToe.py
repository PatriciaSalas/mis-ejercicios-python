from random import randrange
def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

def enter_move(board):
    ok = False	# suposición falsa - la necesitamos para entrar en el bucle
    while not ok:
        move = input("Ingresa tu movimiento: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
        if not ok:
            print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
            continue
        move = int(move) - 1 	# numero de la celda, del 0 al 8
        row = move // 3 	# fila de la celda
        col = move % 3		# columna de la celda
        sign = board[row][col]	# marca el cuadro elegido
        ok = sign not in ['O','X'] 
        if not ok:	# esta ocupado, ingresa una posición nuevamente
            print("¡Cuadro ocupado, ingresa nuevamente!")
            continue
        board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.


def make_list_of_free_fields(board):
    free = []	# la lista esta vacía inicialmente
    for row in range(3): # itera a través de las filas
        for col in range(3): # iitera a través de las columnas
            if board[row][col] not in ['O','X']: # ¿Está la celda libre?
                free.append((row,col)) # si, agrega una nueva tupla a la lista
    return free
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.


def victory_for(board, sign):
    if sign == "X":	# ¿Estamos buscando X?
        who = 'me'	# Si, es la maquina
    elif sign == "O": # ... ¿o estamos buscando O?
        who = 'you'	# Si, es el usuario
    else:
        who = None	# ¡No debemos de caer aquí!
    cross1 = cross2 = True  # para las diagonales
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:	# check row rc
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: # check column rc
            return who
        if board[rc][rc] != sign: # revisar la primer diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sign: # revisar la segunda diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.


def draw_move(board):
    free = make_list_of_free_fields(board) # crea una lista de los cuadros vacios o libres
    cnt = len(free)
    if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True # ¿De quien es turno ahora?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("¡Has ganado!")
elif victor == 'me':
	print("¡He ganado!")
else:
	print("¡Empate!")

