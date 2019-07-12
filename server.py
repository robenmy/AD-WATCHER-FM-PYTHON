import socket
import os
import struct
import hashlib
import threading
#import read_sample as rs
import soapy_sdr as sdr
 
 
def handle(client, addr):
    buffsize = 1024
    #rs.guardar() # capturar sdr
    sdr.capturarSamples()
    file = 'muestra.data'
    print('File size:', os.path.getsize(file))
    fsize = struct.pack('!I', os.path.getsize(file))
    print('Len of file size struct:', len(fsize))
    client.send(fsize)
    with open(file, 'rb') as fd:
        while True:
            chunk = fd.read(buffsize)
            if not chunk:
                break
            client.send(chunk)
        fd.seek(0)
        hash = hashlib.sha512()
        while True:
            chunk = fd.read(buffsize)
            if not chunk:
                break
            hash.update(chunk)
        client.send(hash.digest())
    #os.remove(file)
    client.close()
 


def server():
	addr = ('', 6000)
	sock = socket.socket()
	sock.bind(addr)
	sock.listen(5)

	print ("Server Started.")
	while True:
		client, addr = sock.accept()
		print('Got connection from:', addr)
		t = threading.Thread(target=handle, args=(client, addr))
		t.start()
	sock.close()
 
 	
 	


if __name__ == '__main__':
	server()


# Variables

 
# while True loop normally
# to handle incomming connections 


#handle(client, addr)
#sock.close()
