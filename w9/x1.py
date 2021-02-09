import socket

#creates a socket to the internet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to a server and a host
mysock.connect(('data.pr4e.org', 80))
#http command
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    #receive up to 512 caracters
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
