import os
import platform
import subprocess

def ping(host: str) -> bool:
    """
    Retorna True se o host responder ao ping, senão False.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

if __name__ == "__main__":
    hosts = ["8.8.8.8", "1.1.1.1", "github.com"]

    for host in hosts:
        status = "ONLINE ✅" if ping(host) else "OFFLINE ❌"
        print(f"{host}: {status}")
