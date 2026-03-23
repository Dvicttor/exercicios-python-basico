import psutil

print("=== PARTIÇÕES DE DISCO ===")

for particao in psutil.disk_partitions():
    uso = psutil.disk_usage(particao.mountpoint)

    print(f"\nPartição: {particao.mountpoint}")
    print(f"Total: {uso.total / (1024**3):.2f} GB")
    print(f"Usado: {uso.used / (1024**3):.2f} GB")
    print(f"Livre: {uso.free / (1024**3):.2f} GB")
    print(f"Percentual usado: {uso.percent}%")