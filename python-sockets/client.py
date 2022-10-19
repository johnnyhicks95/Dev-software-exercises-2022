import socket

# PUBLIC IP address
HOST = '192.164.1.1'
PORT = 9090

socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
socket.connect( ( HOST, PORT ) )

socket.send(" Hello socket world ".encode( 'utf-8' ))
print( socket.recv(1024) ).decode( 'utf-8' )

