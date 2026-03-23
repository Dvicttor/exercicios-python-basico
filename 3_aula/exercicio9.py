prestacao = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros (%): "))
dias = int(input("Digite o número de dias de atraso: "))

# Cálculo
juros = (prestacao * taxa * dias) / 100
nova_prestacao = prestacao + juros

# Saída
print("Nova prestação =", nova_prestacao)


