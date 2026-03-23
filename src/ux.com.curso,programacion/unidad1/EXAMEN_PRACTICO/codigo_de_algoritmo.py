def simular_entrenamiento_lotes():
    """
    Simula el proceso de carga de lotes de datos (tensores) a la memoria VRAM
    y detiene la carga si se supera un límite de seguridad para evitar un error OOM.
    """

    # 1. Definir constantes
    LIMITE_SEGURIDAD_VRAM_MB = 2500  # Límite en Megabytes (MB)

    # 2. Inicializar variables
    memoria_usada_total = 0
    conteo_lotes = 0

    print("--- SIMULACIÓN DE ENTRENAMIENTO POR LOTES (BATCH TRAINING) ---")
    print(f"Límite de seguridad de VRAM establecido: {LIMITE_SEGURIDAD_VRAM_MB} MB\n")

    # 3. Bucle de carga de lotes
    # El bucle se ejecuta MIENTRAS la memoria usada sea menor que el límite.
    while memoria_usada_total < LIMITE_SEGURIDAD_VRAM_MB:
        
        # Incrementar el contador de lotes para mayor claridad
        conteo_lotes += 1

        try:
            # Solicitar al usuario el ingreso del tamaño del lote en MB
            entrada_usuario = input(f"Ingrese el tamaño del Lote #{conteo_lotes} (en MB), o 'q' para salir: ")
            
            # Opción para salir manualmente si el usuario lo desea
            if entrada_usuario.lower() == 'q':
                break

            # Convertir la entrada a un número flotante (para permitir decimales)
            tamaño_lote = float(entrada_usuario)

            # Validar que el tamaño sea un número positivo
            if tamaño_lote <= 0:
                print("El tamaño del lote debe ser un número positivo. Intente de nuevo.")
                conteo_lotes -= 1 # No contar este lote
                continue

            # Acumular la memoria usada
            memoria_usada_total += tamaño_lote

            # Mostrar el estado actual
            print(f"  > Lote cargado con éxito ({tamaño_lote} MB).")
            print(f"  > Memoria VRAM total cargada: {memoria_usada_total:.2f} MB.")
            
            # Verificar si se superó el límite DESPUÉS de cargar el lote, para dar el aviso exacto
            if memoria_usada_total >= LIMITE_SEGURIDAD_VRAM_MB:
                print(f"\n[ALERTA DETECTADA]")
                print(f"¡Atención! La memoria VRAM acumulada ({memoria_usada_total:.2f} MB) "
                      f"ha alcanzado o superado el límite de seguridad de {LIMITE_SEGURIDAD_VRAM_MB} MB.")
                print("El proceso de carga se detiene inmediatamente para evitar un error de 'Out of Memory' (OOM).")
                # El bucle while se detendrá en la siguiente evaluación de la condición.
            
            # Salto de línea para mejor lectura
            print("-" * 20)

        except ValueError:
            # Manejar errores si el usuario no ingresa un número válido
            print("Entrada no válida. Por favor, ingrese un número (ej. 500 o 250.5).")
            conteo_lotes -= 1 # No contar este intento fallido
            print("-" * 20)

    # 4. Mensaje de fin de la simulación
    print("\n--- RESUMEN FINAL DE LA SIMULACIÓN ---")
    if memoria_usada_total < LIMITE_SEGURIDAD_VRAM_MB and conteo_lotes > 0:
        # Esto ocurre si el usuario salió manualmente o cargó 0 lotes.
         print(f"La carga se detuvo manualmente.")
    else:
         print(f"Estado de la VRAM: LÍMITE DE SEGURIDAD OPERADO (OOM EVITADO).")
    
    print(f"Total de lotes simulados: {conteo_lotes}")
    print(f"Memoria VRAM final utilizada: {memoria_usada_total:.2f} MB / {LIMITE_SEGURIDAD_VRAM_MB} MB")
    print("Simulación finalizada.")

# Ejecutar la función
if __name__ == "__main__":
    simular_entrenamiento_lotes()