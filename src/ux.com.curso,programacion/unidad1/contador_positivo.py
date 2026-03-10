# Desarrollo de algoritmo contador positivo
def contador_positivos():
    contador=0
    while True:
        numero = int(input("ingrese un número (-1 para terminar): "))
        if numero <0:
            break
    contador += 1

    print("cantidad de numeros positivos ingresados: ",contador)

# definicion de la funcion de main (controla el flujo del programa)
def main():
    print("bienvenido al contador de positivos")
    contador_positivos()

    #llamada a la funcion main para iniciar el programa
    if __name__ == "__main__":
        main()
