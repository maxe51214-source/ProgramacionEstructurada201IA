"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: [Tu Nombre]
"""

import random
import statistics  # Se agregó para utilizar funciones estadísticas optimizadas


# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):

    # Mejora:
    # Se reemplazó la eliminación manual de espacios por strip(),
    # una función integrada más eficiente y legible.
    nombre_limpio = nombre_sucio.strip()

    # Mejora:
    # Se reemplazó la manipulación manual de códigos ASCII
    # por capitalize(), que convierte la primera letra a mayúscula
    # y el resto a minúsculas.
    return nombre_limpio.capitalize()


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):

    # Mejora:
    # Se reemplazó la búsqueda manual carácter por carácter
    # por el operador "in", diseñado específicamente para
    # buscar subcadenas dentro de otra cadena.
    return palabra_prohibida in mensaje_chat


# =====================================================================
# RETO 3: Generador de Contraseñas Temporales
# =====================================================================
def generar_clave_temporal():

    caracteres_validos = (
        "ABCDEFGHJKLMNPQRSTUVWXYZ"
        "abcdefghijkmnpqrstuvwxyz"
        "23456789"
    )

    # Mejora:
    # Se reemplazó la concatenación repetitiva dentro de un ciclo
    # por join() y una comprensión generadora.
    # Esto es más eficiente y profesional.
    return "".join(
        random.choice(caracteres_validos)
        for _ in range(8)
    )


# =====================================================================
# RETO 4: Mediana de Latencia de Red
# =====================================================================
def calcular_mediana_latencia(lista_pings):

    # Mejora:
    # Se eliminó el algoritmo Burbuja implementado manualmente.
    # La librería statistics ya incluye el cálculo de la mediana.
    return statistics.median(lista_pings)


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    print("--- Probando Código Refactorizado (Parte II) ---")

    print(
        "Usuario limpio:",
        [limpiar_nombre_usuario("   luNA_eDUaRDo  ")]
    )

    msg = "No digas malas palabras en este servidor"

    print(
        "¿Tiene groserías?:",
        contiene_palabra_bloqueada(msg, "malas")
    )

    print(
        "Clave generada por el sistema:",
        generar_clave_temporal()
    )

    pings_servidor = [120, 45, 80, 23, 150, 62]

    print(
        "Mediana de latencia encontrada:",
        calcular_mediana_latencia(pings_servidor)
    )