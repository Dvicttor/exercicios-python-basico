import random

numero = random.randint(1, 100)
tentativas = 0

print("Jogo de Adivinhação (1 a 100)")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero:
        print("Maior!")
    else:
        print("Menor!")