from controller01 import saudacao, Create, relatorioHospedes, relatorioHospede, FazerCheckout

def menu():
    menu = 1
    while menu != 0:
        saudacao()
        print("O que você deseja?")

        var = int(input("Digite 1- Para cadastro:\nDigite 2- Leitura:\nDigite 3- Leitura de Hóspede:\nDigite 4- Deletar Hóspede:\n>> "))

        match var:

            case 1:
                pessoa = {}

                pessoa["Nome"] = input("Digite seu nome: ")

                pessoa["Sobrenome"] = input("Digite seu sobrenome: ")

                pessoa["Idade"] = int(input("Digite sua idade: "))

                pessoa["Telefone"] = input("Digite seu telefone: ")

                Create(pessoa)

            case 2:
                relatorioHospedes()

            case 3:
                pessoa = input("Digite o nome que deseja: ")
                relatorioHospede(pessoa)
        
            case 4:
                pessoa = input("Digite o nome da pessoa que deseja Deletar: ")
                FazerCheckout(pessoa)
        
        menu = int(input("Você deseja sair?\n1 - Para Continuar\n0 - Para Sair\n"))

menu()