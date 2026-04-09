# Declaración de constantes
LIMITE_SUPERIOR = 100.0
LIMITE_INFERIOR = 0.0

# Entrada de datos
lectura = float(input("Ingrese la lectura del sensor térmico: "))

# Validación y procesamiento
if LIMITE_INFERIOR <= lectura <= LIMITE_SUPERIOR:
    # Normalización
    dato_normalizado = lectura / LIMITE_SUPERIOR
    print(f"Señal aceptada. Valor normalizado para el modelo: {dato_normalizado}")
else:
    print("Error: Lectura fuera de rango. La señal se considera ruido.")

# Salida final
print("Fin del proceso de filtrado de datos.")