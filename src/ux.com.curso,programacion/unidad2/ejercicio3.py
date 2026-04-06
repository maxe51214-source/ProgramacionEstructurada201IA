# Leer N (Entrada de usuario)
n = int(input("Ingrese la cantidad de números impares a mostrar (N): "))

# Inicialización de variables
contador = 0
numero = 1

# Estructura de control: ¿contador < N?
while contador < n:
    # Imprimir numero
    print(numero)
    
    # numero = numero + 2
    numero = numero + 2
    
    # contador = contador + 1
    contador = contador + 1

# Fin