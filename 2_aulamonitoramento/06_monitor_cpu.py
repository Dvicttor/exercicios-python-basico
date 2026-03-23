import psutil
import os

while True:
    os.system("cls")

    total = psutil.cpu_percent(interval=1)
    nucleos = psutil.cpu_percent(interval=1, percpu=True)

    print(f"CPU Total: {total}%\n")

    for i, nucleo in enumerate(nucleos):
        print(f"Núcleo {i}: {nucleo}%")