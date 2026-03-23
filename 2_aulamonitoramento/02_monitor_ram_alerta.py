import psutil
import time
import os

limite = float(input("Digite o limite de uso da RAM (%): "))

while True:
    os.system("cls")
    memoria = psutil.virtual_memory()

    print(f"Uso atual: {memoria.percent}%")

    if memoria.percent > limite:
        print("⚠ ALERTA: Uso de memória acima do limite!")

    time.sleep(2)