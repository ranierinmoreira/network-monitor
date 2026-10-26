import os
import platform
import subprocess
import sys
from datetime import datetime
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# Garante que emojis sejam exibidos mesmo em consoles Windows com cp1252
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def ping(host: str) -> tuple[bool, float | None]:
    """
    Retorna (status, tempo_ms).
    status = True se o host respondeu, False se não respondeu
    tempo_ms = tempo de resposta em ms ou None se falhou
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            capture_output=True,
            text=True,
            errors="replace"  # saída do ping no Windows usa codepage OEM (ex: cp850)
        )
        if result.returncode == 0:
            # Extrai tempo de resposta
            if platform.system().lower() == "windows":
                for line in result.stdout.splitlines():
                    if "tempo=" in line:
                        tempo = line.split("tempo=")[-1].split("ms")[0].strip()
                        return True, float(tempo)
            else:
                for line in result.stdout.splitlines():
                    if "time=" in line:
                        tempo = line.split("time=")[-1].split(" ")[0]
                        return True, float(tempo)
            return True, None
        else:
            return False, None
    except Exception:
        return False, None

def load_hosts(file_path: str):
    """Lê a lista de hosts de um arquivo txt"""
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def salvar_log(mensagem: str, log_file: str = "monitor.log"):
    """Grava mensagens no arquivo de log com data/hora"""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(mensagem + "\n")

if __name__ == "__main__":
    hosts = load_hosts("host.txt")

    for host in hosts:
        status, tempo = ping(host)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if status:
            msg = f"{timestamp} | {host}: ONLINE ✅ - {tempo} ms"
            print(f"{host}: {Fore.GREEN}ONLINE ✅{Style.RESET_ALL} - {tempo} ms")
        else:
            msg = f"{timestamp} | {host}: OFFLINE ❌"
            print(f"{host}: {Fore.RED}OFFLINE ❌{Style.RESET_ALL}")

        salvar_log(msg)
