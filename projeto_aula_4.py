capacidade = int(input("Qual é a capacidade máxima do transporte? "))
pessoas = int(input("Quantas pessoas vão embarcar? "))

if pessoas <= capacidade:
    print("Tudo certo! O transporte pode seguir viagem.")
else:
    print("Capacidade excedida! Não é possível seguir viagem.")
    print("Excedeu por", pessoas - capacidade, "pessoa(s).")
