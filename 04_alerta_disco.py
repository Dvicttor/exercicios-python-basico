import psutil

limite = 10  # %

print("=== PARTIÇÕES CRÍTICAS ===")

for particao in psutil.disk_partitions():
    uso = psutil.disk_usage(particao.mountpoint)

    if uso.percent > (100 - limite):
        print(f"{particao.mountpoint} está com pouco espaço! ({uso.percent}% usado)")