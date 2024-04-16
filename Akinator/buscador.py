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
        nivel_2(X, Y)
    elif nivel_2(X):
        nivel_3(X, Y)
    elif nivel_3(X):
        nivel_4(X, Y)
    elif nivel_4(X):
        nivel_5(X, Y)
    elif nivel_5(X):
        nivel_6(X, Y)
    elif nivel_6(X):
        nivel_7(X, Y)

def nivel_1(X):
    return X == 'bic_tec'

def nivel_2(X, Y):
    if X == 'bic_tec':
        return Y == 'software' or Y == 'hardware'

def nivel_3(X, Y):
    if X == 'software':
        return Y == 'internet' or Y == 'so'
    elif X == 'hardware':
        return Y == 'dispositivos' or Y == 'componentes'

def nivel_4(X, Y):
    if X == 'internet':
        return Y == 'motor_de_busqueda' or Y == 'web2' or Y == 'web3'
    elif X == 'so':
        return Y == 'movil' or Y == 'escritorio'

def nivel_5(X, Y):
    if X == 'motor_de_busqueda':
        return Y == 'web2' or Y == 'web3'
    elif X == 'movil':
        return Y == 'Abierto' or Y == 'Cerrado'
    elif X == 'escritorio':
        return Y == 'abierto' or Y == 'cerrado'

def nivel_6(X, Y):
    if X == 'web2':
        return Y == 'open_source'
    elif X == 'web3':
        return Y == 'Dapps' or Y == 'NFTs'
    elif X == 'Abierto':
        return Y == 'Android' or Y == 'Sailfish_Os'
    elif X == 'Cerrado':
        return Y == 'Android'

def nivel_7(X, Y):
    if X == 'open_source':
        return Y == 'firefox' or Y == 'opera'
    elif X == 'Dapps':
        return Y == {}
    elif X == 'NFTs':
        return Y == {}
    elif X == 'Android':
        return Y == {}
    elif X == 'Sailfish_Os':
        return Y == {}

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
    mensaje = f"¿El elemento tiene la característica '{pregunta}'?"
    engine.say(mensaje)
    engine.runAndWait()
    respuesta = messagebox.askquestion("Akinator", mensaje)

    if respuesta == 'yes':
        siguiente_nodo = caracteristicas[pregunta]
        return inferir_elemento(siguiente_nodo, pregunta)
    elif respuesta == 'no':
        caracteristicas_restantes = {carac: caracteristicas[carac] for carac in caracteristicas if carac != pregunta}
        if not caracteristicas_restantes:
            return None

        for caracteristica in caracteristicas_restantes:
            siguiente_nodo = caracteristicas_restantes[caracteristica]
            resultado = inferir_elemento(siguiente_nodo, caracteristica)
            if resultado:
                return resultado
        
        return None
    else:
        messagebox.showerror("Error", "Respuesta no válida. Por favor responda 'yes' para sí o 'no' para no.")
        return inferir_elemento(caracteristicas, nodo_actual)

def iniciar_adivinanza():
    # Iniciar la búsqueda desde el nivel 0 (bic_tec) del JSON de taxonomía
    resultado = inferir_elemento(taxonomia, 'bic_tec')
    if resultado:
        mensaje_resultado = f"El elemento es '{resultado}'."
        engine.say(mensaje_resultado)
        engine.runAndWait()
        messagebox.showinfo("Akinator", mensaje_resultado)
    else:
        engine.say("No se pudo inferir el elemento.")
        engine.runAndWait()
        messagebox.showinfo("Akinator", "No se pudo inferir el elemento.")
