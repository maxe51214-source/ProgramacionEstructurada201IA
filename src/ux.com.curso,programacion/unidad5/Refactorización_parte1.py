"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código
Alumno: [Tu Nombre]
"""

import random
import math  # Se agregó para utilizar funciones matemáticas optimizadas

# =====================================================================
# RETO 1: El Teorema de Fermat
# =====================================================================
def verificar_fermat(a, b, c):
    n = 4

    # Mejora:
    # Se simplificó la estructura eliminando un if anidado innecesario.
    # La condición principal ya verifica todo lo necesario.
    if n > 2 and a**n + b**n == c**n:
        print("¡Fermat se equivocó!")
    else:
        print("No, esa combinación no funciona.")


# =====================================================================
# RETO 2: Distancia Euclidiana entre dos puntos
# =====================================================================
def calcular_distancia(x1, y1, x2, y2):
    diferencia_x = x2 - x1
    diferencia_y = y2 - y1

    # Mejora:
    # Se reemplazó el cálculo manual de la raíz cuadrada (**0.5)
    # por math.hypot(), que es más legible, precisa y profesional.
    return math.hypot(diferencia_x, diferencia_y)


# =====================================================================
# RETO 3: Selector Aleatorio de Respuestas para el Bot
# =====================================================================
def obtener_saludo_agente():

    # Mejora:
    # Se reemplazó la cadena de if-elif por una lista y random.choice(),
    # lo que reduce código y facilita agregar nuevos saludos.
    saludos = [
        "Hola, soy el agente de IA. ¿En qué ayudo?",
        "¡Conexión establecida! Listo para operar.",
        "Sistemas en línea. Monitoreando el servidor.",
        "Hola humano, procesando tus peticiones."
    ]

    return random.choice(saludos)


# =====================================================================
# RETO 4: Clasificador de Alertas Críticas
# =====================================================================
def evaluar_error_sistema(valor_loss):

    # Mejora:
    # Se eliminó la anidación excesiva de if-else.
    # El flujo ahora es más claro y fácil de mantener.

    if valor_loss < 0:
        return "Error: Valor negativo inválido"

    if valor_loss < 0.4:
        return "Estable"

    if valor_loss < 0.8:
        return "Advertencia: Gradiente inestable"

    if valor_loss <= 1.0:
        return "CRÍTICO: Abortar entrenamiento"

    return "Error: Valor fuera de rango"


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    print("--- Probando Código Refactorizado ---")

    verificar_fermat(3, 4, 5)

    print("Distancia calculada:",
          calcular_distancia(0, 0, 3, 4))

    print("Respuesta bot:",
          obtener_saludo_agente())

    print("Estado del log:",
          evaluar_error_sistema(0.85))