import psutil
import platform

print("=== INFORMAÇÕES DO PROCESSADOR ===")

print("Modelo:", platform.processor())
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos lógicos:", psutil.cpu_count(logical=True))

freq = psutil.cpu_freq()
print("Frequência atual:", f"{freq.current:.2f} MHz")

print("\nNúmero de série da CPU geralmente não é acessível pelo sistema operacional.")