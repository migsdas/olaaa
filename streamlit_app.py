import time
import os
from colorama import Fore, Style, init
import itertools

init(autoreset=True)

mensagem = [
    "╔══════════════════════════╗",
    "║                          ║",
    "║    VOCÊ É INCRÍVEL!     ║",
    "║      NUNCA SE ESQUEÇA   ║",
    "║                          ║",
    "╚══════════════════════════╝"
]

cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def exibir_cartao():
    for cor in itertools.cycle(cores):
        os.system("cls" if os.name == "nt" else "clear")
        for linha in mensagem:
            print(cor + linha)
        time.sleep(0.3)

try:
    exibir_cartao()
except KeyboardInterrupt:
    print(Style.RESET_ALL + "\nFechando cartão. Até mais!")
