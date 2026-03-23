# 4 - Leia um número e imprima a tabuada dele (1 a 10)

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
