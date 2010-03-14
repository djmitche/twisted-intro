#! /usr/bin/env python

import sys

from twisted.internet import reactor
from example_secrets import mydb, main

def print_user_info(user):
    print "looking up", user
    d = mydb.get_user(user)
    print "still thinking.."
    def got_info(res):
        print "name:", res.name
        reactor.stop()
    d.addCallback(got_info)
    print "*still* thinking.."

main(print_user_info, sys.argv[1])
