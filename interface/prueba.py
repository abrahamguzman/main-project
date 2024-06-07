import tkinter as tk

ventana = tk.Tk()
ventana.title("Prueba")
ventana.geometry("800x600")

texto = tk.Label(ventana, text="Hola mundo")
texto.pack()

boton = tk.Button(ventana, text="Pulsame")
boton.pack()


ventana.mainloop()