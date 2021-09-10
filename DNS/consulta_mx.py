#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
target = "yahoo.com"

def func_mx(_target):
    question = myquery.query(_target, 'MX')

    for _mx in question:
        print(_mx)

func_mx(target)


