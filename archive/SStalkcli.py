from socket import *

HOST = 'localhost'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input('> ')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if data:
            print 'Server said:\n\r' + data
tcpCliSock.close()
