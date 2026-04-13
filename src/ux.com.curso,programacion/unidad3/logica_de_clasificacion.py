# asistente_logico.py

# Configuración de variables
nombre_asistente = "IA-UX"

print(f"¡Bienvenido! Soy {nombre_asistente}, tu asistente virtual.")

# Entrada de datos
frase = input("¿En qué puedo ayudarte hoy?: ").lower()

# Lógica de clasificación
if "hola" in frase or "buenos días" in frase:
    print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

elif "clima" in frase or "temperatura" in frase:
    print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

elif "hora" in frase or "tiempo" in frase:
    print("La hora actual del sistema es: 12:00 PM")  # Puedes cambiarla por una real si quieres

else:
    print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

# Despedida
print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")