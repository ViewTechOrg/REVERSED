"""
DECRYPT BY VIEWTECH OFC KASIH STARTS MAS BRO
CREDIT SCRIPT : MaddKw
Youtubenya : https://youtube.com/@maddkw
error? benerin sendiri lah
"""

import os
import time
try:
    import rich
except (ModuleNotFoundError, ImportError):
    pass  
else:  
    try:
        import requests
except (ModuleNotFoundError, ImportError):
    else:  
        try:
            import bs4
    except (ModuleNotFoundError, ImportError):
        else:  
            try:
                import inquirer
        except (ModuleNotFoundError, ImportError):
            else:  
                try:
                    import fake_useragent
            except (ModuleNotFoundError, ImportError):
                else:  
                    import random
                    import re
                    import json
                    import sys
                    import inquirer
                    import requests
                    import marshal
                    from inquirer.render.console import ConsoleRender
                    from inquirer.render.console._list import List
                    from fake_useragent import UserAgent
                    from rich.console import Console
                    from rich.panel import Panel
                    from rich.tree import Tree
                    from datetime import datetime
                    from requests import get
                    ses = requests.Session()
                    console = Console()
                    now = datetime.now()
                    tanggal = now.strftime('%d-%m-%Y')
                    jam = datetime.now().strftime('%X')
                    ahir = str(datetime.now() - now).split('.')[0]
                    path = '/data/data/com.termux/files/usr'
                    agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
                    ipad = ses.get('http://ip-api.com/json/').json()['query']
                    warna = ['[91m', '[92m', '[93m', '[94m', '[95m', '[96m', '[97m']
                    P = '[1;97m'
                    H = '[1;92m'
                    HH = '[0;32m'
                    A = '[0;30m'
                    line = 0

                    class OtherColorList(List):
                        def get_options(self):
                            choices = self.question.choices
                            for choice in choices:
                                selected = choice == choices[self.current]
                                if selected:
                                    color = '[30;47m'
                                    symbol = '>'
                                else:  
                                    color = self.terminal.normal
                                    symbol = ' '
                                yield (choice, symbol, color)

                    class OtherListConsoleRender(ConsoleRender):
                        def render_factory(self, question_type):
                            if question_type!= 'list':
                                return super(ConsoleRender, self).render_factory(question_type)
                            return OtherColorList

                    def cetak(Text):
                        return Console(width=50, style='bold white').print(Panel(Text))

                    def berjalan(muter):
                        for mau in muter + '\n':
                            sys.stdout.write(mau)
                            sys.stdout.flush()
                            time.sleep(0.03)

                    def waktu():
                        now = datetime.now()
                        jam = datetime.now().strftime('%X')
                        hours = now.hour
                        if 0 <= hours < 11:
                            sapa = 'Selamat pagi'
                            return f'{sapa}'
                        if 11 <= hours < 15:
                            sapa = 'Selamat siang'
                            return f'{sapa}'
                        if 15 <= hours < 18:
                            sapa = 'Selamat sore'
                            return f'{sapa}'
                        if 18 <= hours <= 23:
                            sapa = 'Selamat malam'
                            return f'{sapa}'
                        sapa = 'Selamat datang'
                        return f'{sapa}'

                    def check():
                        try:
                            os.system('clear')
                            with open(f'{path}/package.json', 'r') as f:
                                pass  
                        except FileNotFoundError:
                                local_data = json.load(f)
                                    github_url = 'https://raw.githubusercontent.com/flavytrewq/ABCD/refs/heads/main/efgh/keys1.json'
                                    key_data = requests.get(github_url).json()
                                    if local_data['apikey'] in key_data['valid_keys']:
                                        print(f'{HH}[✓] API Key Valid!{P}')
                                        time.sleep(2)
                                        berjalan('\nSubscribe untuk info selanjutnya ...')
                                        time.sleep(1)
                                        os.system('xdg-open https://m.youtube.com/@MaddKW')
                                        time.sleep(3)
                                        os.system('clear')
                                        menu()
                                    else:  
                                        cetak('[bold red][×] API Key Invalid![bold white]')
                                        os.remove('package.json')
                                        time.sleep(2)
                                        main()
                                print('[1;91m[✗] package.json not found![0m')
                                os.system('clear')
                                main()
                            else:  
                                pass

                    def main():
                        url = 'https://pastebin.com/raw/W2L1Du5h'
                        req = get(url, headers={'user-agent': agent}).text
                        ___index___auto____link___ = req.split('Link: ')[1].split('|')
                        ____link____one___ = ___index___auto____link___[0]
                        ____link____two___ = ___index___auto____link___[1]
                        ____link____three___ = ___index___auto____link___[2].split('\r\nPass2: ')[0]
                        _____random____satu_____ = ____link____one___
                        _____random____dua_____ = ____link____two___
                        _____random____tiga_____ = ____link____three___
                        ________yandex________ = random.choice([_____random____satu_____.split('|'), _____random____dua_____.split('|'), _____random____tiga_____.split('|')])
                        ___link____ = get('https://tinyurl.com/api-create.php?url=' + ________yandex________[0], headers={'user-agent': agent}).text
                        cetak(f'Url token : [bold green]{___link____} ')
                        munyuk = '[bold white]Copy link diatas, lalu pastekan di browser kalian download dan setelah itu salin token dan paste kan token dibawah'
                        Console(width=50).print(Panel(munyuk, subtitle='[bold white on blue]• Login Menu •', style='bold white'))
                        pastebin_url = 'https://pastebin.com/raw/g657n7ry'
                        try:
                            pastebin_data = requests.get(pastebin_url).json()
                            key_url = pastebin_data['Key']
                            apikey = input(f'{HH}Enter your token{P}: {A}').strip()
                            time.sleep(2)
                            if apikey in pastebin_data['valid_keys']:
                                print('[1;92m[✓] API Key Valid![0m')
                                with open(f'{path}/package.json', 'w') as f:
                                    pass  
                        except requests.exceptions.RequestException as e:
                                    json.dump({'apikey': apikey}, f)
                                        time.sleep(2)
                                        check()
                            else:  
                                print('[1;91m[✗] Invalid API Key![0m')
                                os.system('clear')
                                time.sleep(2)
                                main()
                                print(f'[1;91m[✗] Error fetching API keys: {e}[0m')
                                time.sleep(2)

                    def banner():
                        jelek = '[bold white]\n\t[dark_orange3] ⣠⣤⣤⡤⠤⢤⣤⣀⡀[white]⠀⠐⠒⡄⠀⡠⠒⠀[dark_orange3]⠀⢀⣀⣤⠤⠤⣤⣤⣤⡄[white]\n\t[dark_orange3]⠈⠻⣿⡤⠤⡏[white]⠀⠉⠙⠲⣄⠀⢰⢠⠃⢀⡤⠞⠋⠉⠈[dark_orange3]⢹⠤⢼⣿⠏[white]\n\t[dark_orange3]⠀⠀⠘⣿⡅[white]⠓⢒⡤⠤⠀⡈⠱⣄⣼⡴⠋⡀⠀⠤⢤⡒⠓[dark_orange3]⢬⣿⠃[white]\t\n\t[dark_orange3]⠀⠀⠀⠹⣿⣯⣐[white]⢷⣀⣀⢤⡥⢾⣿⠷⢥⠤⣀⣀⣞[dark_orange3]⣢⣽⡿⠃[white]\t\n\t[dark_orange3]⠀⠀⠀⠀⠈⢙⣿[white]⠝⠀⢁⠔⡨⡺⡿⡕⢔⠀⡈⠐⠹[dark_orange3]⣟⠋[white]\t\t[bold white]\n\t[dark_orange3]⠀⠀⠀⠀⠀⢼⣟[white]⢦⢶⢅⠜⢰⠃⠀⢹⡌⢢⣸⠦⠴[dark_orange3]⣿⡇[white]\n\t[dark_orange3]⠀⠀⠀⠀⠀⠘⣿⣇[white]⡬⡌⢀⡟⠀⠀⠀⢷⠀⣧[dark_orange3]⢧⣵⣿⠂[white]\n\t[dark_orange3]⠀⠀⠀⠀⠀⠀⠈⢻[white]⠛⠋⠉⠀⠀⠀⠀⠈⠉⠙[dark_orange3]⢻⡏[white]\n\t[dark_orange3]⠀⠀⠀⠀⠀⠀⢰⡿[white]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[dark_orange3]⣿⠄[white]  Madd-KW Edition.\n'
                        Console(width=50).print(Panel(jelek, title=f'[bold white] {waktu()} ', subtitle='[bold white on dark_orange3] Butterfly-Spam V2 ', style='bold white'))

                    def menu():
                        os.system('rm -rf mytarget.txt')
                        os.system('clear')
                        banner()
                        tanya = [inquirer.List('Menu', message='Gunakan kursor tanda panah untuk memilih', choices=['Spam ', 'Contact '])]
                        answers = inquirer.prompt(tanya, render=OtherListConsoleRender())
                        zx = answers.get('Menu')
                        if zx == 'Spam ':
                            while True:
                                target = input(' > Masukan Nomor: ')
                                with open('mytarget.txt', 'a') as f:
                                    f.write(target + '\n')
                                print('')
                                q = [inquirer.List('lanjut', message='Mau Menambah Target?', choices=['Yes ', 'No '])]
                                jawaban = inquirer.prompt(q, render=OtherListConsoleRender())
                                if jawaban.get('lanjut') == 'No ':
                                    lef_boat()
                        if zx == 'Contact ':
                            ten = [inquirer.List('kanjut', message='Berikut merupakan kontak admin', choices=['WhatsApp ', 'Donasi '])]
                            answers = inquirer.prompt(ten, render=OtherListConsoleRender())
                            kontak = answers.get('kanjut')
                            if kontak == 'WhatsApp ':
                                os.system('xdg-open https://wa.me/+6283870666827?text=permisi+kak,+apa+saya+boleh+bertanya?')
                            else:  
                                if kontak == 'Donasi ':
                                    os.system('xdg-open https://saweria.co/MaddKW')
                        else:  
                            exit('kaga danta pisan')

                    def lef_boat():
                        os.system('clear')
                        banner()
                        cetak('\t CTRL + C, untuk berhenti spam')
                        while True:
                            os.system('touch mytarget.txt')
                            with open('mytarget.txt', 'r') as myfile:
                                lines = [line.strip() for line in myfile if line.strip()]
                            print('Kosong. Silakan jalankan ulang.')
                    pass
                    def load():
                        animasi = ['[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]
                        for i in range(len(animasi)):
                            warna_acak = random.choice(warna)
                            sys.stdout.write(f'\r      [1m{animasi[i]}[0m')
                            sys.stdout.flush()
                            time.sleep(0.1)
                        print('')

                    def countdown(seconds):
                        while seconds >= 0:
                            hours, remainder = divmod(seconds, 3600)
                            mins, secs = divmod(remainder, 60)
                            print(f'      Memulai spam kembali dalam {HH}{hours:02d}:{mins:02d}:{secs:02d}{P}', end='\r')
                            time.sleep(1)
                            seconds -= 1
                        print('\n')
                    if __name__ == '__main__':
                        os.system('git pull')
                        berjalan(f'\n{HH}{waktu()}, hengker!')
                        time.sleep(4)
                        os.system('clear')
                        check()
    print('\t ! Please wait...')
    os.system('pip install rich')
    print('\t ! Please wait...')
    os.system('pip install requests')
    print('\t ! Please wait...')
    os.system('pip install bs4')
    print('\t ! Please wait...')
    os.system('pip install inquirer')
    print('\t ! Please wait...')
    os.system('pip install fake_useragent')
