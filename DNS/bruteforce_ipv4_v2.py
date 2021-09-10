#!/usr/bin/python

import dns.resolver
from threading import *
myquery = dns.resolver.Resolver()
domain = "yahoo.com"
#host ="www"
#target = host + "." + domain

def func_a(_target):
    question = myquery.query(_target, 'A')

    for _addr in question:
        print('[+] - ' + _target + '---> ' + str(_addr))

def bruteforce_dns_ipv4(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break

            try:
                target = machine + "." + domain
                func_a(target)
            
            except:
                pass

#bruteforce_dns_ipv4("file.txt")
thread_ipv4 = Thread(target=bruteforce_dns_ipv4,args=('file.txt',))
thread_ipv4.start()


