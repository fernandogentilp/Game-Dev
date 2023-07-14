def missao_goblins():
    print("Eu vou matar goblins!")

def missao_coleta():
    print("Eu vou coletar materiais!")

def resgatar():
    print("Eu vou resgatar inocentes!")

def main():
    print("Olá aventureiro! No que posso ajudar?")
    print("")
    print("Missões:")
    print("1 - matar goblins.")
    print("2 - coletar materiais.")
    print("3 - resgatar inocentes.")
    resposta = input("Eu escolho: ")
    if resposta == "1":
        missao_goblins()
    elif resposta == "2":
        missao_coleta()
    elif resposta == "3":
        resgatar()
    else:
        print("Hohoho, não existe essa missão!")

while True:
    main()