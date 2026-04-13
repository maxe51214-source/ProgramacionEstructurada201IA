#Limpiez de datos, normalizacion

# ClasificadoPixeles.py
def main():
    clasificar_pixel()
# Declaracion de constantes
UMBRAL_BAJO = 0.3
UMBRAL_ALTO = 0.7

def clasificar_pixel():
    #solicitar datos al usuario
    intensidad = float(input("Ingrese la intensidad del pixel (0.0 a 0.1): "))
    
    #Si la intensidad es menor a 0.0 o mayor a 1.0 es un valor invalido
    if intensidad < 0.0 or intensidad > 1.0:
        print("Error: Valor de pixel invalido")
        return
    
    #Clasificacion del pixel
    if 0.0 <= intensidad <= UMBRAL_BAJO:
        print("Clasificacion (Fodo oscuro):")
        return

    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        print("Clasificacion (Fodo gris):")
        return

    if intensidad >= UMBRAL_ALTO:
        print("Clasificacion (Fodo brillante):")
        return

    print("Analisis de imagen finalizado.")

if __name__ == "__main__":
    main()