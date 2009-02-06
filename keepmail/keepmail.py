"""
A dummy mail server.
"""

from zope.interface import implements

from twisted.internet import defer
from twisted.mail import smtp

class ConsoleMessageDelivery:
    implements(smtp.IMessageDelivery)

    def receivedHeader(self, helo, origin, recipients):
        return "Received: ConsoleMessageDelivery"
    
    def validateFrom(self, helo, origin):
        # All addresses are accepted
        return origin
    
    def validateTo(self, user):
        return lambda: ConsoleMessage()

class ConsoleMessage:
    implements(smtp.IMessage)
    
    def __init__(self):
        self.lines = []
    
    def lineReceived(self, line):
        self.lines.append(line)
    
    def eomReceived(self):
        print "New message received:"
        print "\n".join(self.lines)
        self.lines = None
        return defer.succeed(None)
    
    def connectionLost(self):
        # There was an error, throw away the stored lines
        self.lines = None

class KeepmailSMTPFactory(smtp.SMTPFactory):
    def __init__(self, *a, **kw):
        smtp.SMTPFactory.__init__(self, *a, **kw)
        self.delivery = ConsoleMessageDelivery()
    
    def buildProtocol(self, addr):
        p = smtp.SMTPFactory.buildProtocol(self, addr)
        p.delivery = self.delivery
        return p
