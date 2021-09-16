#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+', 'green', attrs=['blink'])
msg2 = colored('+', 'cyan')
nmap_start= datetime.now()

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
finscan = pynmap.nmap_fin_scan(target)

print('Porta:', finscan['ports']['portid'])
print('Protocolo', finscan['ports']['protocol'])
print('Serviço:', finscan['ports']['service']['name'])
print('Estado:', finscan['ports']['state']['state'])



nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']','Tempo de execução', nmap_time)

print()        
