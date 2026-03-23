raio = float(input("Digite o valor do raio: "))
altura = float(input("Digite o valor da altura: "))

# Constante de π
pi = 3.14

# Cálculo da área da base
area_base = pi * (raio ** 2)

# Cálculo do volume do cone
volume = (area_base * altura) / 3

# Saída
print("Volume do cone =", volume)
