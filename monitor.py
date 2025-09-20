import os
import platform
import subprocess

def ping(hots: str) -> bool:

    param = "-n" if platform.system().lower() == "windows" ele "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
        )