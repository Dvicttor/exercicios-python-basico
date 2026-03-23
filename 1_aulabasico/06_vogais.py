# 6 - Leia uma frase e informe quantas vogais existem

frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase possui {contador} vogais.")
