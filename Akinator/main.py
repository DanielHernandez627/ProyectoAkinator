import tkinter as tk
from PIL import Image, ImageTk
import buscador  # Importa el módulo buscador.py que contiene la lógica de adivinanza

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Akinator")
ventana.geometry("600x400")  # Establecer el tamaño de la ventana

# Cargar y mostrar el GIF
gif_path = "Akinator/genio.gif"
gif = Image.open(gif_path)
frame_imagen = ImageTk.PhotoImage(gif)
gif_label = tk.Label(ventana, image=frame_imagen)
gif_label.pack(padx=20, pady=20)

# Función para iniciar la adivinanza
def empezar_adivinanza():
    respuesta = buscador.iniciar_adivinanza()
    # Aquí podrías manejar la respuesta según lo que necesites hacer con ella

# Botón para iniciar la adivinanza
empezar_button = tk.Button(ventana, text="Empezar Adivinanza", command=empezar_adivinanza)
empezar_button.pack(pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
