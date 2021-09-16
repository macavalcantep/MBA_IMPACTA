#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+', 'green', attrs=['blink'])
msg2 = colored('+', 'cyan')
nmap_start= datetime.now()

target = '11.11.11.171'

pynmap = nmap3.Nmap()
versionscan = pynmap.nmap_version_detection(target)

for _info in versionscan:
    print('[' + msg1 + ']',  _info['port'], _info['protocol'], _info['state'], _info['reason'])

    for chave, valor in _info['service'].items():
        print(' - [' + msg2 + ']', chave, valor)
    print()


nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']','Tempo de execução', nmap_time)

print()

