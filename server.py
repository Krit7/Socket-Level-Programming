#Server
import socket
import pickle
from struct import *

def compress(uncompressed):
	dict_size = 256
	dictionary = {chr(i): i for i in range(dict_size)}

	w = ""
	result = []
	for c in uncompressed:
		wc = w + c
		if wc in dictionary:
			w = wc
		else:
			result.append(dictionary[w])
			# Add wc to the dictionary.
			dictionary[wc] = dict_size
			dict_size += 1
			w = c
	if w in dictionary:
		result.append(dictionary[w])
	return result

def file_server():

	print("File Transfer Server")
	host = ''
	port = 4000

	s = socket.socket()
	# s.settimeout(10)
	print ("Socket successfully created")
	s.bind((host, port))
	print ("Socket binded to %s" %(port))
	s.listen(5)

	print ("Server is listening...")

	conn, addr = s.accept()
	print('Got connection from', addr)
	
	data_recvd = ''
	while True:
		data = conn.recv(1024)
		if not data: 
			break	
		#DATA RECEIVED
		data=data.decode('utf8')
		print('Received',repr(data))
		data_recvd += data		
	
	conn.close()
	
	print('---------------------------')
	print('      File received        ')
	print('---------------------------')

	compressed = compress(data_recvd)
	temp = open("tmp.lzw", "wb")
	for data in compressed:
		temp.write(pack('>H',int(data)))
	temp.close()

	#print(compressed)

	print('---------------------------')
	print('      File Compressed      ')
	print('---------------------------')

	conn, addr = s.accept()
	f = open('tmp.lzw', 'rb')
	l = f.read()
	while(l):
		conn.send(l)
		# print('Sent', repr(l))
		l = f.read(1024)
	f.close()

	print('---------------------------')
	print('         File Sent         ')
	print('---------------------------')

	conn.close()
	print("Server Disconnected")


if __name__ == '__main__':
	file_server()







