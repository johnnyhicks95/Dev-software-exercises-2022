import socket
"""
1.Start the server in one terminal
2. Open a second terminal window and run the client
3. Enter a value in prompt
4. Send the value, execute again client to watch the received data
"""

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#name , port number
client.connect(('localhost', 2401))
print("Received: {0}".format(client.recv(1024) ))
client.close




