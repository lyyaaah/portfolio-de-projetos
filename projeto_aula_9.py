numero_secreto = 17  # escolha o número

for tentativa in range(1, 5 + 1):
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

else:
    print("Você perdeu!")
    print("O número correto era", numero_secreto)
