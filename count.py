import tkinter as tk

def main():
    # Inicializamos la ventana principal
    root = tk.Tk()
    root.title("Contador Simple")
    root.geometry("250x300")

    # Variable para almacenar el contador
    contador = tk.IntVar(value=0)

    # Función que incrementa el contador
    def incrementar():
        contador.set(contador.get() + 1)

    # Funcion que resetea el contador
    def resetear():
        contador.set(0)

    # Etiqueta para mostrar el valor del contador
    etiqueta = tk.Label(root, textvariable=contador, font=("Arial", 24))
    etiqueta.pack(pady=20)

    # Botón que incrementa el contador
    boton = tk.Button(root, text="Incrementar", command=incrementar, font=("Arial", 14))
    boton.pack()

    # Botón que resetea el contador
    boton_reset = tk.Button(root, text="Resetear", command=resetear, font=("Arial", 14))
    boton_reset.pack(pady=10)

    # Bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
