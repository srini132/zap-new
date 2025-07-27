import requests
from bs4 import BeautifulSoup
import socket

def check_url_response(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"[+] {url} responded with status code: {response.status_code}")
        return response
    except Exception as e:
        print(f"[-] Failed to reach {url}: {e}")
        return None

def check_http_headers(headers):
    print("[*] Checking HTTP headers for security issues...")
    security_headers = [
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-XSS-Protection"
    ]
    for header in security_headers:
        if header not in headers:
            print(f"[!] Missing security header: {header}")
        else:
            print(f"[+] Present: {header}")

def extract_forms(html):
    print("[*] Scanning for HTML forms...")
    soup = BeautifulSoup(html, 'html.parser')
    forms = soup.find_all('form')
    for i, form in enumerate(forms, 1):
        print(f"  - Form #{i}: action={form.get('action')} method={form.get('method')}")

def find_common_vuln_patterns(html):
    print("[*] Checking page for common vulnerable code patterns...")
    keywords = ['eval(', 'document.write(', 'innerHTML', 'onclick=', 'onerror=']
    for keyword in keywords:
        if keyword in html:
            print(f"[!] Possible unsafe code found: {keyword}")

def port_scan(host):
    print(f"[*] Scanning ports on {host}...")
    ports = [21, 22, 23, 25, 80, 443, 3306]
    for port in ports:
        try:
            sock = socket.create_connection((host, port), timeout=1)
            print(f"[+] Port {port} is open")
            sock.close()
        except:
            pass
