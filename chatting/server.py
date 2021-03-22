from twisted.internet import protocol, reactor
import names

transports = set()
users = set()

class Chat(protocol.Protocol):
    def connectionMade(self):
        name = names.get_first_name()
        users.add(name)
        transports.add(self.transport)
        self.transport.write(f'{name}'.encode())

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        for t in transports:
            if self.transport is not t:
                t.write(data)

class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()

print('Server started!')
reactor.listenTCP(8000, ChatFactory())
reactor.run()
