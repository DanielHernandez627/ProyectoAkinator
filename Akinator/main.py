import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3

# Lista de frases para simular el diálogo del GIF
frases = [
    "¡Hola! Soy un GIF animado.",
    "¿Cómo estás hoy?",
    "¡Estoy aquí para animarte!",
    "¡Diviértete programando con Python!",
]

# Texto inicial de saludo
saludo_inicial = "¡Hola! Bienvenido a la aplicación del GIF hablante."

# Función para reproducir el texto en voz de forma asincrónica
def reproducir_texto_en_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Función para actualizar el texto del recuadro de diálogo y reproducir en voz
def actualizar_dialogo():
    global indice_frase
    if indice_frase < len(frases):
        texto_dialogo = frases[indice_frase]

        # Actualizar el texto en el cuadro de diálogo
        dialogo_label.config(text=texto_dialogo)

        # Programar la reproducción del texto en voz después de un breve retraso
        ventana.after(100, lambda: reproducir_texto_en_voz(texto_dialogo))

        # Incrementar el índice de frase
        indice_frase += 1

# Función para empezar la lectura de las frases
def empezar_lectura():
    # Mostrar el saludo inicial en el cuadro de diálogo
    dialogo_label.config(text=saludo_inicial)

    # Reproducir el saludo inicial en voz después de un breve retraso
    ventana.after(100, lambda: reproducir_texto_en_voz(saludo_inicial))

    # Habilitar el botón para mostrar la siguiente frase
    siguiente_frase_button.config(state=tk.NORMAL)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("GIF Hablante")

# Cargar el GIF usando PIL
gif_path = "Akinator/genio.gif"
gif = Image.open(gif_path)
frame_imagen = ImageTk.PhotoImage(gif)

# Crear un widget de etiqueta para mostrar el GIF
gif_label = tk.Label(ventana, image=frame_imagen)
gif_label.pack(padx=20, pady=20, side=tk.LEFT)

# Crear un frame para contener el cuadro de diálogo
dialogo_frame = tk.Frame(ventana, padx=20, pady=20)
dialogo_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear un widget de etiqueta para el recuadro de diálogo
dialogo_label = tk.Label(dialogo_frame, text="", font=("Helvetica", 12), width=30, height=5, relief=tk.RIDGE)
dialogo_label.pack(fill=tk.BOTH, expand=True)

# Botón para empezar la lectura de las frases
empezar_button = tk.Button(ventana, text="Empezar Lectura", command=empezar_lectura)
empezar_button.pack(pady=(0, 10), side=tk.BOTTOM)  # Alineado abajo con un pequeño margen arriba

# Botón para mostrar la siguiente frase
siguiente_frase_button = tk.Button(ventana, text="Siguiente Frase", command=actualizar_dialogo, state=tk.DISABLED)
siguiente_frase_button.pack(pady=(0, 20), side=tk.BOTTOM)  # Alineado abajo con un margen más grande arriba

# Índice inicial de la frase
indice_frase = 0

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
