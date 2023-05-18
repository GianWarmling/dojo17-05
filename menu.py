from controller import saudacao, create, relatoriohospede

def menu():
    menu = 1
    while menu != 0:
        saudacao()
        print("O que você deseja?")

        var = int(input("Digite 1- Para cadastro\nDigite 2- Leitura\nDigite 3- Leitura de Hóspede\nDigite 4- Deletar Hóspede\n>> "))

        match var:

            case 1:
                pessoa = {}

                pessoa["Nome"] = input("Digite seu nome: ")

                pessoa["Sobrenome"] = input("Digite seu sobrenome: ")

                pessoa["Idade"] = int(input("Digite sua idade: "))

                pessoa["Telefone"] = input("Digite seu telefone: ")

                create(pessoa)

            case 2:
                relatoriohospede()

            case 3:
                print("Leitura Hóspede!")
        
            case 4:
                print("Deletar!")
        
        menu = int(input("Você deseja sair?\n1 - Para Continuar\n2 - Para Sair\n"))





menu()