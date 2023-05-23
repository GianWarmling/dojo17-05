import random

user_points = 0
computer_points = 0

opcao = ["Rocha", "Tesoura", "Papel"]

while True:
    user_choice = input("Escolha:\nR (PEDRA)\nP (PAPEL)\nT (TESOURA)\nOu Q para Sair\n-> ").upper()

    if user_choice == 'Q':
        break

    if user_choice not in ['R', 'P', 'T']:
        continue

    computer_choice = random.randint(0, 2)
    computer_opcao = opcao[computer_choice]

    print("O computador escolheu: " + computer_opcao)

    if user_choice == computer_opcao[0]:
        print("Empate!")
    elif (user_choice == 'R' and computer_opcao == "Tesoura") or (user_choice == 'P' and computer_opcao == "Rocha") or (user_choice == 'T' and computer_opcao == "Papel"):
        print("Você Ganhou!")
        user_points += 1
    else:
        print("Você perdeu!")
        computer_points += 1

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if user_points > computer_points:
    print("Vitória!")
elif computer_points == user_points:
    print("Empate!")
else:
    print("Derrota!")