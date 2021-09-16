#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+', 'green', attrs=['blink'])
nmap_start= datetime.now()

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
vanilla = pynmap.nmap_tcp_scan(target)

for _info in vanilla[target]:
    print('[' + msg1 + ']',  _info['portid'], _info['protocol'], _info['state'], _info['reason'])

nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']','Tempo de execução', nmap_time)

print()

for chave, valor in vanilla['runtime'].items():
    if chave == 'timestr':
        _time = valor
        print('[+] ' + _time)

    if chave == 'summary':
        _sum = valor
        print('[+] ' + _sum)
        

