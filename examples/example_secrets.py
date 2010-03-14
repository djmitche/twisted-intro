# secret stuff that shouldn't confuse the issue in example 1

from urllib2 import URLError

from twisted.internet import defer, reactor
from twisted.python import failure

# a fake database
class User(object):
    def __init__(self, name):
        self.name = name

class MyDB(object):
    users = {
            'dustin' : User('Dustin'),
            'karl' : User('Karl'),
            }

    def get_user(self, user):
        d = defer.Deferred()
        def result_ready():
            u = self.users[user]
            d.callback(u)
        reactor.callLater(1.5, result_ready)
        return d

mydb = MyDB()

def get_page_title(url):
    d = defer.Deferred()
    def result_ready():
        if url == 'http://buildbot.net':
            d.callback('Buildbot')
        else:
            d.errback(failure.Failure(URLError("404 Not Found")))
    reactor.callLater(.5, result_ready)
    return d

def main(fn, arg):
    reactor.callWhenRunning(fn, arg)
    reactor.run()
