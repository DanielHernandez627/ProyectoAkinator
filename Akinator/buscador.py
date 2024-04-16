import json

# Cargar el árbol de taxonomía desde el JSON
with open('taxonomia.json', 'r') as file:
    taxonomia = json.load(file)

# Predicados para cada nivel y dato en la taxonomía
def nivel_1(X):
    return X == 'bic' or X == 'tec'

def nivel_2(X, Y):
    if X == 'bic':
        return Y == 'software' or Y == 'hardware'
    elif X == 'tec':
        return Y == 'software' or Y == 'hardware'

def nivel_3(X, Y):
    if X == 'software':
        return Y == 'internet' or Y == 'so'
    elif X == 'hardware':
        return Y == 'dispositivos' or Y == 'componentes'

def nivel_4(X, Y):
    if X == 'internet':
        return Y == 'motor de busqueda' or Y == 'web 2' or Y == 'web 3'
    elif X == 'so':
        return Y == 'movil' or Y == 'escritorio'

def nivel_5(X, Y):
    if X == 'motor de busqueda':
        return Y == 'web 2' or Y == 'web 3'
    elif X == 'movil':
        return Y == 'Abierto' or Y == 'Cerrado'
    elif X == 'escritorio':
        return Y == 'abierto' or Y == 'cerrado'

def nivel_6(X, Y):
    if X == 'web 2':
        return Y == 'open surce'
    elif X == 'web 3':
        return Y == 'Dapps' or Y == 'NFTs'
    elif X == 'Abierto':
        return Y == 'Android' or Y == 'Sailfish Os'
    elif X == 'Cerrado':
        return Y == 'Android'

def nivel_7(X, Y):
    if X == 'open surce':
        return Y == 'firefox' or Y == 'opera'
    elif X == 'Dapps':
        return Y == {}
    elif X == 'NFTs':
        return Y == {}
    elif X == 'Android':
        return Y == {}
    elif X == 'Sailfish Os':
        return Y == {}
    elif X == 'firefox':
        return Y == {}
    elif X == 'opera':
        return Y == {}

# Reglas de inferencia interrelacionadas basadas en la taxonomía
def es_consecuente(X, Y):
    # Reglas para cada nivel y dato en la taxonomía
    if nivel_1(X):
        return nivel_2(X, Y)
    elif nivel_2(X, Y):
        return nivel_3(X, Y)
    elif nivel_3(X, Y):
        return nivel_4(X, Y)
    elif nivel_4(X, Y):
        return nivel_5(X, Y)
    elif nivel_5(X, Y):
        return nivel_6(X, Y)
    elif nivel_6(X, Y):
        return nivel_7(X, Y)
    else:
        return False

# Función para realizar la inferencia basada en las reglas de taxonomía con backtracking
def inferir_elemento(caracteristicas, nodo_actual):
    if not caracteristicas:
        respuesta_final = input(f"¿El elemento es '{nodo_actual}'? (1 para sí / 2 para no): ")
        if respuesta_final == '1':
            return nodo_actual  # Éxito en la inferencia
        else:
            return None  # Falla en la inferencia, se realizará backtracking

    pregunta = next(iter(caracteristicas))  # Obtener la primera característica para la pregunta
    respuesta = input(f"¿El elemento tiene la característica '{pregunta}'? (1 para sí / 2 para no): ")

    if respuesta == '1':
        siguiente_nodo = caracteristicas[pregunta]
        return inferir_elemento(siguiente_nodo, pregunta)  # Recursivamente continuar la inferencia
    elif respuesta == '2':
        caracteristicas_restantes = {carac: caracteristicas[carac] for carac in caracteristicas if carac != pregunta}
        if not caracteristicas_restantes:
            return None  # Si no quedan más características, regresar None (falla en la inferencia)

        # Probar con las características restantes (backtracking)
        for caracteristica in caracteristicas_restantes:
            siguiente_nodo = caracteristicas_restantes[caracteristica]
            resultado = inferir_elemento(siguiente_nodo, caracteristica)  # Probar con cada característica restante
            if resultado:
                return resultado
        
        return None  # Si no se encontró ningún elemento, regresar None (falla en la inferencia)
    else:
        print("Respuesta no válida. Por favor responda '1' para sí o '2' para no.")
        return inferir_elemento(caracteristicas, nodo_actual)  # Volver a solicitar la respuesta
