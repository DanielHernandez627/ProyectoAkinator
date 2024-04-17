import tkinter.messagebox as messagebox
import pyttsx3
import json
from pyDatalog import pyDatalog

# Cargar la taxonomía desde el archivo JSON
with open("Akinator/taxonomia.json") as file:
    taxonomia = json.load(file)

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Función para crear átomos de pyDatalog según la estructura de la taxonomía
def crear_atomos(taxonomia, prefijo=''):
    for clave, valor in taxonomia.items():
        if isinstance(valor, dict):
            subprefijo = f"{prefijo}_{clave}" if prefijo else clave
            crear_atomos(valor, subprefijo)
        else:
            # Crear átomo con el prefijo adecuado
            atom_name = f"{prefijo}_{clave}" if prefijo else clave
            pyDatalog.create_atoms(atom_name)

# Crear átomos de pyDatalog según la estructura de la taxonomía
crear_atomos(taxonomia)

# Función para inferir el elemento que cumple con las características dadas
def inferir_elemento(caracteristicas, nodo_actual):
    if not caracteristicas:
        mensaje = f"¿El elemento es '{nodo_actual}'?"
        engine.say(mensaje)
        engine.runAndWait()
        respuesta_final = messagebox.askquestion("Akinator", mensaje)
        if respuesta_final == 'yes':
            return nodo_actual
        else:
            return None

    pregunta = next(iter(caracteristicas))
    siguiente_nodo = caracteristicas[pregunta]

    mensaje = f"¿El elemento tiene la característica '{pregunta}'?"
    engine.say(mensaje)
    engine.runAndWait()
    respuesta = messagebox.askquestion("Akinator", mensaje)

    if respuesta == 'yes':
        return inferir_elemento(siguiente_nodo, pregunta)
    elif respuesta == 'no':
        caracteristicas_restantes = {carac: caracteristicas[carac] for carac in caracteristicas if carac != pregunta}
        if not caracteristicas_restantes:
            return None

        return inferir_elemento(caracteristicas_restantes, nodo_actual)
    else:
        messagebox.showerror("Error", "Respuesta no válida. Por favor responda 'yes' para sí o 'no' para no.")
        return inferir_elemento(caracteristicas, nodo_actual)

# Función principal para iniciar la adivinanza
def iniciar_adivinanza():
    # Iniciar la búsqueda desde el nivel 0 (bic_tec) del JSON de taxonomía
    resultado = inferir_elemento(taxonomia, 'bic_tec')

    if resultado:
        mensaje_resultado = f"¡He adivinado tu elemento! Es {resultado}."
    else:
        mensaje_resultado = "No se pudo inferir el elemento."

    # Sintetizar voz con el resultado
    engine.say(mensaje_resultado)
    engine.runAndWait()

    messagebox.showinfo("Akinator", mensaje_resultado)