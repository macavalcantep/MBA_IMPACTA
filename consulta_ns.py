#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
target = "yahoo.com"
host = "www"
htarget = host + "." + target

#Colocar em um arquivo consula_ns.py
def func_ns(_target):
    question = myquery.query(_target, 'NS')

    for _ns in question:
        print(_ns)

#Colocar em um arquivo consula_mx.py
def func_mx(_target):
    question = myquery.query(_target, 'MX')

    for _mx in question:
        print(_mx)

#Colocar em um arquivo consula_txt.py
def func_txt(_target):
    question = myquery.query(_target, 'TXT')

    for _txt in question:
        print(_txt)

#Colocar em um arquivo consula_a.py
def func_a(_target):
    question = myquery.query(_target, 'A')

    for _a in question:
        print("[+] - " + _target + "--->" + str(_a))

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

bruteforce_dns_ipv4("file.txt")

#Colocar em um arquivo consula_aaaa.py
def func_aaaa(_htarget):
    question = myquery.query(_htarget, 'AAAA')

    for _a in question:
        print(_a)

print("#" * 60)
print("Consultas classicas de DNS - NS, MX, TXT")

def func_dnsenum(target):
    print("#" * 60)
    print("Lista de servidores DNS do dominio\n")
    func_ns(target)
    print()
    print("#" * 60)
    print("Lista de servidores MX do (Mail eXchange do dominio)\n")
    func_mx(target)
    print()
    print("#" * 60)
    print("Informações de servidores TXT do dominio\n")
    func_txt(target)
    print()
    # func_a(htarget)
    # func_aaaa(htarget)

func_dnsenum(target)


