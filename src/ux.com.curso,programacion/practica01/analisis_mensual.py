# 1. IMPORTACIÓN
# Importamos la biblioteca externa NumPy y le asignamos el alias 'np'
import numpy as np

def procesar_estadisticas(lista_mensajes):
    """
    Función que recibe datos y utiliza funciones externas
    de NumPy para procesarlos.
    """

    # Promedio
    promedio = np.mean(lista_mensajes)

    # Valor máximo
    pico_maximo = np.max(lista_mensajes)

    # Desviación estándar
    desviacion = np.std(lista_mensajes)

    # Redondear desviación a 1 decimal
    desviacion_redondeada = np.round(desviacion, 1)

    # Mediana
    mediana = np.median(lista_mensajes)

    return promedio, pico_maximo, desviacion_redondeada, mediana


# --- Programa Principal ---

# Datos: mensajes enviados por hora durante 8 horas
datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]

# Llamada a la función
prom, maximo, ds, med = procesar_estadisticas(datos_servidor)

# Reporte final
print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
print(f"Promedio de mensajes por hora: {prom:.2f}")
print(f"Pico de actividad registrado: {maximo} mensajes")
print(f"Variabilidad del tráfico (Desviación): {ds}")
print(f"Mediana de mensajes: {med}")


# OBSERVACIÓN:
# Si intentamos usar funciones como np.mean() sin hacer
# 'import numpy as np', Python genera un error llamado:
# NameError: name 'np' is not defined
# porque el programa no reconoce qué es 'np'.