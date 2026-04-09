# Inicialización
intentos = 0
clave_correcta = "1234"

# Ciclo principal
while intentos < 3:
    contrasena = input("Ingrese clave: ")

    # Validación
    if contrasena == clave_correcta:
        print("Acceso Concedido")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta")

# Bloqueo de cuenta (solo se ejecuta si no hubo break)
if intentos == 3:
    print("Cuenta bloqueada")