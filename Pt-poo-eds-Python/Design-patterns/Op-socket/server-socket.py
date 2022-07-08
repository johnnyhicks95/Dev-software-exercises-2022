""" 
TCP socket , takes a string of input bytes and outputs to the receiving socket
at the other end.
"""

import socket

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes( response, 'utf8' ) )
    client.close()
    
server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.bind( ( 'localhost', 2401 ) )
server.listen(1)

try:
    while True:
        client, addr = server.accept()
        respond(client)
        # respond(LogSocket(client))

finally:
    server.close()    
    

# Loggin decorator, outputs    
class LogSocket:
    """Decorator class, prints message while sendin,
    closes connection when it's done"""
    def __init__( self, socket ):
        self.socket = socket
    
    def send(self, data):
        print("Sending {0} to {1}".format(
            data, self.socket.getpeername()[0]
        ))
        self.socket.send(data)
        
    def close(self):
        self.socket.close()

client, addr = server.accept()
if log_send:
    client = LoggingSocket(client)

if client.getpeername()[0] in compress_hosts:
    client = GzipSocket(client)
respond(client)


