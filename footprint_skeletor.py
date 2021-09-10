#!/usr/bin/python

### skeletor libraries
import argparse
import sys
from pyfiglet import Figlet
from termcolor import colored
import dns.resolver

#### variaveis argpase - skeletor
myquery = dns.resolver.Resolver()
target = "yahoo.com"
host = "www"
#htarget = host + "." + target

nome_app = str(sys.argv[0])
msg_usage = "\n Usage: python3 " + nome_app + " -d <dominio alvo> -w <wordlist> \n" 
msg_domain = "Informe o dominio alvo" 
### variaveis do banner
msg_font=('puffy')
msg_banner="myWHOIS" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'white')
msg_ok=colored('[+] - ','green') 
msg_att=colored('[!] - ','yellow') 
msg_wordlist = msg_att + "Informe a wordlist" 
msg_version = "Version: 0.1 " 

def func_version():
    print(msg_banner_color)
    print(" -------------------------------------------------------------------> " + msg_version)
    print()

func_version()
### skeletor

################ Inicio do seu codigo - funcao consultas classicas

def func_ns(_target):
    question = myquery.query(_target, 'NS')

    for _ns in question:
        print(_ns)


def func_mx(_target):
    question = myquery.query(_target, 'MX')

    for _mx in question:
        print(_mx)


def func_txt(_target):
    question = myquery.query(_target, 'TXT')

    for _txt in question:
        print(_txt)

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


################ Fim do seu codigo


################ Inicio do seu codigo - funcao forca bruta IPv4

def func_a(_target):
    domain = "yahoo.com"
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

#bruteforce_dns_ipv4("file.txt")


################ Fim do seu codigo

################ Inicio do seu codigo - funcao forca bruta IPv6

def func_aaaa(_target):
    domain = "yahoo.com"
    question = myquery.query(_target, 'AAAA')

    for _a in question:
        print("[+] - " + _target + "--->" + str(_a))

def bruteforce_dns_ipv6(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            try:
                target = machine + "." + domain
                func_aaaa(target)
            except:
                pass

#bruteforce_dns_ipv6("file.txt")

################ Fim do seu codigo

    
################ Inicio do seu codigo - funcao traferencia de zona


################ Fim do seu codigo

    

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-d",'--domain', action="store", dest="domain",  help=msg_domain)
    option.add_argument("-w",'--wordlist', action="store", dest="wordlist", default='wordlist.txt',  help=msg_wordlist)
    option.add_argument("-v",'--version', action="store_true", dest="version",  help=msg_version)
    option_args = option.parse_args()

    if option_args.version:
        func_version()
    
    if option_args.domain == None:
        print(option.description)
        exit(0)
    else:
        #func_dnsenum(option_args.domain)
        #bruteforce_dns_ipv4("./file.txt")
        #bruteforce_dns_ipv6("file.txt")

    #domaintarget = option_args.domain
    bruteforce_dns_ipv4("file.txt")

if __name__ == '__main__':
    func_main()

