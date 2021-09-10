#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
domain = "yahoo.com"
host ="www"
target = host + "." + domain

def func_aaaa(_target):
    question = myquery.query(_target, 'AAAA')

    for _addr in question:
        print(_addr)

func_aaaa(target)


