import os
import base64
import random
import time

# ألوان ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
COLORS = [RED, GREEN]

def rand_color():
    return random.choice(COLORS)

def color_print(text):
    for line in text.splitlines():
        print(rand_color() + line + RESET)

def encrypt_text():
    text = input(BLUE + "Enter text to encrypt: ").strip()
    if not text:
        print(RED + "Text cannot be empty!" + RESET)
        return
    encoded = base64.b64encode(text.encode()).decode()
    print(GREEN + f"Encrypted: {encoded}")

def simulate_progress():
    total_gb = 127.0
    step = 0.1  # كل خطوة تمثل 0.1GB
    total_steps = int(total_gb / step)
    delay_per_step = (14 * 60 * 60) / total_steps  # 14 ساعة / عدد الخطوات ≈ 39.6 ثانية

    bar_length = 30  # طول شريط التحميل

    for i in range(total_steps + 1):
        current_gb = round(i * step, 1)
        percent = current_gb / total_gb
        filled_len = int(bar_length * percent)
        bar = "█" * filled_len + '-' * (bar_length - filled_len)
        print(f"{GREEN}[{bar}] Progressing {current_gb:.1f}GB / {total_gb:.1f}GB{RESET}", end='\r')
        time.sleep(delay_per_step)

    print()  # للسطر الجديد بعد الانتهاء

def decrypt_text():
    print(GREEN + "\n[✓] USB detected.\n" + RESET)
    input(YELLOW + "Press Enter to start reading data from USB... ")
    simulate_progress()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    allowed_keys = ["Nadjib1921111"]

    clear_screen()
    print(rand_color() + "🔐 Welcome to Decrypt by Maher")

    user_key = input(YELLOW + "Enter your key: ")
    if user_key not in allowed_keys:
        print(RED + "Access denied!" + RESET)
        exit()
    else:
        print(GREEN + "Access granted!\n" + RESET)

    while True:
        clear_screen()
        color_print(r"""
 _    _ _______ _______ _____  
| |  | |__   __|__   __|  __ \ 
| |  | |  | |     | |  | |__) |
| |  | |  | |     | |  |  ___/ 
| |__| |  | |     | |  | |     
 \____/   |_|     |_|  |_|     SOLO OMERTA CONTRO TUTTI
""")

        print(MAGENTA + "Decrypt by Maher")
        print("="*70)
        print("Telegram : @maher_moussa12")
        print("="*70)
        print("2011/1921\n")

        print(rand_color() + "[1] Encrypt")
        print(rand_color() + "[2] Decrypt")
        print(rand_color() + "\n[00] EXIT\n")

        choice = input(YELLOW + "Enter your choice: ").strip()

        if choice == "1":
            encrypt_text()
        elif choice == "2":
            decrypt_text()
        elif choice == "00":
            print("Exiting...")
            break
        else:
            print(RED + "Invalid choice!" + RESET)

        input(YELLOW + "\nPress Enter to continue...")

if __name__ == "__main__":
    main()
