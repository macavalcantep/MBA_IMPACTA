#!/usr/bin/python

import shodan
shodan_mykey='XAbsu1Ruj5uhTNcxGdbGNgrh9WuMS1B6'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target='179.191.78.194'
shodan_host = shodan_api.host(shodan_target)


def shodan_info():
    print('[*] - Informacoes genericas do ALVO')
    print('IP alvo:',shodan_host['ip_str'])
    print('Organizacao:', shodan_host.get('org','n/a'))
    print('Sistema Operacional:', shodan_host.get('os','n/a'))
    print("-" * 60)


def shodan_portscan():
        print('[*] - Identificacao de portas abertas')

        for _line in shodan_host['data']:
            print("[+} = Porta Aberta:", _line['port'])



        print("-" * 60)
        

print("-" * 60)
shodan_info()
shodan_portscan()

