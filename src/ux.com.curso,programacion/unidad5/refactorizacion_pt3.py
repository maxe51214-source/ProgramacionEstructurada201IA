"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: [Tu Nombre]
"""

import math

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# =====================================================================
def inicializar_tablero_vacio():

    # Mejora:
    # Se reemplazó la creación de filas con referencias compartidas
    # por una comprensión de listas que genera filas independientes.
    # Esto evita que modificar una fila modifique todas las demás.
    tablero = [[0 for _ in range(4)] for _ in range(4)]

    # Se eliminó el ciclo posterior que volvía a asignar ceros,
    # ya que el tablero nace correctamente inicializado.
    return tablero


# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping)
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):

    # Mejora:
    # Se sustituyó la estructura if-else anidada por una expresión
    # usando min() y max(), mucho más compacta y profesional.
    return max(minimo, min(valor_lectura, maximo))


# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero
# =====================================================================
def buscar_error_minimo(lista_errores):

    # Mejora:
    # Se eliminó el número arbitrario 999999.99.
    # También se sustituyó el cálculo manual del valor absoluto
    # por la función integrada abs().

    return min(abs(error) for error in lista_errores)


# =====================================================================
# RETO 4: Filtro de Valores Únicos
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):

    # Mejora:
    # Se eliminó el algoritmo de búsqueda doblemente anidado.
    # dict.fromkeys() elimina duplicados conservando el orden original.
    return list(dict.fromkeys(lista_ids))


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    print("--- Probando Código Refactorizado (Parte III) ---")

    tablero_ia = inicializar_tablero_vacio()

    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)

    print(
        "Lectura recortada (125.4 en rango 0-100):",
        limitar_senal_sensor(125.4, 0.0, 100.0)
    )

    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]

    print(
        "El error más cercano a cero es:",
        buscar_error_minimo(errores_entrenamiento)
    )

    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]

    print(
        "Lista de IDs únicas filtradas:",
        depurar_usuarios_repetidos(ids_discord)
    )