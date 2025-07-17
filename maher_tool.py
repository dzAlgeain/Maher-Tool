from colorama import Fore, Style, init
import os
import time

init(autoreset=True)

# 🔑 List of accepted keys
ACCESS_KEYS = ["Nadjib1921111", "maher1921"]

def check_key():
    os.system("clear" if os.name != "nt" else "cls")
    print(Fore.CYAN + "🔐 Welcome to Maher Tool")
    key = input(Fore.YELLOW + "Enter your key: " + Fore.RESET)
    if key not in ACCESS_KEYS:
        print(Fore.RED + "Invalid key! Access denied.")
        exit()
    print(Fore.GREEN + "Access granted!\n")
    time.sleep(1)

def banner():
    print(Fore.YELLOW + Style.BRIGHT + r"""
  ___  ____   ___   ___ 
 |__ \|___ \ / _ \ / _ \
    ) | __) | | | | | | |
   / / |__ <| |_| | |_| |
  |_| |___/ \___/ \___/ 
    """)
    print(Fore.MAGENTA + "</> Author: Maher | Maher Project")
    print(Fore.MAGENTA + "=" * 60)
    print(Fore.CYAN + "Telegram: https://t.me/maher_moussa12")
    print(Fore.MAGENTA + "=" * 60)
    print(Fore.GREEN + "2011/1921\n")

def menu():
    print(Fore.CYAN + "[1] Instagram")
    print(Fore.MAGENTA + "[2] Facebook")
    print(Fore.BLUE + "\n[00] EXIT")

def instagram_menu():
    print(Fore.CYAN + "\n[1] Group publication know")
    print(Fore.MAGENTA + "[2] Account access (cookies method)")
    print(Fore.BLUE + "[0] Back")

    while True:
        sub_choice = input(Fore.YELLOW + "Select Instagram option: " + Fore.RESET)
        if sub_choice == "1":
            print(Fore.GREEN + "Selected: Group publication know")
            link = input(Fore.CYAN + "Link of publication: " + Fore.RESET)
            print(Fore.GREEN + f"Received link: {link}")
            print(Fore.YELLOW + "Please wait until validation...\n")
            time.sleep(1)
            break
        elif sub_choice == "2":
            print(Fore.GREEN + "Selected: Account access (cookies method)")
            account = input(Fore.CYAN + "Account name: " + Fore.RESET)
            print(Fore.GREEN + f"Received account: {account}")
            print(Fore.YELLOW + "Please wait until validation...\n")
            time.sleep(1)
            break
        elif sub_choice == "0":
            break
        else:
            print(Fore.RED + "Invalid option. Try again.")

def main():
    check_key()
    banner()
    menu()

    while True:
        choice = input(Fore.YELLOW + "\nEnter your choice: " + Fore.RESET)
        if choice == "00" or choice.lower() == "exit":
            print(Fore.RED + "Exiting...")
            break
        elif choice == "1":
            instagram_menu()
        elif choice == "2":
            print(Fore.GREEN + "Launching Facebook module...")
        else:
            print(Fore.RED + "Invalid option. Try again.")

if __name__ == "__main__":
    main()
