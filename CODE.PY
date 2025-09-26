import subprocess
import time

SERVER = "minecraft.server.address"   # coloque IP/host
THRESHOLD_MS = 200  # se ping > 200ms, aplica medidas
CHECK_INTERVAL = 30  # segundos

def ping_ms(host):
    try:
        # comando ping no Windows: -n 1
        out = subprocess.check_output(["ping", "-n", "1", host], universal_newlines=True)
        # procura "Tempo = XXms" (pt-BR) ou "time=XXms"
        import re
        m = re.search(r"(?:Tempo = |time=)(\d+)", out)
        if m:
            return int(m.group(1))
    except subprocess.CalledProcessError:
        return None
    return None

def run_fix_actions():
    print("Rodando ações de otimização...")
    subprocess.call(["ipconfig", "/flushdns"])
    subprocess.call(["netsh", "winsock", "reset"])
    subprocess.call(["netsh", "int", "ip", "reset"])
    # não renova ip automaticamente para evitar perda de conexão inesperada
    print("Acoes concluídas. Reinicie se necessario.")

if __name__ == "__main__":
    while True:
        rtt = ping_ms(SERVER)
        print(time.strftime("%Y-%m-%d %H:%M:%S"), "Ping:", rtt)
        if rtt is None:
            print("Ping falhou.")
        elif rtt > THRESHOLD_MS:
            print(f"Ping alto ({rtt} ms) — executando correcoes...")
            run_fix_actions()
        time.sleep(CHECK_INTERVAL)
