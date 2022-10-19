import socket
# private ip address
HOST = '192.164.1.1'
host = socket.gethostbyname(socket.gethostname())
# print(host)
# now we configure a port, must be the same for server and client
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
# server.bind( HOST, PORT )
server.bind( host, PORT )

#begin to listen incoming connections
server.listen(5)

while True:
    # we are waiting for connections to come in
    communication_socket, address = server.accept()
    print( f"Connected to {address}" )
    # message from client
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send( f"Got your message here in server!".encode('utf-8') )
    print(f"Connection with {address} closed!")    

