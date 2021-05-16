import os, time
import keyboard
import random
from colorama import Fore, init

number = random.randint(100000000, 10000000000)

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

print("                                             Client Version : Release 2.0")
time.sleep(0.25)
print("                                               Client ID :" ,number,)
time.sleep(0.25)
print("                                                Supported Modes : 2")
time.sleep(0.25)
print("                                                 Creator : Cherful")
time.sleep(1.50)

os.system("cls")


print(title)

time.sleep(2)
print("") 
print("                           ==================                          =================                                                              ")
print("                           = Game Selection =                          = Start-up Apps =                                                              ")
print("                           ==================                          =================                                                              ")
print("                                                                                                                                                      ")
print("                             =============                               =============                                                                ")
print("                             =     1     =                               =     2     =                                                                ")
print("                             =============                               =============                                                                ")


time.sleep(1)


while True:
    if keyboard.is_pressed('1'):
        print("Traveling!")
        os.system("Game_Selection.py")
        break

    if keyboard.is_pressed('2'):
        print("Traveling!")
        os.system("startup_apps.py")
        break