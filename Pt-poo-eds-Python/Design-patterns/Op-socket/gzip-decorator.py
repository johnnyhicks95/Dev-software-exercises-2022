import gzip
from io import BytesIO
"""Compresses data and sends it to tje client"""

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.Gzipfile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())
        
    def close(self):
        self.socket.close()
        
        
        
