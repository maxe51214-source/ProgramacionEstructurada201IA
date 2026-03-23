def verificar_sincronizacion_agentes():
    """
    Determina si la frecuencia de un agente es divisor exacto de la otra
    para establecer una Relación de Sincronización de Ciclos.
    """
    print("--- SISTEMA DE COMUNICACIÓN MULTI-AGENTE ---")
    
    try:
        # 1. Solicitar frecuencias
        freq_a = float(input("Ingrese la frecuencia del Agente A (Hz): "))
        freq_b = float(input("Ingrese la frecuencia del Agente B (Hz): "))

        # 2. Validar que las frecuencias sean mayores a cero
        if freq_a <= 0 or freq_b <= 0:
            print("Error: Las frecuencias deben ser valores mayores a 0 Hz.")
            return

        print(f"\nAnalizando: Agente A ({freq_a} Hz) vs Agente B ({freq_b} Hz)...")

        # 3. Lógica de Sincronización (Divisor exacto)
        # Usamos el operador módulo (%) que devuelve el residuo de la división.
        # Si el residuo es 0, es un divisor exacto.
        
        es_a_divisor_de_b = (freq_b % freq_a == 0)
        es_b_divisor_de_a = (freq_a % freq_b == 0)

        if es_a_divisor_de_b or es_b_divisor_de_a:
            print("✅ ESTADO: SINCRONIZACIÓN PERFECTA DETECTADA.")
            
            if es_a_divisor_de_b:
                print(f"El Agente A es un divisor exacto del Agente B.")
            else:
                print(f"El Agente B es un divisor exacto del Agente A.")
                
            print("El intercambio de mensajes será armónico y sin desfase.")
        else:
            print("❌ ESTADO: SINCRONIZACIÓN NO ALCANZADA.")
            print("Las frecuencias no son divisores exactos entre sí.")
            print("Se requiere un buffer de compensación para la comunicación.")

    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

# Ejecutar la función
if __name__ == "__main__":
    verificar_sincronizacion_agentes()