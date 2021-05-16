import os, time
import keyboard
import random
from colorama import Fore, init

os.system("cls")



title = f"""
{Fore.RED}                           ┌────────────────────────────────────────────────────────────┐
{Fore.RED}                           │{Fore.RESET}      __                        _               {Fore.GREEN} ___{Fore.RED}        │
{Fore.RED}                           │{Fore.RESET}     / /  __ _ _   _ _ __   ___| |__   ___ _ __ {Fore.GREEN}/ _ \/\_/\{Fore.RED}  │
{Fore.RED}                           │{Fore.RESET}    / /  / _` | | | | '_ \ / __| '_ \ / _ \ '__{Fore.GREEN}/ /_)/\_ _/{Fore.RED}  │
{Fore.RED}                           │{Fore.RESET}   / /__| (_| | |_| | | | | (__| | | |  __/ | {Fore.GREEN}/ ___/  / \{Fore.RED}   │
{Fore.RED}                           │{Fore.RESET}   \____/\__,_|\__,_|_| |_|\___|_| |_|\___|_| {Fore.GREEN}\/      \_/{Fore.RED}   │
{Fore.RED}                           │{Fore.RESET}                                              {Fore.RED}              │
{Fore.RED}                           └────────────────────────────────────────────────────────────┘{Fore.RESET}"""
print(title)

print("")
print("                                             Client Version : Release 2.0")
print("                                                Supported Games : 4")
print("                                                 Creator : Cherful")
time.sleep(1.50)

print("")
print("                                                  ================                  ")
print("                                                  = Startup Apps =                ")
print("                                                  ================                 ")
time.sleep(1)
print("")
print("                                            Press S To Open Startup Apps")

while True:
    if keyboard.is_pressed('S'):
            print("Opening 2+ Apps. Hold Tight!")
            time.sleep(2)
            os.system("bat\startup.bat")
            os.system("succes.py")
            break
else:()
os.system("Launcher")
            
