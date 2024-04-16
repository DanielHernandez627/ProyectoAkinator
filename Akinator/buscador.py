import tkinter.messagebox as messagebox
import pyttsx3
import json

# Cargar la taxonomía desde el archivo JSON
with open("Akinator/taxonomia.json") as file:
    taxonomia = json.load(file)

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

def es_consecuente(X, Y):
    # Verificar si Y es consecuente con X
    if nivel_1(X):
        return nivel_1(X) == Y
    elif nivel_2(X):
        return nivel_2(X) == Y
    elif nivel_3(X):
        return nivel_3(X) == Y
    elif nivel_4(X):
        return nivel_4(X) == Y
    elif nivel_5(X):
        return nivel_5(X) == Y
    elif nivel_6(X):
        return nivel_6(X) == Y
    elif nivel_7(X):
        return nivel_7(X) == Y
    else:
        return False

def nivel_1(X):
    return X == 'bic_tec'

def nivel_2(X):
    return X in taxonomia['bic_tec']

def nivel_3(X):
    if X == 'software':
        return X in taxonomia['bic_tec']['software']
    elif X == 'hardware':
        return X in taxonomia['bic_tec']['hardware']

def nivel_4(X):
    if X == 'internet' or X == 'so':
        return X in taxonomia['bic_tec']['software']
    elif X == 'dispositivos' or X == 'componentes':
        return X in taxonomia['bic_tec']['hardware']

def nivel_5(X):
    if X == 'motor_de_busqueda' or X == 'movil' or X == 'escritorio':
        return X in taxonomia['bic_tec']['software']
    elif X == 'abierto' or X == 'cerrado':
        return X in taxonomia['bic_tec']['hardware']

def nivel_6(X):
    if X == 'web2' or X == 'web3' or X == 'Abierto' or X == 'Cerrado':
        return X in taxonomia['bic_tec']['software']

def nivel_7(X):
    if X == 'open_source' or X == 'Dapps' or X == 'NFTs' or X == 'Android' or X == 'Sailfish_Os':
        return X in taxonomia['bic_tec']['software']
    elif X == 'firefox' or X == 'opera':
        return X in taxonomia['bic_tec']['software']['internet']['motor_de_busqueda']['web2']
    else:
        return False

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

def iniciar_adivinanza():
    # Iniciar la búsqueda desde el nivel 0 (bic_tec) del JSON de taxonomía
    resultado = inferir_elemento(taxonomia, 'bic_tec')

    if resultado:
        mensaje_resultado = f"¡He adivinado tu compañía! Es {resultado}."
        engine.say(mensaje_resultado)
        engine.runAndWait()
        messagebox.showinfo("Akinator", mensaje_resultado)
    else:
        engine.say("No se pudo inferir el elemento.")
        engine.runAndWait()
        messagebox.showinfo("Akinator", "No se pudo inferir el elemento.")