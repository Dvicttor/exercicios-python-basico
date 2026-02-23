import psutil
import time
import os

antigo = psutil.net_io_counters()

while True:
    time.sleep(1)
    os.system("cls")

    novo = psutil.net_io_counters()

    download = (novo.bytes_recv - antigo.bytes_recv) / 1024
    upload = (novo.bytes_sent - antigo.bytes_sent) / 1024

    print(f"Download: {download:.2f} KB/s")
    print(f"Upload: {upload:.2f} KB/s")

    antigo = novo