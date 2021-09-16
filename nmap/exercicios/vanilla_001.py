#!/usr/bin/python

import nmap3
import json

pynmap = nmap3.NmapScanTechniques()

target = '11.11.11.171'

vanilla = pynmap.nmap_tcp_scan(target)

vanilla_json = json.dumps(vanilla, indent = 6)

print(vanilla_json)

