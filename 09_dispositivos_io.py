import psutil

print("=== DISPOSITIVOS DE ARMAZENAMENTO ===")

particoes = psutil.disk_partitions()

for i, particao in enumerate(particoes):
    print(f"{i} - {particao.mountpoint}")

escolha = int(input("\nEscolha uma partição: "))

uso = psutil.disk_usage(particoes[escolha].mountpoint)

print("\nDetalhes:")
print(f"Total: {uso.total / (1024**3):.2f} GB")
print(f"Usado: {uso.used / (1024**3):.2f} GB")
print(f"Livre: {uso.free / (1024**3):.2f} GB")