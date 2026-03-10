# ejemplo para visualizar la indentacion en python

def explicar_identacion():
    #nivel 1
    mensaje = "Nivel 1 de identacion"
    print(mensaje)
    
    puntos = 10
    
    if puntos > 9:
        #nivel 2
        print("entra el flujo de if")
        
        if puntos == 10:
            #nivel 3
            print("puntos es igual a 10")
            
    # cierre del nivel 1

# definicion de la funcion main para iniciar el programa
def main():
    explicar_identacion()

# Llamada a la funcion main para iniciar el programa
if __name__ == "__main__":
    main()