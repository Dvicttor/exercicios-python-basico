import psutil
import time
import os

while True:
    os.system("cls")
    memoria = psutil.virtual_memory()

    total = memoria.total / (1024 ** 3)
    usado = memoria.used / (1024 ** 3)
    livre = memoria.available / (1024 ** 3)

    print("=== MONITOR DE MEMÓRIA RAM ===")
    print(f"Total: {total:.2f} GB")
    print(f"Usado: {usado:.2f} GB")
    print(f"Livre: {livre:.2f} GB")
    print(f"Percentual usado: {memoria.percent}%")

    time.sleep(2) 