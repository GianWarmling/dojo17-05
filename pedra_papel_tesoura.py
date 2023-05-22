import random

user_points = 0
computer_points = 0


opcao = ["Rocha", "Tesoura", "Papel"]


while True:
    user_choice = input("Escolha:\nR (PEDRA)\nP (PAPEL\nT (TESOURA)\nOu Q para Sair\n-> ").lower()

    if user_choice == 'q':
        break

    if user_choice not in opcao:
        continue

    computer_choice = random.randint(0, 2)
    
    computer_opcao = opcao[computer_choice]

    print("O computador escolheu: " + computer_opcao)

    if user_choice == computer_opcao:
        print("Empate!")

    elif user_choice == "r" and computer_opcao == "t":
        print("Você Ganhou!")
        user_points = user_points +1
        
    elif user_choice == "p" and computer_opcao == "r":
        print("Você Ganhou!")
        user_points = user_points +1

    elif user_choice == "t" and computer_opcao == "p":
        print("Você Ganhou!")
        user_points = user_points +1
    
    else:
        print("Você perdeu!")
        computer_points = computer_points +1

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if user_points > computer_points:
    print("Vitória!!!!")

elif computer_points == user_points:
    print("Empate!")

else:
    print("Derrota!!")
