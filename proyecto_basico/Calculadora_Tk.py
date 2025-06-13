import tkinter as tk
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")
        
    print(resultado)
def limpiar():
    entrada.delete(0, tk.END)
def losbotones (parametro):
    entrada.insert(tk.END, parametro)
    print(parametro)
#Crear la ventana principal
ventana = tk.Tk()
ventana.title("CALCULADORA")
#Crear la caja de entrada (donde se muestra la operación y el resultado)
entrada = tk.Entry(ventana, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0) # Botón de limpiar
]
for texto,fila,columna in botones:
    print(texto,fila,columna)
    if (texto == '='):
        boton = tk.Button(ventana, text=texto, width=10, height=3, font=('Arial', 10), command=calcular)
    elif texto == 'C':
        boton = tk.Button(ventana, text=texto, width=10, height=3, font=('Arial', 10), command=limpiar)
    else:
        boton = tk.Button(ventana, text=texto, width=10, height=3, font=('Arial', 10), command=lambda valor=texto: losbotones(valor))
    boton.grid(row=fila, column=columna) 
    
#Ejecutar la aplicación
ventana.mainloop()