# --- PROGRAMA DE SUMA ACUMULADA ---

suma = 0

while suma <= 500:
    try:
        # Leer numero
        entrada = input("Ingresa un número para sumar: ")
        numero = float(entrada)
        
        # suma = suma + numero
        suma += numero
        
        print(f"Suma actual: {suma}")
        
    except ValueError:
        print("Error: Por favor ingresa un número válido.")

# Mostrar suma final cuando sea > 500
print("-" * 30)
print(f"¡Hecho! La suma final es: {suma}")
print("Fin del programa.")