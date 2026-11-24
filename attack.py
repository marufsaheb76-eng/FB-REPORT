import os
import sys
import time
import random

# ============== COLORS ==============

RED = "\033[1;31m"
DARK = "\033[31m"
WHITE = "\033[1;97m"
RESET = "\033[0m"

# ============== SETTINGS ==============

LOG_COUNT = 80
LOG_DELAY = 0.25
RELOAD_DURATION = 3


# ============== MARUF BANNER ==============

def logo():
    print(RED + r"""
████╗   ███╗  █████╗  ██████╗  ██╗   ██╗ ███████╗
████╗ ████║ ██╔══██╗ ██╔══██╗ ██║   ██║ ██╔════╝
██╔████╔██║ ███████║ ██████╔╝ ██║   ██║ █████╗
██║╚██╔╝██║ ██╔══██║ ██╔══██╗ ╚██╗ ██╔╝ ██╔══╝
██║ ╚═╝ ██║ ██║  ██║ ██║  ██║  ╚████╔╝  ██
╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝   ╚═══╝
""" + RESET)

    print(RED + "       PREMIUM REPORT ENGINE" + RESET)
    print(RED + "=" * 54 + RESET)


# ============== SCREEN ==============

def clear():
    os.system("clear")


# ============== TARGET ==============

def target():
    print()
    print(RED + "       [1] TARGET URL" + RESET)
    print()

    return input(
        WHITE + "       MARUF@TARGET >> " + RESET
    ).strip()


# ============== RELOAD ==============

def reload():
    print()
    print(RED + "          [ RELOAD PROCESS ]" + RESET)
    print()

    steps = 30

    for i in range(steps + 1):

        percent = int((i / steps) * 100)
        filled = int((i / steps) * 20)
        empty = 20 - filled

        bar = "█" * filled + "░" * empty

        sys.stdout.write(
            f"\r{RED}[{bar}] {percent:03d}%{RESET}"
        )

        sys.stdout.flush()
        time.sleep(RELOAD_DURATION / steps)

    print()
    print(RED + "          [ RELOAD COMPLETE ]" + RESET)


# ============== RANDOM DEVICE ==============

def random_device():
    chars = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
    )

    return "".join(
        random.choices(chars, k=9)
    )


# ============== SIMULATION LOGS ==============

def logs():
    print()
    print(RED + "========== LIVE ATTACK LOGS ==========" + RESET)
    print()

    for i in range(1, LOG_COUNT + 1):

        device = random_device()

        line = (
            f">Device:{device};"
            f"Http-200/Success RP<"
        )

        print(RED + line + RESET, flush=True)

        time.sleep(LOG_DELAY)

    print()
    print(RED + "[ 80/80 ] CYCLE COMPLETED" + RESET)


# ============== MAIN ENGINE ==============

def main():
    clear()
    logo()

    url = target()

    if not url:
        print(RED + "\n[!] URL REQUIRED" + RESET)
        return

    print()
    print(RED + "=" * 54 + RESET)
    print(WHITE + " MODE     : ONLINE ATTACK" + RESET)
    print(WHITE + " TARGET   : " + url + RESET)
    print(WHITE + " LOGS     : 80 PER CYCLE" + RESET)
    print(WHITE + " SPEED    : 4 LOGS / SECOND" + RESET)
    print(WHITE + " RELOAD   : 3 SECONDS" + RESET)
    print(RED + "=" * 54 + RESET)

    cycle = 0

    while True:
        cycle += 1

        print()
        print(RED + f"========== CYCLE {cycle} ==========" + RESET)

        reload()
        logs()

        print()
        print(RED + "[ SYSTEM ] NEXT CYCLE INITIALIZING..." + RESET)

        time.sleep(1)


# ============== START ==============

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()
        print(RED + "[ MARUF ] ATTACK STOPPED" + RESET)
