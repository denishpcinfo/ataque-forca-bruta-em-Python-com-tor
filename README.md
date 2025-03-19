# Brute Force Login com Tor

## Descrição
Este script em Python realiza um ataque de força bruta contra uma página de login, utilizando o Tor para anonimizar as requisições. O programa tenta diferentes combinações de usuário e senha e muda o IP através do Tor a cada 5 tentativas para evitar bloqueios.

## Aviso Legal
**Este projeto é apenas para fins educacionais.** O uso não autorizado deste código para acessar sistemas sem permissão é ilegal e pode resultar em sanções legais. Use apenas em ambientes de teste e com autorização.

## Requisitos
- Python 3+
- Tor instalado e rodando (`sudo service tor start`)
- Bibliotecas necessárias (instale com o comando abaixo):
  ```bash
  pip install requests[socks]
  ```

## Como Usar
1. **Configurar o Tor**: Certifique-se de que o Tor está rodando. Ele deve estar ouvindo na porta **9050** para SOCKS5 e na porta **9051** para controle.
2. **Editar o Script**:
   - Modifique a `url` do alvo para o site desejado.
   - Ajuste as listas `usuarios` e `senhas` conforme necessário.
3. **Executar o Script**:
   ```bash
   python3 brute_force_tor.py
   ```

## Como Funciona
1. O script usa **SOCKS5** para enviar requisições HTTP através do Tor.
2. Ele tenta fazer login com combinações de nome de usuário e senha.
3. A cada 5 tentativas, muda o IP enviando um comando ao Tor.
4. Se encontrar credenciais válidas, ele exibe na tela.

## Exemplo de Uso
```
[-] Tentativa falhou: admin:123456
[-] Tentativa falhou: user:password
[+] Login encontrado: admin:admin123
```

## Segurança e Considerações
- Sites podem bloquear IPs suspeitos mesmo usando o Tor.
- Utilize em ambientes controlados para aprender sobre segurança ofensiva.
- Nunca execute testes sem permissão explícita do dono do sistema.
