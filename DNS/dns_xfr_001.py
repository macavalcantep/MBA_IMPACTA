#!/usr/bin/python

import dns.query
import dns.zone

domain = 'yellow.dojo'
target = 'ns.yellow.dojo'

transfzone = dns.zone.from_xfr(dns.query.xfr(target, domain))

for _machines in transfzone:
    print('[+] -', str(_machines) + '.' + domain)

