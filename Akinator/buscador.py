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

# Función para verificar si Y es consecuente con X
def es_consecuente(X, Y):
    if X == 'bic_tec' and Y == 'tecnologia':
        return True
    elif X == 'software' and Y == 'tecnologia':
        return True
    elif X == 'hardware' and Y == 'tecnologia':
        return True
    elif X == 'internet' and Y == 'red':
        return True
    elif X == 'so' and Y == 'sistema_operativo':
        return True
    elif X == 'dispositivos' and Y == 'tipo_dispositivo':
        return True
    elif X == 'componentes' and Y == 'componente_hardware':
        return True
    elif X == 'motor_de_busqueda' and Y == 'motor_busqueda':
        return True
    elif X == 'app' and Y == 'aplicacion':
        return True
    elif X == 'movil' and Y == 'version_movil':
        return True
    elif X == 'escritorio' and Y == 'version_escritorio':
        return True
    elif X == 'pc' and Y == 'computadora_personal':
        return True
    elif X == 'telefonos' and Y == 'telefono':
        return True
    elif X == 'tabletas' and Y == 'tableta':
        return True
    elif X == 'cpu' and Y == 'unidad_procesamiento_central':
        return True
    elif X == 'gpu' and Y == 'unidad_procesamiento_grafico':
        return True
    elif X == 'almacenamiento' and Y == 'dispositivo_almacenamiento':
        return True
    elif X == 'ram' and Y == 'memoria_ram':
        return True
    elif X == 'web2' and Y == 'version_web2':
        return True
    elif X == 'web3' and Y == 'version_web3':
        return True
    elif X == 'open_source' and Y == 'software_codigo_abierto':
        return True
    elif X == 'corporativo' and Y == 'software_corporativo':
        return True
    elif X == 'Dapps' and Y == 'aplicacion_descentralizada':
        return True
    elif X == 'NFTs' and Y == 'token_no_fungible':
        return True
    elif X == 'firefox' and Y == 'navegador_firefox':
        return True
    elif X == 'opera' and Y == 'navegador_opera':
        return True
    elif X == 'chrome' and Y == 'navegador_chrome':
        return True
    elif X == 'edge' and Y == 'navegador_edge':
        return True
    elif X == 'whatsapp' and Y == 'aplicacion_whatsapp':
        return True
    elif X == 'line' and Y == 'aplicacion_line':
        return True
    elif X == 'messenger' and Y == 'aplicacion_messenger':
        return True
    elif X == 'youtube' and Y == 'plataforma_video_youtube':
        return True
    elif X == 'redes_sociales' and Y == 'aplicacion_redes_sociales':
        return True
    elif X == 'Dapps' and Y == 'aplicacion_descentralizada':
        return True
    elif X == 'NFTs' and Y == 'token_no_fungible':
        return True
    elif X == 'Arch Linux' and Y == 'distro_linux_corporativa':
        return True
    elif X == 'Ubuntu server' and Y == 'distro_ubuntu_server':
        return True
    elif X == 'hdd' and Y == 'disco_duro':
        return True
    elif X == 'ssd' and Y == 'unidad_estado_solido':
        return True
    else:
        return False

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
        mensaje_resultado = f"¡He adivinado tu compañía! Es {resultado}."
    else:
        mensaje_resultado = "No se pudo inferir el elemento."

    engine.say(mensaje_resultado)
    engine.runAndWait()
    messagebox.showinfo("Akinator", mensaje_resultado)