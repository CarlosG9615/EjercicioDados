from rich.console import Console
from rich.table import Table
from rich.live import Live
from time import sleep
import random

console = Console()

def tirar_dado(sides: int, count: int):
    results = [random.randint(1, sides) for _ in range(count)]
    return results

def animacion_tirada(sides: int, count: int):
    with Live("🎲 Tirando...", refresh_per_second=20) as live:
        for i in range(20):
            live.update(f"🎲 Tirando... {i+1}/20")
            sleep(0.05)
        live.update("Fin de la tirada")