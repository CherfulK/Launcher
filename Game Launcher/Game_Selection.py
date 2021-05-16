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
print("                               ============             ========           =================            ")
print("                               = Valorant =             = CarX =           = Rocket League =            ")
print("                               ============             ========           =================            ")
print("")
print("                                            ============          ==============            ")
print("                                            = Fortnite =          = OBS Studio =            ")
print("                                            ============          ==============            ")
time.sleep(1)
print("")

print("                                              Press V To Open Valorant")
print("")
print("                                            Press R To Open Rocket League")
print("")
print("                                                Press C To Open CarX")
print("")
print("                                              Press F To Open Fortnite")
print("")
print("                                             Press O To Open OBS Studio")

while True:
    if keyboard.is_pressed('v'):
        print("Launching!")
        os.system("bat\Valorant.bat")
        os.system("succes.py")
        break

    if keyboard.is_pressed('c'):
            print("Launching!")
            os.system("bat\CarX.bat")
            os.system("succes.py")
            break

    if keyboard.is_pressed('R'):
            print("Launching!")
            os.system("bat\RL.bat")
            break

    if keyboard.is_pressed('F'):
            print("Launching!")
            os.system("bat\Fnbr.bat")
            os.system("succes.py")
            break

    if keyboard.is_pressed('O'):
            print("Launching!")
            os.system("bat\Obs.bat")
            os.system("succes.py")
            break