# calculo del factorial de un numero
def calculo():
    numero = (int) (input("ingresa un numnero"))
    factorial = 1 
    i = 1 
    while i<= numero:
        factorial = factorial*i
        i=i + 1
    return factorial

def main():
    resultado= calculo()
    print("el resultado es",resultado)
   
if __name__=="__main__":
    main()






















    