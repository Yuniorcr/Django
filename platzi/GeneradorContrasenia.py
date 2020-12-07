import random
def generate_password():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoM = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    caracteres = '!@#$%^&*()_+/.,'

    conbinado = alfabeto + alfabetoM + caracteres
    password =''
    for i in range(15):
        passw = random.choice(conbinado)
        password += passw
    return password
def run():
    password = generate_password()
    print("tu nueva password es: ", password)

if __name__ == "__main__":
    run()
