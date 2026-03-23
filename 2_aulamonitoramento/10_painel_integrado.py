import psutil
import time
import os

while True:
    os.system("cls")

    memoria = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    disco = psutil.disk_usage("C:\\")
    rede1 = psutil.net_io_counters()
    time.sleep(1)
    rede2 = psutil.net_io_counters()

    download = (rede2.bytes_recv - rede1.bytes_recv) / 1024
    upload = (rede2.bytes_sent - rede1.bytes_sent) / 1024

    print("=== PAINEL DE MONITORAMENTO ===\n")

    print(f"RAM: {memoria.percent}% usado")
    print(f"CPU: {cpu}%")
    print(f"Disco C: {disco.percent}% usado")
    print(f"Download: {download:.2f} KB/s")
    print(f"Upload: {upload:.2f} KB/s")

    time.sleep(2)