#! /usr/bin/env python

import sys

from twisted.internet import reactor
from example_secrets import mydb, main

def get_user_name(user):
    d = mydb.get_user(user)
    def extract_name(res):
        print "extract_name(%r)" % res
        if res:
            return res.name
        return "(unknown)"
    d.addCallback(extract_name)
    return d

def print_user_name(user):
    d = get_user_name(user)
    def print_name(name):
        print "print_name(%r)" % name
        print "Name:", name
        reactor.stop()
    d.addCallback(print_name)
    print "print_user_name returning"

main(print_user_name, sys.argv[1])

