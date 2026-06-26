import tkinter as tk
import random

secreto = random.randint(1,100)
intentos = 0

def adivinar():
    intento = int(entrada.get())
    global intentos
    intentos += 1

    if intento < secreto:
        resultado["text"] = "Muy bajo. Mas ALTO!"
    elif intento > secreto:
        resultado["text"] = "Muy alto. Mas BAJO!"
    else:
        resultado["text"] = f"Correcto! En {intentos}."
    entrada.delete(0, tk.END)
       
ventana = tk.Tk()
ventana.title("Adivina el numero")

tk.Label(ventana, text="Adivina (1-100:)").pack()

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Probar", command=adivinar).pack()

resultado = tk.Label(ventana, text="Escribe y pulsa Probar!")
resultado.pack()

ventana.mainloop()
