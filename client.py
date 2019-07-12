import socket
import os
import struct
import hashlib
import pickle
import demudalate_sample as dem
import threading
''' 
addr = ('localhost', 9000)
sock = socket.socket()
sock.connect(addr)
print('Connected to', addr)
 
received = 0
chunks = []
while received< 4:
    data = sock.recv(4 - received)
    received += len(data)
    chunks.append(data)
print('Received len of file size struct', len(b''.join(chunks)))
fsize = struct.unpack('!I', b''.join(chunks))[0]
print('Filesize:', fsize)
 
buffer = 1024
received = 0
chunks = []
while received < fsize:
    data = sock.recv(min(fsize - received, buffer))
    received += len(data)
    chunks.append(data)
file = b''.join(chunks)
print('Received file')
print('Expected size:', fsize)
print('Received size:', len(file))
documento ="samples.data" 
with open(documento,'wb') as filehandle:
  pickle.dump(file, filehandle)
 
received = 0
chunks = []
while received < 64:
    data = sock.recv(64 - received)
    received += len(data)
    chunks.append(data)
sha512 = b''.join(chunks)
#print('Received Hash', len(sha512), sha512)
sock.close()
 
hash_ok = hashlib.sha512(file).digest() == sha512
print('Hash is ok') if hash_ok else print('Hash is not ok')
'''


def handle(sock):
    received = 0
    chunks = []
    while received< 4:
        data = sock.recv(4 - received)
        received += len(data)
        chunks.append(data)

    print('Received len of file size struct', len(b''.join(chunks)))
    fsize = struct.unpack('!I', b''.join(chunks))[0]
    print('Filesize:', fsize)

    buffer = 1024
    received = 0
    chunks = []
    while received < (fsize):
        data = sock.recv(min(fsize - received, buffer))
        received += len(data)
        chunks.append(data)
    

    file = b''.join(chunks)
    print('Received file')
    print('Expected size:', fsize)
    print('Received size:', len(file))
    documento ="Data/muestra.data" 

    with open(documento,'wb') as filehandle:
        filehandle.write(file)

    #################################
    with open(documento,'rb') as filehandle:
        x =pickle.load(filehandle)
    #print(x)

    ####################################3

    received = 0
    chunks = []
    while received < 64:
        data = sock.recv(64 - received)
        received += len(data)
        chunks.append(data)
    sha512 = b''.join(chunks)
    #print('Received Hash', len(sha512), sha512)
    sock.close()
    hash_ok = hashlib.sha512(file).digest() == sha512
    print('Hash is ok') if hash_ok else print('Hash is not ok')



def client():
    addr = ('', 6000)#localhost
    sock = socket.socket()
    sock.connect(addr)
    print('Connected to', addr)
    handle(sock)


#if __name__ == "__main__":
 #   indice = 1
  #  client()
    #data = dem.load(indice)
    #target=dem.frec_inte(data, indice)
   






    
    


    
    
    



 




    
    
    






  
 



    
    
    



 




