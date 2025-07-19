import os
import base64
import random

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
    text = input(BLUE + "Enter text to encrypt: ")
    encoded = base64.b64encode(text.encode()).decode()
    print(GREEN + f"Encrypted: {encoded}")

def decrypt_text():
    # تظهر الرسالة وكأنها خطأ لتنبيه المستخدم
    print(RED + "\n[ERROR] Please plug the flash disk (USB)!\n" + RESET)
    input(YELLOW + "Press Enter after plugging the USB... ")
    print(GREEN + "Waiting for USB data...")  # وهمية

def main():
    allowed_keys = ["Nadjib1921111"]

    # تنظيف الشاشة
    os.system("cls" if os.name == "nt" else "clear")
    print(rand_color() + "🔐 Welcome to Decrypt by Maher")

    # التحقق من المفتاح
    user_key = input(YELLOW + "Enter your key: ")
    if user_key in allowed_keys:
        print(rand_color() + "Access granted!\n")
    else:
        print(rand_color() + "Access denied!")
        exit()

    # شعار UTTP
    color_print(r"""
 _    _ _______ _______ _____  
| |  | |__   __|__   __|  __ \ 
| |  | |  | |     | |  | |__) |
| |  | |  | |     | |  |  ___/ 
| |__| |  | |     | |  | |     
 \____/   |_|     |_|  |_|     SOLO OMERTA CONTRO TUTTI
""")

    # معلومات المؤلف
    print(MAGENTA + "Decrypt by Maher")
    print("="*70)
    print("Telegram : @maher_moussa12")
    print("="*70)
    print("2011/1921\n")

    # القائمة
    print(rand_color() + "[1] Encrypt")
    print(rand_color() + "[2] Decrypt")
    print(rand_color() + "\n[00] EXIT\n")

    choice = input(YELLOW + "Enter your choice: ")

    # تنفيذ الخيارات
    if choice == "1":
        encrypt_text()
    elif choice == "2":
        decrypt_text()
    elif choice == "00":
        print("Exiting...")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
