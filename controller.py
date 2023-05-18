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

def relatoriohospede():
    with open('hotel.txt', 'r') as arquivo:
        print(arquivo.read())
