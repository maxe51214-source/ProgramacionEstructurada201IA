# Inicialización de variables
saldo = 0
meta = 1000

# El bucle continúa mientras el saldo NO sea mayor a la meta
while not (saldo > meta):
    # Leer deposito (entrada del usuario)
    try:
        deposito = float(input("Ingrese el monto del depósito: "))
        
        # saldo = saldo + deposito
        saldo += deposito
        
        # Condición: ¿saldo > meta?
        if saldo > meta:
            # Si la respuesta es Sí
            print("Meta superada")
            print(f"Saldo final: {saldo}")
        else:
            # Si la respuesta es No, el bucle vuelve a empezar (Leer deposito)
            print(f"Saldo actual: {saldo}. Aún no alcanzas la meta de {meta}.")
            
    except ValueError:
        print("Por favor, ingrese un número válido.")

print("Fin del programa")