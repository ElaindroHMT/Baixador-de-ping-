# Baixador-de-ping-
Isso vai baixar seu Ping por completo em qualquer jogo ate Minecraft e vai te ajudar a baixa tbm a Latencia


## ✨ Sobre Eliandro
Eu sou uma pessoa desenvolvedora full-stack...

Oi sou programador de python Sou um Junior que quer facilitar sua vida na program,ação do mercado
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


## Instalação

Instale my-project com npm

```bash
  pip install pyinstaller

pyinstaller --onefile ping_guard.py

```
    
## cmd 1,2,3,4

## Script.bat

@echo off
echo Limpando DNS...
ipconfig /flushdns

echo Renovando IP...
ipconfig /release
timeout /t 2 >nul
ipconfig /renew

echo Reset Winsock...
netsh winsock reset

echo Reset interface TCP/IP...
netsh int ip reset

echo Operacao concluida. Reinicie o computador se for solicitado.
pause

## set DNS

@echo off
rem Troque "Ethernet" por "Wi-Fi" se usar wifi
set IFACE=Ethernet

echo Definindo DNS primario 1.1.1.1 e secundario 1.0.0.1 para %IFACE%...
netsh interface ip set dns name="%IFACE%" static 1.1.1.1
netsh interface ip add dns name="%IFACE%" 1.0.0.1 index=2

echo DNS atualizado.
ipconfig /flushdns
pause

## APPS.bat

@echo off
echo Fechando apps comuns (Discord, Steam, OBS, navegadores)...
taskkill /IM Discord.exe /F
taskkill /IM steam.exe /F
taskkill /IM obs64.exe /F
taskkill /IM chrome.exe /F
taskkill /IM firefox.exe /F

echo Feitos. Tenha cuidado: isso fecha processos sem salvar.
pause

## LOG.bat

@echo off
set SERVER=minecraft.server.address
set LOG=ping_log.txt

echo Testando ping para %SERVER%...
for /f "tokens=6 delims== " %%a in ('ping -n 1 %SERVER% ^| find "Tempo"') do set RTT=%%a
echo %date% %time% - %SERVER% - %RTT% >> %LOG%
type %LOG%
pause


## CODE PYTHON

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

