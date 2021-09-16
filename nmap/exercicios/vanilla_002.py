#!/usr/bin/python

import nmap3

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
vanilla = pynmap.nmap_tcp_scan(target)

for _info in vanilla[target]:
    print(_info['portid'], _info['protocol'], _info['state'], _info['reason'])


