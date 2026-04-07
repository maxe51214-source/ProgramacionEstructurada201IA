# --- PROGRAMA DE SUMA POR RANGO (10-50) ---

suma = 0

while True:
    try:
        # Leer numero
        entrada = input("Ingresa un número (10 a 50 para sumar, cualquier otro para finalizar): ")
        numero = float(entrada)
        
        # ¿numero >= 10 Y numero <= 50?
        if numero >= 10 and numero <= 50:
            # Sí: suma = suma + numero y volver a leer
            suma += numero
            print(f"Número aceptado. Suma actual: {suma}")
        else:
            # No: Mostrar suma y Fin
            print("Número fuera de rango. Finalizando...")
            break
            
    except ValueError:
        print("Error: Por favor ingresa un número válido.")

# Mostrar suma
print("-" * 30)
print(f"SUMA TOTAL: {suma}")
print("Fin")