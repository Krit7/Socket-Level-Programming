#Client
import socket
import pickle
from io import StringIO
from struct import *

def decompress(compressed):
    """Decompress a list of output ks to a string."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()

def file_client():

	BUF_SIZE = 1024
	print('File Transfer Client')
	host = socket.gethostbyname('')  # Enter the host address of the of the system on which the server is running  
	port = 4000						

	s = socket.socket()
	s.connect((host, port))

	f = open('file.txt','rb')	
	l = f.read(BUF_SIZE) 
	while(l):
		s.send(l)
		print('Sent file:-', repr(l))
		l = f.read(BUF_SIZE)
	f.close()
	s.close()
	
	print('-----------------------------')
	print('        File Uploaded        ')
	print('-----------------------------')

	print('-----------------------------')
	print('   Press Enter to download:  ')
	print('-----------------------------')
	input()

	s = socket.socket()
	s.connect((host, port))	
	f = open('compressed.lzw', 'wb')
	while(True):
		data = s.recv(BUF_SIZE)
		if not data: break
		f.write(data)	
	f.close()	
	
	print('-----------------------------')
	print('       File Downloaded       ')
	print('-----------------------------')

	compressed = []
	f = open('compressed.lzw', 'rb')
	data = f.read(2)
	while(data):
		compressed.append(unpack('>H',data)[0])
		data = f.read(2)

	decompressed = decompress(compressed)
	with open('decompressed.txt', 'w') as f:
		f.write(decompressed)
	
	print(decompressed)

	s.close()
	print("Client Disconnected")


if __name__ == '__main__':
	file_client()

	




