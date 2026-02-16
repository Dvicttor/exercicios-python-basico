# 7 - Peça uma quantidade N e leia N números
# Depois mostre o maior, o menor e a média

quantidade = int(input("Quantos números você quer digitar? "))

numeros = []

for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média: {media}")
