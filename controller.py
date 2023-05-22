from datetime import datetime

def saudacao():
    hora = datetime.now(tz=None)
    if hora.hour >= 5 and hora.hour < 12:
        print("Bom Dia")

    elif hora.hour >= 12 and hora.hour < 18:
        print("Boa Tarde!")
    
    else:
        print("Boa Noite!")

def create(cliente):    
    with open ('hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+ '\n')

def relatoriohospedes():
    with open('hotel.txt', 'r') as arquivo:
        print(arquivo.read())

def relatorioHospede(Clientefind):
    
    index = 0

    flag = 0

    arquivo = open("hotel.txt", "r")

    for line in arquivo:

        index += 1

        if Clientefind == eval(line)["Nome"]:
            print(line)
            flag = 1
    
    if flag == 0:
        print("Cliente não Encontrado!")

def FazerCheckout(cliente):
    index = 0 
    flag = 0

    arquivo = open("hotel.txt", "r")

    for line in arquivo:
        index += 1

        if cliente == eval(line)["Nome"]:

            chave = index

            flag = 1

    arquivo.close()

    if flag == 0:
        print("Cliente nao encontrado")

    else:

        try:
            with open("hotel.txt", "r") as arquivo:
                lines = arquivo.readlines()

                posicao = 1

                with open("hotel.txt", "w") as arquivo:
                    for line in lines:
                        if posicao != chave:
                            arquivo.write(line)

                        posicao += 1
            print("Pessoa Deletada")

        except:
            print("Erro Sistema")