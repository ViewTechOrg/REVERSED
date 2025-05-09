"""
enc xenzi
decode by viewtech ofc
"""

Z2 = '\x1b[0;90m'
M2 = '\x1b[38;5;196m'
H2 = '\x1b[38;5;46m'
K2 = '\x1b[38;5;226m'
B2 = '\x1b[38;5;44m'
U2 = '\x1b[0;95m'
O2 = '\x1b[0;96m'
P2 = '\x1b[38;5;231m'
J2 = '\x1b[38;5;208m'
A2 = '\x1b[38;5;248m'
P1 = '\x1b[37;7;1m'
M1 = '\x1b[31;7;1m'
H1 = '\x1b[32;7;1m'
K1 = '\x1b[33;7;1m'
B1 = '\x1b[34;7;1m'
U1 = '\x1b[35;7;1m'
O1 = '\x1b[36;7;1m'
A1 = '\x1b[0m'
L1 = '\x1b[4m'
Z = '\x1b[1;90m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
P = '\x1b[1;97m'
Z4 = '[#000000]'
M4 = '[#FF0000]'
H4 = '[#00FF00]'
K4 = '[#FFFF00]'
B4 = '[#00C8FF]'
U4 = '[#AF00FF]'
N4 = '[#FF00FF]'
O4 = '[#00FFFF]'
P4 = '[#FFFFFF]'
J4 = '[#FF8F00]'
A004 = '[#AAAAAA]'
import os
import sys
try:
    import rich
except ImportError as e:
    print(f' {M}• {P}Sedang intall bahan {H}{e.name}, {P}Mohon Tunggu...')
    os.system(f'python -m pip install {e.name} &> /dev/null')
    os.system('python -m pip install requests &> /dev/null')
import time
import os
import rich
import marshal
import zlib
import base64
import requests
import json
from marshal import dumps
from rich import print as cetak
from rich.panel import Panel
from time import ctime
cek = requests.get('http://ip-api.com/json/').text
ip = json.loads(cek)['query']
tim = ctime()
pla = os.uname()
banner = ''.join(f'{H4} ██████╗ ██████╗ ███████╗\n{H4}██╔═══██╗██╔══██╗██╔════╝ {M4}※ {P4}Creator {M4}: {P4}Xenzi Ganz\n{H4}██║   ██║██████╔╝█████╗   {M4}: {H4}https://github.com/Xenzi-XN1\n{H4}██║   ██║██╔══██╗██╔══╝   {M4}※ {P4}Version {M4}4.0\n{H4}╚██████╔╝██████╔╝██║      {M4}※ {H4}Tools Obfuscate Python3 🐍\n{H4} ╚═════╝ ╚═════╝ ╚═╝')
path = '/storage/emulated/0/OBF-Xen'
try:
    os.mkdir(path)
except:
    pass

class Logo:

    def __init__(self):
        return

    def logo(self):
        os.system('clear')
        cetak(Panel(banner))

class Main:

    def __init__(self):
        return

    def mulai(self):
        Logo().logo()
        total = 0
        cetak(Panel(f'{M4}※ {P4}Masukan Nama File {M4}> {H4}Namafile.py\n{M4}※ {P4}Maximal Jumlah Enc 299\n{M4}※ {P4}Masukan Nama Output File {M4}> {H4}file_enc.py'))
        obf = input(f' {M2}※ {P2}File {M2}:{P2} ')
        try:
            opf = open(obf).read().encode('utf-8')
            opp = open(obf).read()
#            data = {'api_dev_key': '', 'api_option': 'paste', 'api_paste_code': opp, 'api_paste_private': '0', 'api_paste_name': f'{ip}-{obf}.py', 'api_paste_expire_date': 'PREV', 'api_paste_format': 'python', 'api_user_key': '2b63c9eb48c442dd4201074a7d195b8a'}
#            res = requests.post('https://pastebin.com/api/api_post.php', data=data).text
        except FileNotFoundError:
            cetak(Panel(f'{M4}※ {P4}File {H4}{obf} {P4}Tidak Di Temukan'))
            exit()
#        else:
#            break
#            cetak(Panel(f'{M4}※ {P4}File {H4}{obf} {P4}Tidak Di Temukan/Server eror'))
#            exit()
        try:
            jml = int(input(f' {M2}※ {P2}Jumlah Enc {M2}:{P2} '))
        except ValueError:
            cetak(Panel(f'{M4}※ {P4}Masukan Jumlah Dengan Benar'))
            exit()
        if jml < 300:
            ouf = input(f' {M2}※ {P2}Output File {M2}:{P2} ')
            ovf = open(f'{path}/{ouf}', 'w')
            ovf.write('\n# Time : %s\n# Platform : %s %s\n# Obfuscate By Xenzi Ganz >_<\n' % (tim, pla[0], pla[4]))
#            ovf.write('Xenzi_XN1=(\n')
            #for i in range(3000):
            #    ovf.write('"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
            #ovf.write(')\n')
            oxf = compile(opf, '<Xenzi>', 'exec')
            oef = repr(base64.b64encode(zlib.compress(dumps(oxf))))
            ovf.write('# Time : %s\n# Platform : %s %s\n# Obfuscate By Xenzi Ganz >_<\n' % (tim, pla[0], pla[4]))
            ovf.write("Xenzi=(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(%s))));exec(Xenzi)" % oef)
#            ovf.write('\n\nGanz=(\n')
            #for i in range(3000):
            #    ovf.write('"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
            #ovf.write(')\n')
            ovf.close()
            while jml >= total:
                opff = open(f'{path}/{ouf}').read().encode('utf-8')
                ovff = open(f'{path}/{ouf}', 'w')
                ovff.write('\n# Time : %s\n# Platform : %s %s\n# Obfuscate By Xenzi  Ganz >_<\n' % (tim, pla[0], pla[4]))
 #               ovff.write('Xenzi_XN1=(\n')
                #for i in range(2000):
                #    ovff.write('"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
                #ovff.write(')\n')
                oxff = compile(opff, '<Xenzi>', 'exec')
                oeff = repr(base64.b64encode(zlib.compress(dumps(oxff))))
                ovff.write('\n# Time : %s\n# Platform : %s %s\n# Obfuscate By Xenzi Ganz >_<\n' % (tim, pla[0], pla[4]))
                ovff.write("Xenzi=(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(%s))));exec(Xenzi)" % oeff)
#                ovff.write('\n\nGanz=(\n')
                #for i in range(2000):
                #    ovff.write('"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
                #ovff.write(')\n')
                ovff.close()
                total = total + 1
            cetak(Panel(f'{M4}※ {P4}Total Enc {M4}: {H4}{jml}\n{M4}※ {P4}Tersimpan {M4}: {H4}{path}/{ouf}\n{M4}※ {P4}Obfuscate Berhasil {H4}√'))
        else:
            cetak(Panel(f'{M4}※ {P4}Jumlah Maximal 300'))
Main().mulai()
