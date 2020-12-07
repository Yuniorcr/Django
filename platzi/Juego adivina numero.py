import random

def run():
    Numero_aleatorio = random.randint(1, 100)
    numero_ingresado = int(input("ingrese un numero: "))
    vida = 5
    while numero_ingresado != Numero_aleatorio and vida != 0:
        if numero_ingresado < Numero_aleatorio:
            print("ingrese un numero mas grande")
            vida -= 1 
        else:
            print("ingrese un numero menor")
            vida -= 1
        print("vidas restantes: ",vida+1)
        numero_ingresado = int(input("ingrese numero: "))
    if vida >0:
        print("ganaste")
    else:
        print("Perdiste, el numero era: ", Numero_aleatorio)
        
if __name__ == "__main__":
    run()
