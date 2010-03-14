#! /usr/bin/env python

import sys

from twisted.internet import reactor
from example_secrets import get_page_title, main

def print_page_title(url):
    print "fetching", url
    d = get_page_title(url)
    def got_info(title):
        print "title:", title
        reactor.stop()
    def fail_info(f):
        print "failed!", f
        reactor.stop()
    d.addCallbacks(got_info, fail_info)

main(print_page_title, sys.argv[1])

