#!/usr/bin/env python
# Read username, output from non-empty factory, drop connections
# Use deferreds, to minimize synchronicity assumptions

from twisted.internet import protocol, reactor, defer, utils, endpoints
from twisted.protocols import basic
from twisted.web import client

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        d = self.factory.getUser(user)

        def onError(err):
            return 'Internal error in server'
        d.addErrback(onError)

        def writeResponse(message):
            self.transport.write(message + b'\r\n')
            self.transport.loseConnection()
        d.addCallback(writeResponse)

# factory: doesn't get constructed for every connection
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, prefix):
        self.prefix = prefix
    #def __init__(self, users):
    #    self.users = users

    def getUser(self, user):
        return client.getPage(self.prefix + user)
        #return utils.getProcessOutput(b"finger", [user])
        #return defer.succeed(self.users.get(user, b"No such user"))

fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
fingerEndpoint.listen(FingerFactory(prefix=b'http://livejournal.com/~'))
#fingerEndpoint.listen(FingerFactory())
#fingerEndpoint.listen(FingerFactory({b'moshez': b'Happy and well'}))
reactor.run()
